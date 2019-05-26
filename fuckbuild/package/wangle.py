#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target
from .folly import Folly
from .boost import Boost
from .glog import Glog
from .gflags import Gflags
from .openssl import Openssl
from .libevent import Libevent
from .double_conversion import DoubleConversion
from .gtest import Gtest


class Wangle(Target):

    def __init__(self, prefix_path):
        super(Wangle, self).__init__(prefix_path,
                                     name="wangle",
                                     version="v2018.08.20.00",
                                     website="",
                                     git_uri="git@github.com:facebook/wangle")

        self.deps = [
            Folly(self.prefix_path),
            Boost(self.prefix_path),
            Glog(self.prefix_path),
            Gflags(self.prefix_path),
            Openssl(self.prefix_path),
            Libevent(self.prefix_path),
            DoubleConversion(self.prefix_path),
            Gtest(self.prefix_path)]

    def get_build_cmd(self):
        prefix_path = [dep.install_path() for dep in self.deps]
        return "cd wangle && " + self.cmake_cmd('-DCMAKE_PREFIX_PATH="%s"', ";".join(prefix_path))
