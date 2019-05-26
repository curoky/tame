#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target
from .openssl import Openssl
from .boost import Boost
from .bison import Bison
from .flex import Flex
from .mstch import Mstch
from .folly import Folly
from .gflags import Gflags
from .glog import Glog
from .krb5 import Krb5
from .yarpl import Yarpl
from .wangle import Wangle
from .zlib import Zlib
from .zstd import Zstd
from .gtest import Gtest


class Fbthrift(Target):
    """
    2018.08.20.00
        - need bison 3.1 and flex 2.6.4
        - thrift/lib/cpp2/async/SemiStream-inl.h mf->f

    """

    def __init__(self, prefix_path):
        super(Fbthrift, self).__init__(prefix_path,
                                       name="fbthrift",
                                       version="v2018.08.20.00",
                                       website="",
                                       git_uri="git@github.com:facebook/fbthrift")

        self.deps = [
            Openssl(self.prefix_path),
            Boost(self.prefix_path),
            Bison(self.prefix_path),
            Flex(self.prefix_path),
            Mstch(self.prefix_path),
            Folly(self.prefix_path),
            Glog(self.prefix_path),
            Krb5(self.prefix_path),
            Gflags(self.prefix_path),
            Wangle(self.prefix_path),
            Zlib(self.prefix_path),
            Zstd(self.prefix_path),
            Gtest(self.prefix_path)]

    def get_build_cmd(self):
        prefix_path = [dep.install_path() for dep in self.deps]
        return self.cmake_cmd('-DCMAKE_PREFIX_PATH="%s"', ";".join(prefix_path))
