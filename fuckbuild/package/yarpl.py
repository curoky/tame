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


class yarpl(Target):
    def __init__(self, root, version="master", install_root=None):
        super(yarpl, self).__init__(
            root, "yarpl", version,  # ff6466ab59406a6f6233e46485d29d6e4584ea21
            install_root,
            website="http://rsocket.io/",
            git_uri="git@github.com:rsocket/rsocket-cpp.git",
            deps=[boost, folly, glog, gflags, double_conversion, gtest]
        )

    def get_build_cmd(self):
        return self.cmake_cmd(' -DBUILD_TESTS=OFF'
                              ' -DBUILD_EXAMPLES=OFF'
                              ' -DBUILD_BENCHMARKS=OFF')
