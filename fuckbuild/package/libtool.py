#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class libtool(Target):

    def __init__(self, root, version="2.4.6", install_root=None):
        archive_uri = "http://mirrors.ustc.edu.cn/gnu/libtool/libtool-%s.tar.gz" % version
        super(libtool, self).__init__(
            root, "libtool", version, install_root,
            website="https://www.gnu.org/software/libtool/",
            archive_uri=archive_uri)

    def get_build_cmd(self):
        return self.configure_cmd()
