#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class Libsodium(Target):

    def __init__(self, prefix_path):
        super(Libsodium, self).__init__(prefix_path,
                                        name="libsodium",
                                        version="1.0.16",
                                        website="https://libsodium.org",
                                        git_uri="git@github.com:jedisct1/libsodium.git")

    def get_build_cmd(self):
        return "./autogen.sh && " + self.configure_cmd()
