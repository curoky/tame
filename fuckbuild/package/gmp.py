#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class gmp(Target):

    def __init__(self, root, version="6.1.2", install_root=None):
        archive_uri = "https://ftp.gnu.org/gnu/gmp/gmp-%s.tar.xz" % version
        super(gmp, self).__init__(
            root, "gmp", version, install_root,
            website="https://gmplib.org/",
            archive_uri=archive_uri
        )

    def get_build_cmd(self):
        return self.configure_cmd() + " && make check"
