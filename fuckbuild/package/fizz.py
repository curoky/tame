#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target
from .openssl import openssl


class fizz(Target):

    def __init__(self, root, version="v2019.03.18.00", install_root=None):
        super(fizz, self).__init__(
            root, "fizz", version, install_root,
            website="",
            git_uri="git@github.com:facebookincubator/fizz.git",
            deps=[openssl]
        )

    def get_build_cmd(self):
        return self.cmake_cmd(" -S %s", self.get_repo_sub_path("fizz"))
