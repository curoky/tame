#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target
from .gmp import gmp
from .mpfr import mpfr


class mpc(Target):

    def __init__(self, root, version="1.1.0", install_root=None):
        archive_uri = "https://ftp.gnu.org/gnu/mpc/mpc-%s.tar.gz" % version
        super(mpc, self).__init__(
            root, "mpc", version, install_root,
            archive_uri=archive_uri,
            deps=[gmp, mpfr]
        )

    def get_build_cmd(self):
        return self.configure_cmd("--with-gmp=%s -with-mpfr=%s", self.deps[0].install_root,
                                  self.deps[1].install_root)
