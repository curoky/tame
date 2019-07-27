#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class helpman(Target):

    def __init__(self, root, version="1.47.9", install_root=None):
        archive_uri = "http://mirrors.ustc.edu.cn/gnu/help2man/help2man-%s.tar.xz" % version
        super(helpman, self).__init__(
            root, "help2man", version, install_root,
            archive_uri=archive_uri)

    def get_build_cmd(self):
        return self.configure_cmd()
