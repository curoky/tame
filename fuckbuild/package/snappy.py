#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class snappy(Target):
    def __init__(self, root, version="1.1.7", install_root=None):
        super(snappy, self).__init__(
            root,
            "snappy",
            version,
            install_root,
            git_uri="git@github.com:google/snappy.git")

    def get_build_cmd(self):
        return self.cmake_cmd()
