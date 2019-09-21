#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import register, cmake_helper

register(name="zstd", url="git@github.com:facebook/zstd.git",
         builder=cmake_helper(src_path="build/cmake"))

register(name="wangle",
         deps={'double-conversion', 'libevent', 'folly', 'fizz', 'openssl',
               'glog', 'gtest', 'boost', 'gflags'},
         url="git@github.com:facebook/wangle",
         builder=cmake_helper(src_path="wangle"))

register(name="fbthrift",
         deps={'wangle', 'zlib', 'flex', 'folly', 'fizz', 'bison', 'openssl',
               'glog', 'mstch', 'zstd', 'krb5', 'gtest',
               'boost', 'gflags'}, url="git@github.com:facebook/fbthrift",
         builder=cmake_helper())

register(name="fizz",
         deps={'zlib', 'libsodium', 'double-conversion', 'libevent', 'folly',
               'openssl', 'gflags'},
         url="git@github.com:facebookincubator/fizz.git",
         builder=cmake_helper(src_path="fizz",args="-DCMAKE_CROSSCOMPILING=OFF"))

register(name="folly",
         deps={'double-conversion', 'lz4', 'libevent', 'openssl', 'glog',
               'zstd', 'boost', 'gflags', 'snappy', 'lzma'},
         url="git@github.com:facebook/folly",
         builder=cmake_helper())
