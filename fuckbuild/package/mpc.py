#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target
from .gmp import Gmp
from .mpfr import Mpfr


class Mpc(Target):

    def __init__(self, prefix_path):
        super(Mpc, self).__init__(prefix_path,
                                  name="mpc",
                                  version="1.1.0",
                                  archive_uri="https://ftp.gnu.org/gnu/mpc/mpc-%s.tar.gz")
        self.download_uri = self.archive_uri % self.version
        self.extract_dir_name = "mpc-%s" % self.version
        self.deps = [Gmp(self.prefix_path), Mpfr(self.prefix_path)]

    def get_build_cmd(self):
        return self.configure_cmd("--with-gmp=%s -with-mpfr=%s", self.deps[0].install_path(),
                                  self.deps[1].install_path())
