#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class Pythonlib(Target):

    def __init__(self, prefix_path):
        super(Pythonlib, self).__init__(prefix_path,
                                        name="pythonlib",
                                        version="3.6.3",
                                        archive_uri="https://www.python.org/ftp/python/%s/Python-%s.tgz")
        self.download_uri = self.archive_uri % (self.version, self.version)
        self.extract_dir_name = "Python-%s" % self.version

    def install_path(self):
        return "/data01/home/liqiming.icecory/.local"

    def get_build_cmd(self):
        return self.configure_cmd("--enable-optimizations")
