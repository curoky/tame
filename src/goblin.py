#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        : manage mirror file

import logging
import os

from . import TargetInfo
from .builder import Builder
from .depender import Depender
from .downloader import Downloader, global_info


class Goblin(object):
    """
    主要负责全局的资源管理
    """

    def __init__(self, root, name, versions, install_path, build_thread_num,
                 download_thread_num):
        self.name = name
        self.root = root
        self.install_path = install_path
        self.logger = logging.getLogger(__name__)

        self.builder = Builder(root, build_thread_num)
        self.depender = Depender()
        self.downloader = Downloader(root, download_thread_num)

        if not os.path.exists(self.root):
            os.makedirs(self.root)

        self.targets_list = []
        self.targets_map = {}
        self._prepare_target_info(versions)

    def _prepare_target_info(self, versions: dict):
        deps = self.depender.get_deps_list(self.name)
        for dep in deps:
            t = TargetInfo(root=self.root,
                           name=dep,
                           install_path=self.install_path,
                           version=versions.get(dep,
                                                global_info[dep]["version"][0]),
                           force_build=False)
            self.targets_list.append(t)
            self.targets_map[dep] = t

    def update(self, update_deps, proxies):
        need_update_targets = self.targets_list if update_deps else self.targets_list[
            -1:]

        if proxies:
            self.logger.info("use proxy: %s", str(proxies))
        self.downloader.downloads(repos=dict(
            (t.name, t.version) for t in need_update_targets),
                                  proxies=proxies)

    def build(self, build_deps, force_build):
        self.targets_map[self.name].force_build = force_build
        need_build_deps = self.targets_list if build_deps else self.targets_list[
            -1:]

        self.logger.info("start to build \ndeps[%s]",
                         [t.name for t in need_build_deps])

        for t in need_build_deps:
            ret = self.builder.build(t.name, self.targets_map)
            if ret != 0:
                self.logger.critical("build error with %d", ret)
