#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

"http://ftp.gnu.org/gnu/automake/automake-1.16.1.tar.gz"

from . import Target


class Automake(Target):

    def __init__(self, prefix_path):
        super(Automake, self).__init__(prefix_path,
                                       name="automake",
                                       version="1.16.1",
                                       archive_uri="http://ftp.gnu.org/gnu/automake/automake-%s.tar.gz")
        self.download_uri = self.archive_uri % self.version
        self.extract_dir_name = "automake-%s" % self.version

    def get_build_cmd(self):
        return self.configure_cmd()
