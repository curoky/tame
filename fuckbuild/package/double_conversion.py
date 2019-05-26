#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class DoubleConversion(Target):

    def __init__(self, prefix_path):
        super(DoubleConversion, self).__init__(prefix_path,
                                               name="double-conversion",
                                               version="v3.0.0",
                                               git_uri="git@github.com:google/double-conversion.git")

    def get_build_cmd(self):
        return self.cmake_cmd()
