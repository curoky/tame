#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class Zstd(Target):

    def __init__(self, prefix_path):
        super(Zstd, self).__init__(prefix_path,
                                   name="zstd",
                                   version="v1.3.5",
                                   git_uri="git@github.com:facebook/zstd.git")

    def get_build_cmd(self):
        return "cd build/cmake && " + self.cmake_cmd()
