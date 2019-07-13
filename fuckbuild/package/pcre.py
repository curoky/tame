#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class Pcre(Target):
    def __init__(self, prefix_path):
        super(Pcre, self).__init__(prefix_path,
                                   name="pcre",
                                   version="8.35",
                                   website="https://pcre.org/",
                                   archive_uri="https://ftp.pcre.org/pub/pcre/pcre-%s.tar.gz")
        self.download_uri = self.archive_uri % self.version
        self.extract_dir_name = "pcre-%s" % self.version

    def get_build_cmd(self):
        return self.configure_cmd()
