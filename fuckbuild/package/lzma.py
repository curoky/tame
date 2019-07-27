#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class lzma(Target):
    """
    wget https://tukaani.org/xz/xz-5.2.3.tar.gz && tar -zxvf xz-5.2.3.tar.gz
    """

    def __init__(self, root, version="5.2.3", install_root=None):
        archive_uri = "https://tukaani.org/xz/xz-%s.tar.gz" % version
        super(lzma, self).__init__(
            root, "lzma", version, install_root,
            archive_uri=archive_uri)

    def get_build_cmd(self):
        return self.configure_cmd()
