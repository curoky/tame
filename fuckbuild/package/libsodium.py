#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class libsodium(Target):

    def __init__(self, root, version="1.0.16", install_root=None):
        super(libsodium, self).__init__(
            root, "libsodium", version, install_root,
            website="https://libsodium.org",
            git_uri="git@github.com:jedisct1/libsodium.git")

    def get_build_cmd(self):
        return "./autogen.sh && " + self.configure_cmd()
