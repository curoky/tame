#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class Gettext(Target):

    def __init__(self, prefix_path):
        super(Gettext, self).__init__(prefix_path,
                                      name="gettext",
                                      version="0.19.8",
                                      website="https://www.gnu.org/software/gettext/",
                                      archive_uri="https://ftp.gnu.org/gnu/gettext/gettext-%s.tar.gz")
        self.download_uri = self.archive_uri % self.version
        self.extract_dir_name = "gettext-%s" % self.version

    def get_build_cmd(self):
        return self.configure_cmd()
