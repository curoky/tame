#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class c_ares(Target):

    def __init__(self, root, version="cares-1_15_0", install_root=None):
        super(c_ares, self).__init__(
            root, "c_ares", version, install_root,
            website="https://c-ares.haxx.se/",
            git_uri="git@github.com:c-ares/c-ares.git")

    def get_build_cmd(self):
        return self.cmake_cmd()
