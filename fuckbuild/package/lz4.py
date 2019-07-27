#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class lz4(Target):

    def __init__(self, root, version="v1.8.2", install_root=None):
        super(lz4, self).__init__(
            root,
            "lz4",
            version,
            install_root,
            git_uri="git@github.com:lz4/lz4.git")

    def get_build_cmd(self):
        return "cd contrib/cmake_unofficial && " + self.cmake_cmd()
