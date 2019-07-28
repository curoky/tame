#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target
from .boost import boost
from .double_conversion import double_conversion
from .folly import folly
from .gflags import gflags
from .glog import glog
from .gtest import gtest
from .libevent import libevent
from .openssl import openssl


class wangle(Target):

    def __init__(self, root, version="v2019.03.04.00", install_root=None):
        super(wangle, self).__init__(
            root,
            "wangle",
            version,
            install_root,
            git_uri="git@github.com:facebook/wangle",
            deps=[folly, boost, glog, gflags, openssl,
                  libevent, double_conversion, gtest])

    def get_build_cmd(self):
        return self.cmake_cmd(' -S %s', self.get_repo_sub_path("wangle"))
