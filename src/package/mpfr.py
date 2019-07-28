#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target
from .gmp import gmp


class mpfr(Target):

    def __init__(self, root, version="4.0.2", install_root=None):
        archive_uri = "https://www.mpfr.org/mpfr-current/mpfr-%s.tar.gz" % version
        super(mpfr, self).__init__(
            root,
            "mpfr",
            version,
            install_root,
            website="https://www.mpfr.org/",
            archive_uri=archive_uri,
            deps=[gmp]
        )

    def get_build_cmd(self):
        return self.configure_cmd("--with-gmp=%s", self.deps[0].install_root)
