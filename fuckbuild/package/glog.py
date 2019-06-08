#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target
from .gflags import Gflags


class Glog(Target):

    def __init__(self, prefix_path):
        super(Glog, self).__init__(prefix_path,
                                   name="glog",
                                   version="v0.3.3",
                                   git_uri="git@github.com:google/glog")
        self.deps = [Gflags(self.prefix_path)]

    def get_build_cmd(self):
        return self.configure_cmd("--with-gflags=%s", self.deps[0].install_path())
