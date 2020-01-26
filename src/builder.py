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
    def _prepare_env(include_paths, gcc_path):
        env = dict()
        base_path = "/bin:/usr/bin/:/usr/local/bin:/usr/sbin/"

        env["PATH"] = ":".join([os.path.join(p, "bin") for p in include_paths
                               ]) + ":" + base_path

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

        env["CXXFLAGS"] = env["CPPFLAGS"]
        # for perl
        env["PERL5LIB"] = ":".join(
            [os.path.join(p, "lib/perl5") for p in include_paths])
        if gcc_path:
            gcc_path = os.path.expanduser(gcc_path)
        if gcc_path:
            env["PATH"] = gcc_path + "/bin:" + env["PATH"]
            env["LD_LIBRARY_PATH"] = gcc_path + "/lib:" + env["LD_LIBRARY_PATH"]
            env["LD_LIBRARY_PATH"] = gcc_path + "/lib64:" + env[
                "LD_LIBRARY_PATH"]
            env["CC"] = gcc_path + "/bin/gcc"
            env["CXX"] = gcc_path + "/bin/g++"
        return env

    def build(self, target_infos, include_paths, gcc_path):
        deps_paths = {}
        for target in target_infos:
            if os.path.isdir(target.install_path) and os.listdir(
                    target.install_path):
                self.logger.info("[%s]: already build", target.dirname)
                include_paths.add(target.install_path)
                deps_paths[target.repo_name] = target.install_path
                continue

            build = self.global_config[target.repo_name]["build"]
            build_cmd = " && ".join(build["step"])
            target.build_path = os.path.join(target.download_path,
                                             build["build_path"])

            env = self._prepare_env(include_paths, gcc_path)

            cmd = Template(build_cmd).render(
                cmake_prefix=";".join(include_paths),
                install_path=target.install_path,
                repo_path=target.download_path,
                build_path=target.build_path,
                thread_num=self.thread_num,
                deps_paths=deps_paths)

            if not os.path.exists(target.build_path):
                os.makedirs(target.build_path)

            self.logger.info(
                "start to build %s\n\tcmd: %s\n\tenv: %s", target.repo_name,
                cmd,
                json.dumps(env, sort_keys=True, indent=4,
                           separators=(',', ':')))
            res = subprocess.Popen(cmd,
                                   cwd=target.build_path,
                                   env=env,
                                   shell=True,
                                   stdout=sys.stdout,
                                   stderr=sys.stderr)
            retcode = res.wait()
            if retcode != 0:
                shutil.rmtree(target.install_path, ignore_errors=True)
                self.logger.critical("build error with %d", retcode)

            include_paths.add(target.install_path)
            deps_paths[target.repo_name] = target.install_path

    def install(self, path):
        pass

    def remove(self, name):
        pass
