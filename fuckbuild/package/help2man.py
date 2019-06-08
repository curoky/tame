#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class Help2man(Target):

    def __init__(self, prefix_path):
        super(Help2man, self).__init__(prefix_path,
                                       name="help2man",
                                       version="1.47.9",
                                       archive_uri="http://mirrors.ustc.edu.cn/gnu/help2man/help2man-%s.tar.xz")
        self.download_uri = self.archive_uri % self.version
        self.extract_dir_name = "help2man-%s" % self.version

    def get_build_cmd(self):
        return self.configure_cmd()
