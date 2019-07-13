#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class Cares(Target):

    def __init__(self, prefix_path):
        super(Cares, self).__init__(prefix_path,
                                    name="c_ares",
                                    version="cares-1_15_0",
                                    website="https://c-ares.haxx.se/",
                                    git_uri="git@github.com:c-ares/c-ares.git")

    def get_build_cmd(self):
        return self.cmake_cmd()
