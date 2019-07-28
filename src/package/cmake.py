#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class cmake(Target):

    def __init__(self, root, version="v3.13.4", install_root=None):
        super(cmake, self).__init__(
            root, "cmake", version, install_root,
            website="https://cmake.org/",
            git_uri="git@github.com:Kitware/CMake.git")

    def get_build_cmd(self):
        return "./bootstrap --prefix=%s && " % self.install_root + \
               self.make_cmd()
