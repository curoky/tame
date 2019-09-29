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

from jinja2 import Template

from src.config import repo_config


class Builder(object):

    def __init__(self, root, thread_num):
        self.root = root
        self.logger = logging.getLogger(__name__)
        self.thread_num = thread_num
        self.env = None

    def _prepare_env(self, install_paths: [str]):
        self.env = dict()
        self.env["PATH"] = ":".join([
            os.path.join(p, "bin") for p in install_paths
        ]) + ":" + os.environ["PATH"]

        self.env["PKG_CONFIG_PATH"] = ":".join(
            [os.path.join(p, "lib/pkgconfig") for p in install_paths])

        # Just use for automake
        self.dep_libs = ""
        self.dep_incs = ""
        for p in install_paths:
            self.dep_libs += "-L%s " % os.path.join(p, "lib")
            self.dep_incs += "-I%s " % os.path.join(p, "include")
        self.env["LDFLAGS"] = '%s' % self.dep_libs
        self.env["CPPFLAGS"] = '%s' % self.dep_incs
        self.env["CFLAGS"] = self.env["CPPFLAGS"]
        # self.env["LIBS"] = '-lncurses'
        # self.env["CXXFLAGS"] = '-I%s' % os.path.join(self.deps_path, "include")

        # for perl
        self.env["PERL5LIB"] = ":".join(
            [os.path.join(p, "lib/perl5") for p in install_paths])

    def build(self, target, all_install_paths):

        build = repo_config[target.repo_name]["build"]
        build_cmd = " && ".join(build["step"])
        build_path = os.path.join(target.repo_path, build["build_path"])

        if self.check_build_mark(target.repo_name):
            self.logger.info("[%s]: already build", target.repo_name)
            return 0

        if build["type"] == "cmake":
            cmd = Template(build_cmd).render(
                cmake_prefix=";".join(all_install_paths),
                install_path=target.install_path,
                repo_path=target.repo_path,
                thread_num=self.thread_num)
        elif build["type"] == "configure":
            self._prepare_env(all_install_paths)
            cmd = Template(build_cmd).render(install_path=target.install_path,
                                             repo_path=target.repo_path,
                                             thread_num=self.thread_num)
        else:
            self._prepare_env(all_install_paths)
            cmd = Template(build_cmd).render(install_path=target.install_path,
                                             repo_path=target.repo_path,
                                             thread_num=self.thread_num)

        if not os.path.exists(build_path):
            os.makedirs(build_path)

        self.logger.info("start to build %s\n\tcmd: %s\n\tenv: %s",
                         target.repo_name, cmd, self.env)
        res = subprocess.Popen(cmd,
                               cwd=build_path,
                               env=self.env,
                               shell=True,
                               stdout=sys.stdout,
                               stderr=sys.stderr)
        retcode = res.wait()
        if retcode == 0:
            self._write_build_mark(target.repo_name)
        return retcode

    def check_build_mark(self, repo_name):
        mark = self._load_build_mark()
        if mark and repo_name in mark:
            return True
        return False

    def _write_build_mark(self, repo_name):
        mark_path = os.path.join(self.root, "VERSION")
        mark = self._load_build_mark()
        if not mark:
            mark = {}
        if repo_name not in mark:
            mark[repo_name] = time.strftime("%Y-%m-%dT%H:%M:%SZ",
                                            time.localtime())
            with codecs.open(mark_path, "w", "utf8") as f:
                f.write(json.dumps(mark))
        self.logger.info("[%s] write build version", repo_name)

    def _load_build_mark(self):
        mark_path = os.path.join(self.root, "VERSION")
        if os.path.isfile(mark_path):
            with codecs.open(mark_path, "r", "utf8") as f:
                return json.loads(f.read())
