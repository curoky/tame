#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class bison(Target):

    def __init__(self, root, version="3.1", install_root=None):
        archive_uri = "http://ftp.gnu.org/gnu/bison/bison-%s.tar.gz" % version
        super(bison, self).__init__(
            root, "bison", version, install_root,
            website="https://www.gnu.org/software/bison/",
            archive_uri=archive_uri
        )

    def get_build_cmd(self):
        return self.configure_cmd()
