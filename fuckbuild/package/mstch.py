#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target
from .boost import boost


class mstch(Target):

    def __init__(self, root, version="1.0.2", install_root=None):
        super(mstch, self).__init__(
            root,
            "mstch",
            version,
            install_root,
            website="http://mustache.github.io/",
            git_uri="git@github.com:no1msd/mstch.git",
            deps=[boost])

    def get_build_cmd(self):
        return self.cmake_cmd()
