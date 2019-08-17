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

    def __init__(self, root, version):
        version = version or "1.1.1b"
        super(openssl, self).__init__(
            root, "openssl", version,
            website="https://www.openssl.org",
            url="https://www.openssl.org/source/openssl-%s.tar.gz" % version)

    def get_build_cmd(self, install_path):
        return "./config --prefix=%s --openssldir=%s/ssl" % (
            install_path, install_path) + " && " + self.make_cmd()
