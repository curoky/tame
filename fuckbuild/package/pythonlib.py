#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class Pythonlib(Target):

    def __init__(self, root, version="3.6.3", install_root=None):
        archive_uri = "https://www.python.org/ftp/python/%s/Python-%s.tgz" % (
            version, version)
        super(Pythonlib, self).__init__(
            root,
            "pythonlib",
            version,
            install_root,
            archive_uri=archive_uri)

    def get_build_cmd(self):
        return self.configure_cmd("--enable-optimizations")
