#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class Libtool(Target):

    def __init__(self, prefix_path):
        super(Libtool, self).__init__(prefix_path,
                                      name="libtool",
                                      version="2.4.6",
                                      website="https://www.gnu.org/software/libtool/",
                                      archive_uri="http://ftpmirror.gnu.org/libtool/libtool-%s.tar.gz")
        self.download_uri = self.archive_uri % self.version
        self.extract_dir_name = "libtool-%s" % self.version

    def get_build_cmd(self):
        return self.configure_cmd()
