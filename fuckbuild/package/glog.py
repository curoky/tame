#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target
from .gflags import gflags


class glog(Target):

    def __init__(self, root, version="v0.3.3", install_root=None):
        super(glog, self).__init__(
            root, "glog", version, install_root,
            git_uri="git@github.com:google/glog",
            deps=[gflags])

    def get_build_cmd(self):
        return self.configure_cmd("--with-gflags=%s", self.deps[0].install_root)
