#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class Zlib(Target):

    def __init__(self, prefix_path):
        super(Zlib, self).__init__(prefix_path,
                                   name="zlib",
                                   version="v1.2.11",
                                   website="http://zlib.net/",
                                   git_uri="git@github.com:madler/zlib.git")

    def get_build_cmd(self):
        return self.configure_cmd()
