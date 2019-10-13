#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        : manage mirror file

import logging
import os

from . import Target
from .builder import Builder
from .depender import Depender
from .downloader import Downloader

from .config import register_all, repo_config


class Chafer(object):
    """
    主要负责全局的资源管理
    """

    def __init__(self, root, repo_name, versions, install_path,
                 build_thread_num):
        register_all()
        self.repo_name = repo_name
        self.root = root
        self.install_path = install_path
        self.logger = logging.getLogger(__name__)

        self.builder = Builder(root, build_thread_num)
        self.depender = Depender()
        self.downloader = Downloader(root)

        if not os.path.exists(self.root):
            os.makedirs(self.root)

        self.target_list = []
        self.prepare_targets(versions)

    def prepare_targets(self, versions: dict):
        repo_names = self.depender.get_deps_list(self.repo_name)
        for repo_name in repo_names:
            t = Target(self.root,
                       repo_name=repo_name,
                       version=versions.get(repo_name) or
                       repo_config[repo_name]["version"][0],
                       install_path=self.install_path,
                       need_build=True)
            self.target_list.append(t)

    def update(self, update_deps, proxies):
        if update_deps:
            need_update_targets = self.target_list
        else:
            need_update_targets = self.target_list[-1:]

        if proxies:
            self.logger.info("use proxy: %s", str(proxies))
        self.downloader.downloads(need_update_targets, proxies=proxies)

    def build(self, build_deps):
        search_paths = [t.install_path for t in self.target_list]
        search_paths.append(os.path.join(self.root, "install"))
        search_paths = set(search_paths)
        if build_deps:
            need_build_targets = self.target_list
        else:
            need_build_targets = self.target_list[-1:]

        self.logger.info("start to build \n\t%s",
                         str([t.repo_name for t in need_build_targets]))

        for t in need_build_targets:
            ret = self.builder.build(t, search_paths)
            if ret != 0:
                self.logger.critical("build error with %d", ret)
