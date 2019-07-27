#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class mbedtls(Target):

    def __init__(self, root, version="mbedtls-2.1.18", install_root=None):
        super(mbedtls, self).__init__(
            root, "mbedtls", version, install_root,
            website="https://tls.mbed.org",
            git_uri="git@github.com:ARMmbed/mbedtls.git")

    def get_build_cmd(self):
        return self.cmake_cmd()
