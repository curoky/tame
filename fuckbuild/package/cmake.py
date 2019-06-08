#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class Cmake(Target):

    def __init__(self, prefix_path):
        super(Cmake, self).__init__(prefix_path,
                                    name="cmake",
                                    version="v3.13.4",
                                    website="https://cmake.org/",
                                    git_uri="git@github.com:Kitware/CMake.git")

    # def install_path(self):
    #     return "/data01/home/liqiming.icecory/.local"

    def get_build_cmd(self):
        return "./bootstrap --prefix=%s && " % self.install_path() + \
               self.make_cmd()
