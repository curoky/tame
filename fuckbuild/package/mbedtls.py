#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class Mbedtls(Target):

    def __init__(self, prefix_path):
        super(Mbedtls, self).__init__(prefix_path,
                                      name="mbedtls",
                                      version="mbedtls-2.1.18",
                                      website="https://tls.mbed.org",
                                      git_uri="git@github.com:ARMmbed/mbedtls.git")

    def get_build_cmd(self):
        return self.cmake_cmd()
