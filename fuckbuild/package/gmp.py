#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class Gmp(Target):

    def __init__(self, prefix_path):
        super(Gmp, self).__init__(prefix_path,
                                  name="gmp",
                                  version="6.1.2",
                                  website="https://gmplib.org/",
                                  archive_uri="https://ftp.gnu.org/gnu/gmp/gmp-%s.tar.xz")
        self.download_uri = self.archive_uri % self.version
        self.extract_dir_name = "gmp-%s" % self.version

    def get_build_cmd(self):
        return self.configure_cmd() + " && make check"
