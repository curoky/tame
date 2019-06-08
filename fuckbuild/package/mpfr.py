#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target
from .gmp import Gmp


class Mpfr(Target):

    def __init__(self, prefix_path):
        super(Mpfr, self).__init__(prefix_path,
                                   name="mpfr",
                                   version="4.0.2",
                                   website="https://www.mpfr.org/",
                                   archive_uri="https://www.mpfr.org/mpfr-current/mpfr-%s.tar.gz")
        self.download_uri = self.archive_uri % self.version
        self.extract_dir_name = "mpfr-%s" % self.version
        self.deps = [Gmp(self.prefix_path)]

    def get_build_cmd(self):
        return self.configure_cmd("--with-gmp=%s", self.deps[0].install_path())
