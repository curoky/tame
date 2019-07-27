#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class openssl(Target):
    """
    - OPENSSL_ROOT_DIR=$HOME
    - OPENSSL_INCLUDE_DIR=$HOME/include
    - OPENSSL_LIBRARIES=$HOME/lib
    """

    def __init__(self, root, version="OpenSSL_1_1_1", install_root=None):
        archive_uri = "https://github.com/openssl/openssl/archive/%s.tar.gz" % version
        super(openssl, self).__init__(
            root,
            "openssl",
            version,
            install_root,
            website="https://www.openssl.org",
            archive_uri=archive_uri,
            git_uri="git@github.com:openssl/openssl.git")

    def get_build_cmd(self):
        return "./config --prefix=%s --openssldir=%s/ssl && " % (
            self.install_root, self.install_root) + self.make_cmd()
