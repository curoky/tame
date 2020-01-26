#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        : manage mirror file

import os
import json
import codecs
import logging

from . import Package
from .config import register_all
from .builder import Builder
from .depender import Depender
from .downloader import Downloader


class Chafer(object):
    """
    主要负责全局的资源管理
    """

    def __init__(self, root, build_thread_num, download_thread_num):
        if not os.path.exists(root):
            os.makedirs(root)

        self.root = root
        self.global_config = register_all()

        self.builder = Builder(root, self.global_config, build_thread_num)
        self.downloader = Downloader(root, self.global_config,
                                     download_thread_num)
        self.depender = Depender(self.global_config)

        self.install_path = os.path.join(root, "install")
        self.archive_path = self.downloader.archive_path

        self.package_list = []
        self.logger = logging.getLogger("main")

    def prepare(self, target_infos):
        self.logger.info("target_infos: %s", target_infos)
        for target in target_infos:
            name = target[0]
            version = target[1]
            if version is None:
                version = self.global_config[name]["version"][0]
            self.package_list.append(
                Package(root=self.root, repo_name=name, version=version))

    def prepare_deps(self, target_infos):
        if len(target_infos) != 1:
            self.logger.critical("auto deps only use for on package")
        deps_list = self.depender.get_deps_list(target_infos[0][0])[:-1]
        idx = 0
        for dep in deps_list:
            target_infos.insert(idx, [dep, None])
            idx += 1

    def download(self, update_deps, proxies):
        if proxies:
            self.logger.info("use proxy: %s", str(proxies))
        self.downloader.downloads(self.package_list, proxies=proxies)

    def build(self, build_deps, include_paths, gcc_path):
        include_paths = set(include_paths)
        self.logger.info("build: %s", self.package_list)
        self.builder.build(self.package_list, include_paths, gcc_path)

    def gen_env(self):
        paths = os.listdir(self.install_path)
        bin_path = [os.path.join(self.install_path, p, "bin") for p in paths]
        lib_path = [os.path.join(self.install_path, p, "lib") for p in paths]
        lib64_path = [
            os.path.join(self.install_path, p, "lib64") for p in paths
        ]

        bin_path = [p for p in bin_path if os.path.exists(p)]
        lib_path = [p for p in lib_path if os.path.exists(p)]
        lib64_path = [p for p in lib64_path if os.path.exists(p)]

        path_env = "export PATH=" + ":".join(bin_path) + ":$PATH"
        LD_env = "export LD_LIBRARY_PATH=" + ":".join(
            lib_path + lib64_path) + ":$LD_LIBRARY_PATH"
        with codecs.open(os.path.join(self.root, "env.sh"), "w", "utf8") as f:
            f.write(path_env + "\n\n")
            f.write(LD_env + "\n")

    def list(self):
        paths = os.listdir(self.install_path)
        print("Already build repos:")
        for p in paths:
            info = p.split("_")
            print("\t%s: %s" % (info[0], info[1]))

    def info(self, target_infos):
        for target in target_infos:
            config = self.global_config[target[0]]
            config.pop("name")
            config.pop("build")
            print(json.dumps(config,
                             sort_keys=True,
                             indent=4,
                             separators=(',', ':')))
