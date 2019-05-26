#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class Mstch(Target):

    def __init__(self, prefix_path):
        super(Mstch, self).__init__(prefix_path,
                                    name="mstch",
                                    version="1.0.2",
                                    website="http://mustache.github.io/",
                                    git_uri="git@github.com:no1msd/mstch.git")

    def get_build_cmd(self):
        return self.cmake_cmd()
