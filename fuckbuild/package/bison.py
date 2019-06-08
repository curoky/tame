#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class Bison(Target):

    def __init__(self, prefix_path):
        super(Bison, self).__init__(prefix_path,
                                    name="bison",
                                    version="3.1",
                                    website="https://www.gnu.org/software/bison/",
                                    archive_uri="http://ftp.gnu.org/gnu/bison/bison-%s.tar.gz")
        self.download_uri = self.archive_uri % self.version
        self.extract_dir_name = "bison-%s" % self.version

    def get_build_cmd(self):
        return self.configure_cmd()
