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


class Yarpl(Target):
    def __init__(self, root, version="master", install_root=None):
        super(Yarpl, self).__init__(
            root,
            "yarpl",
            version,  # ff6466ab59406a6f6233e46485d29d6e4584ea21
            install_root,
            website="http://rsocket.io/",
            git_uri="git@github.com:rsocket/rsocket-cpp.git",
            deps=[boost, folly, glog, gflags,
                  double_conversion, gtest]
        )

    # def get_build_cmd(self):
    #     deps = self.deps()
    #     # return """ git checkout d05f962 && cd yarpl \
    #     # return """ mkdir -p build && cd build \
    #     return """ cd yarpl \
    #         && cmake .. -DCMAKE_INSTALL_PREFIX=%s \
    #         -Dfolly_DIR=%s\
    #         -DFOLLY_INCLUDE_DIR=%s\
    #         -DFOLLY_LIBRARY=%s\
    #         -DFOLLY_BENCHMARK_LIBRARY=%s\
    #         -DGLOG_INCLUDE_DIR=%s\
    #         -DGLOG_LIBRARY=%s\
    #         -DGFLAGS_INCLUDE_DIR=%s \
    #         -DGFLAGS_LIBRARY=%s \
    #         -DBOOST_INCLUDE_DIR=%s \
    #         -DBOOST_LIBRARY=%s \
    #         -DBUILD_TESTS=OFF\
    #         -DBUILD_BENCHMARKS=OFF\
    #         && make
    #         """ % (self.install_root,
    #                deps[0].install_lib + "/cmake/folly",
    #                deps[0].install_inc, deps[0].install_lib, deps[0].install_lib,
    #                deps[1].install_inc, deps[1].install_lib + "/libglog.a",
    #                deps[2].install_inc, deps[2].install_lib + "/libgflags.a",
    #                deps[3].install_inc, deps[3].install_lib,
    #                )
    def get_build_cmd(self):
        root = [dep.install_root for dep in self.deps]
        return "rm -rf ttt && mkdir ttt && cd ttt && " + \
               self.cmake_cmd(' .. '
                              ' -DBUILD_TESTS=OFF'
                              ' -DBUILD_EXAMPLES=OFF'
                              ' -DBUILD_BENCHMARKS=OFF'
                              ' -DCMAKE_PREFIX_PATH="%s"', ";".join(root))
