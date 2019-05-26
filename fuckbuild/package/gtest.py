#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class Gtest(Target):

    def __init__(self, prefix_path):
        super(Gtest, self).__init__(prefix_path,
                                    name="gtest",
                                    version="release-1.8.1",
                                    git_uri="git@github.com:google/googletest.git")

    def get_build_cmd(self):
        return self.cmake_cmd()
