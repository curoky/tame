#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target
from .bison import bison
from .boost import boost
from .flex import flex
from .folly import folly
from .gflags import gflags
from .glog import glog
from .gtest import gtest
from .krb5 import krb5
from .mstch import mstch
from .openssl import openssl
from .wangle import wangle
from .zlib import zlib
from .zstd import zstd


class fbthrift(Target):
    """
    2018.08.20.00
        - need bison 3.1 and flex 2.6.4
        - thrift/lib/cpp2/async/SemiStream-inl.h mf->f

    """

    def __init__(self, root, version="v2019.03.04.00", install_root=None):
        super(fbthrift, self).__init__(
            root, "fbthrift", version, install_root,
            git_uri="git@github.com:facebook/fbthrift",
            deps=[openssl, boost, bison, flex, mstch, folly, glog,
                  krb5, gflags, wangle, zlib, zstd, gtest]
        )

    def get_build_cmd(self):
        return self.cmake_cmd()
