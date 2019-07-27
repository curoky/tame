#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class gtest(Target):

    def __init__(self, root, version="release-1.8.1", install_root=None):
        super(gtest, self).__init__(
            root, "gtest", version, install_root,
            git_uri="git@github.com:google/googletest.git")

    def get_build_cmd(self):
        return self.cmake_cmd()
