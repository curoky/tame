#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class double_conversion(Target):

    def __init__(self, root, version="v3.0.0", install_root=None):
        super(double_conversion, self).__init__(
            root, "double-conversion", version, install_root,
            git_uri="git@github.com:google/double-conversion.git")

    def get_build_cmd(self):
        return self.cmake_cmd()
