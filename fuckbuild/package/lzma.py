#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class Lzma(Target):
    """
    wget https://tukaani.org/xz/xz-5.2.3.tar.gz && tar -zxvf xz-5.2.3.tar.gz
    """

    def __init__(self, prefix_path):
        super(Lzma, self).__init__(prefix_path,
                                   name="lzma",
                                   version="5.2.3",
                                   website="",
                                   archive_uri="https://tukaani.org/xz/xz-%s.tar.gz")
        self.download_uri = self.archive_uri % self.version
        self.extract_dir_name = "xz-%s" % self.version

    def get_build_cmd(self):
        return self.configure_cmd()
