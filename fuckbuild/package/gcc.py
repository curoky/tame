#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target
from .gmp import gmp
from .mpc import mpc
from .mpfr import mpfr


class gcc(Target):

    def __init__(self, root, version="7.4.0", install_root=None):
        archive_uri = "https://bigsearcher.com/mirrors/gcc/releases/gcc-%s/gcc-%s.tar.xz" % (
            version, version)
        super(gcc, self).__init__(
            root, "gcc", version, install_root,
            website="https://gcc.gnu.org",
            archive_uri=archive_uri,
            deps=[gmp, mpfr, mpc])

    def get_build_cmd(self):
        return self.configure_cmd("--with-gmp=%s --with-mpfr=%s --with-mpc=%s "
                                  "--disable-multilib --enable-checking=release "
                                  "--enable-languages=c,c++ --with-system-zlib ",
                                  self.deps[0].install_root,
                                  self.deps[1].install_root,
                                  self.deps[2].install_root)
