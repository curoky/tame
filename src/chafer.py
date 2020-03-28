#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        : manage mirror file

import logging
import os

from . import Package
from .builder import Builder
from .depender import Depender
from .downloader import Downloader
from .helper import ConfigHelper, EnvHelper, InfoHelper


class Chafer(object):

    def __init__(self, root, thread_num, proxies, verbose):
        if not os.path.exists(root):
            os.makedirs(root)

        self.root = root
        self.archive_prefix = os.path.join(self.root, 'archive')
        self.extract_prefix = os.path.join(self.root, 'extract')
        self.install_prefix = os.path.join(self.root, 'install')
        os.makedirs(self.root, exist_ok=True)
        os.makedirs(self.archive_prefix, exist_ok=True)
        os.makedirs(self.extract_prefix, exist_ok=True)
        os.makedirs(self.install_prefix, exist_ok=True)

        self.pkg_list = []
        self.config_helper = ConfigHelper()
        self.modules = self.config_helper.get_modules()
        self.info_helper = InfoHelper(self.modules)

        self.depender = Depender(self.modules)
        self.downloader = Downloader(proxies)
        self.builder = Builder()

        self.proxies = proxies
        self.verbose = verbose
        self.thread_num = thread_num
        self.logger = logging.getLogger('main')
        self.debug()

    def prepare(self, name, with_deps, inc_list: [str] = None):
        if with_deps:
            deps = self.depender.get_deps(name)
            deps = self.depender.sort_deps(deps)
        else:
            deps = [name]
        inc_list = inc_list or []
        inc_map = {}
        self.pkg_list.clear()
        for d in deps:
            pkg = Package(d,
                          self.archive_prefix,
                          self.extract_prefix,
                          self.install_prefix,
                          self.modules[d],
                          thread_num=self.thread_num,
                          verbose=self.verbose)
            inc_map[d] = pkg.install_path
            inc_list.append(pkg.install_path)
            pkg.prepare_build_opt(inc_list, inc_map)
            self.pkg_list.append(pkg)

        self.logger.info('build target list: %s', [p.name for p in self.pkg_list])

    def download(self):
        self.downloader.download(self.pkg_list)

    def build(self):
        self.builder.build(self.pkg_list)

    def gen(self):
        bash_file = os.path.join(self.root, 'main.sh')
        cmake_file = os.path.join(self.root, 'FindCmakePrefixConfig.cmake')
        EnvHelper.generator_bash_file(self.install_prefix, bash_file)
        EnvHelper.generator_cmake_file(self.install_prefix, cmake_file)

    def list(self):
        self.info_helper.list(self.install_prefix)

    def show(self, name):
        self.info_helper.show(name)

    def debug(self):
        self.logger.debug('with proxies: %s', self.proxies)
        self.logger.debug('with thread_num: %d', self.thread_num)
        self.logger.debug('with archive_prefix: %d', self.archive_prefix)
        self.logger.debug('with extract_prefix: %d', self.extract_prefix)
        self.logger.debug('with install_prefix: %d', self.install_prefix)

    def new(self, name):
        self.config_helper.new(name)
