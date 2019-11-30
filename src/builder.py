#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

import codecs
import json
import logging
import os
import subprocess
import sys
import time
import shutil

from jinja2 import Template


class Builder(object):

    def __init__(self, root, global_config, thread_num):
        self.root = root
        self.global_config = global_config
        self.thread_num = thread_num

        self.logger = logging.getLogger("builder")

    @staticmethod
    def _prepare_env(include_paths):
        env = dict()
        env["PATH"] = ":".join([os.path.join(p, "bin") for p in include_paths
                               ]) + ":" + os.environ["PATH"]

        env["PKG_CONFIG_PATH"] = ":".join(
            [os.path.join(p, "lib/pkgconfig") for p in include_paths] +
            [os.path.join(p, "share/pkgconfig") for p in include_paths])

        env["LD_LIBRARY_PATH"] = ":".join(
            [os.path.join(p, "lib") for p in include_paths])
        # Just use for automake
        dep_libs = ""
        dep_incs = ""
        for p in include_paths:
            dep_libs += "-L%s " % os.path.join(p, "lib")
            dep_incs += "-I%s " % os.path.join(p, "include")
        env["LDFLAGS"] = '%s' % dep_libs
        env["CPPFLAGS"] = '%s' % dep_incs
        env["CFLAGS"] = env["CPPFLAGS"]
        # env["LIBS"] = '-lncurses'
        # env["CXXFLAGS"] = '-I%s' % os.path.join(deps_path, "include")

        # for perl
        env["PERL5LIB"] = ":".join(
            [os.path.join(p, "lib/perl5") for p in include_paths])
        return env

    def build(self, package_list, include_paths):

        for package in package_list:

            if os.path.isdir(package.install_path) and os.listdir(
                    package.install_path):
                self.logger.info("[%s]: already build", package.dirname)
                include_paths.add(package.install_path)
                continue

            build = self.global_config[package.repo_name]["build"]
            build_cmd = " && ".join(build["step"])
            package.build_path = os.path.join(package.download_path,
                                              build["build_path"])

            env = self._prepare_env(include_paths)

            cmd = Template(build_cmd).render(
                cmake_prefix=";".join(include_paths),
                install_path=package.install_path,
                repo_path=package.download_path,
                build_path=package.build_path,
                thread_num=self.thread_num)

            if not os.path.exists(package.build_path):
                os.makedirs(package.build_path)

            self.logger.info(
                "start to build %s\n\tcmd: %s\n\tenv: %s", package.repo_name,
                cmd,
                json.dumps(env, sort_keys=True, indent=4,
                           separators=(',', ':')))
            res = subprocess.Popen(cmd,
                                   cwd=package.build_path,
                                   env=env,
                                   shell=True,
                                   stdout=sys.stdout,
                                   stderr=sys.stderr)
            retcode = res.wait()
            if retcode != 0:
                shutil.rmtree(package.install_path, ignore_errors=True)
                self.logger.critical("build error with %d", retcode)

            include_paths.add(package.install_path)

    def install(self, path):
        pass

    def remove(self, name):
        pass
