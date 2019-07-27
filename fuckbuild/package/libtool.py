#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class Libtool(Target):

    def __init__(self, root, version="2.4.6", install_root=None):
        archive_uri = "http://ftpmirror.gnu.org/libtool/libtool-%s.tar.gz" % version
        super(Libtool, self).__init__(
            root, "libtool", version, install_root,
            website="https://www.gnu.org/software/libtool/",
            archive_uri=archive_uri)

    def get_build_cmd(self):
        return self.configure_cmd()
