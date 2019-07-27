#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class gflags(Target):

    def __init__(self, root, version="v2.1.2", install_root=None):
        super(gflags, self).__init__(
            root, "gflags", version, install_root,
            website="https://gflags.github.io/gflags/",
            git_uri="git@github.com:gflags/gflags.git")

    def get_build_cmd(self):
        #  -DBUILD_STATIC_LIBS=ON
        return self.cmake_cmd(" -DBUILD_SHARED_LIBS=ON")
