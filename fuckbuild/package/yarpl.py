#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target
from .folly import Folly
from .glog import Glog
from .gflags import Gflags
from .boost import Boost
from .double_conversion import DoubleConversion
from .gtest import Gtest


class Yarpl(Target):
    def __init__(self, prefix_path):
        super(Yarpl, self).__init__(prefix_path,
                                    name="yarpl",
                                    version="master",  # ff6466ab59406a6f6233e46485d29d6e4584ea21
                                    website="http://rsocket.io/",
                                    git_uri="git@github.com:rsocket/rsocket-cpp.git"
                                    )

        self.deps = [Boost(self.prefix_path),
                     Folly(self.prefix_path),
                     Glog(self.prefix_path),
                     Gflags(self.prefix_path),
                     DoubleConversion(self.prefix_path),
                     Gtest(self.prefix_path)]

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
    #         """ % (self.install_path(),
    #                deps[0].get_lib() + "/cmake/folly",
    #                deps[0].get_include(), deps[0].get_lib(), deps[0].get_lib(),
    #                deps[1].get_include(), deps[1].get_lib() + "/libglog.a",
    #                deps[2].get_include(), deps[2].get_lib() + "/libgflags.a",
    #                deps[3].get_include(), deps[3].get_lib(),
    #                )
    def get_build_cmd(self):
        prefix_path = [dep.install_path() for dep in self.deps]
        return "rm -rf ttt && mkdir ttt && cd ttt && " + \
               self.cmake_cmd(' .. '
                              ' -DBUILD_TESTS=OFF'
                              ' -DBUILD_EXAMPLES=OFF'
                              ' -DBUILD_BENCHMARKS=OFF'
                              ' -DCMAKE_PREFIX_PATH="%s"', ";".join(prefix_path))
