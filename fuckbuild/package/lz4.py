#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class Lz4(Target):

    def __init__(self, prefix_path):
        super(Lz4, self).__init__(prefix_path,
                                  name="lz4",
                                  version="v1.8.2",
                                  git_uri="git@github.com:lz4/lz4.git")

    def get_build_cmd(self):
        return "cd contrib/cmake_unofficial && " + self.cmake_cmd()
