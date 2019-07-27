#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class zlib(Target):

    def __init__(self, root, version="v1.2.11", install_root=None):
        super(zlib, self).__init__(
            root,
            "zlib",
            version,
            install_root,
            website="http://zlib.net/",
            git_uri="git@github.com:madler/zlib.git")

    def get_build_cmd(self):
        return self.configure_cmd()
