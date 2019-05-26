#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class Gflags(Target):

    def __init__(self, prefix_path):
        super(Gflags, self).__init__(prefix_path,
                                     name="gflags",
                                     version="v2.1.2",
                                     website="https://gflags.github.io/gflags/",
                                     git_uri="git@github.com:gflags/gflags.git")

    def get_build_cmd(self):
        # return "cmake -DCMAKE_INSTALL_PREFIX=%s -DBUILD_STATIC_LIBS=ON &&" % (
        return "cmake -DCMAKE_INSTALL_PREFIX=%s -DBUILD_SHARED_LIBS=ON &&" % (
            self.install_path()) + self.make_cmd()
