#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class Snappy(Target):
    def __init__(self, prefix_path):
        super(Snappy, self).__init__(prefix_path,
                                     name="snappy",
                                     version="1.1.7",
                                     git_uri="git@github.com:google/snappy.git")

    def get_build_cmd(self):
        return self.cmake_cmd()
