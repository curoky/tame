#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class Gcc(Target):

    def __init__(self, prefix_path):
        super(Gcc, self).__init__(prefix_path,
                                  name="gcc",
                                  version="7.4.0",
                                  website="https://gcc.gnu.org",
                                  archive_uri="https://bigsearcher.com/mirrors/gcc/releases/gcc-%s/gcc-%s.tar.xz")
        self.download_uri = self.archive_uri % (self.version, self.version)
        self.extract_dir_name = "gcc-%s" % self.version

    def get_build_cmd(self):
        # LD_LIBRARY_PATH
        return self.configure_cmd("--with-gmp=%s --with-mpfr=%s --with-mpc=%s "
                                  "--disable-multilib --enable-checking=release "
                                  "--enable-languages=c,c++ --with-system-zlib ")
