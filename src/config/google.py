#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import register, cmake_helper

register(name="protobuf",
         website="https://developers.google.com/protocol-buffers/",
         url="https://github.com/protocolbuffers/protobuf/releases/"
         "download/v{{version}}/protobuf-all-{{version}}.tar.gz",
         builder=cmake_helper(src_path="cmake"))

register(name="glog",
         deps={'gflags'},
         url="git@github.com:google/glog",
         builder=cmake_helper("-DBUILD_SHARED_LIBS=OFF"))

register(name="snappy",
         deps={'gtest'},
         url="git@github.com:google/snappy.git",
         builder=cmake_helper("-DSNAPPY_BUILD_TESTS=OFF"))

register(name="double-conversion",
         url="git@github.com:google/double-conversion.git",
         builder=cmake_helper())

register(name="gtest",
         url="git@github.com:google/googletest.git",
         builder=cmake_helper())

register(name="gflags",
         website="https://gflags.github.io/gflags/",
         url="git@github.com:gflags/gflags.git",
         builder=cmake_helper("-DBUILD_SHARED_LIBS=OFF"))
