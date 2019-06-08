#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class Openssl(Target):
    """
    - OPENSSL_ROOT_DIR=$HOME
    - OPENSSL_INCLUDE_DIR=$HOME/include
    - OPENSSL_LIBRARIES=$HOME/lib
    """

    def __init__(self, prefix_path):
        super(Openssl, self).__init__(prefix_path,
                                      name="openssl",
                                      version="OpenSSL_1_1_1",
                                      website="https://www.openssl.org",
                                      git_uri="git@github.com:openssl/openssl.git")

    def get_build_cmd(self):
        return "./config --prefix=%s --openssldir=%s/ssl && " % (
            self.install_path(), self.install_path()) + self.make_cmd()
