#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import register, cmake_helper, configure_helper, builder_helper, make_cmd

register(name="flex", website="https://www.gnu.org/software/flex/",
         deps={'bison', 'libtool', 'gettext', 'automake'},
         url="https://github.com/westes/flex/releases/download/v{{version}}/flex-{{version}}.tar.gz",
         builder=configure_helper())

register(name="libsodium", website="https://libsodium.org",
         url="https://github.com/jedisct1/libsodium/releases/download/{{version}}/libsodium-{{version}}.tar.gz",
         builder=configure_helper())

register(name="libevent", website="http://libevent.org",
         url="https://github.com/libevent/libevent/releases/download/release-{{version}}/libevent-{{version}}.tar.gz",
         builder=configure_helper())

register(name="pcre", website="https://pcre.org/",
         url="http://ftp.pcre.org/pub/pcre/pcre-{{version}}.tar.gz",
         builder=configure_helper())

register(name="pkg-config", url="https://pkg-config.freedesktop.org/releases/pkg-config-{{version}}.tar.gz",
         builder=configure_helper(args='--with-internal-glib'))

register(name="libev", website="http://software.schmorp.de/pkg/libev.html",
         url="http://dist.schmorp.de/libev/libev-{{version}}.tar.gz",
         builder=configure_helper())

register(name="lzma", url="https://tukaani.org/xz/xz-{{version}}.tar.gz",
         builder=configure_helper())

register(name="zlib", website="http://zlib.net/", url="git@github.com:madler/zlib.git",
         builder=configure_helper())

register(name="lz4", url="git@github.com:lz4/lz4.git",
         builder=cmake_helper(src_path="contrib/cmake_unofficial"))

register(name="mstch", deps={
         'boost'}, url="git@github.com:no1msd/mstch.git", builder=cmake_helper())
register(name="mbedtls", website="https://tls.mbed.org",     url="git@github.com:ARMmbed/mbedtls.git",
         builder=cmake_helper())

register(name="c_ares", website="https://c-ares.haxx.se/", url="git@github.com:c-ares/c-ares.git",
         builder=cmake_helper())

register(name="yarpl", website="http://rsocket.io/",
         deps={'double-conversion', 'folly',
               'glog', 'gtest', 'boost', 'gflags'},
         url="git@github.com:rsocket/rsocket-cpp.git",
         builder=cmake_helper(args='-DBUILD_TESTS=OFF -DBUILD_EXAMPLES= -DBUILD_BENCHMARKS=OFF'))

register(name="krb5", deps={'bison', 'automake'}, url="git@github.com:krb5/krb5.git",
         builder=builder_helper(
             type="custom",
             cmd='cd src && autoreconf -ivf && {{repo_path}}/src/configure --prefix={{install_path}} &&' + make_cmd(),
             build_path=".",
             src_path="."))

register(name="boost", website="https://www.boost.org/",
         url="https://dl.bintray.com/boostorg/release/{{version}}/source/boost_{{version|replace('.','_')}}.tar.gz",
         builder=builder_helper(
             type="custom",
             cmd='./bootstrap.sh --prefix={{install_path}} && ./b2 install --prefix={{install_path}} -j{{thread_num}}',
             build_path=".",
             src_path="."
         ))

register(name="openssl", website="https://www.openssl.org",
         url="https://www.openssl.org/source/openssl-{{version}}.tar.gz",
         builder=builder_helper(
             type='custom',
             cmd='{{repo_path}}/config --prefix={{install_path}} --openssldir={{install_path}}/ssl && ' + make_cmd(),
             build_path='.', src_path='.'))

register(name="tree", url="http://mama.indstate.edu/users/ice/tree/src/tree-{{version}}.tgz",
         builder=builder_helper(type="custom", cmd='make && cp {{repo_path}}/tree {{install_path}}/bin',
                                build_path='.',
                                src_path='.'))

register(name="bzip2", website="http://www.bzip.org/", url="https://nchc.dl.sourceforge.net/project/bzip2/bzip2-{{version}}.tar.gz",
         builder=builder_helper(type="custom", cmd="make && make install PREFIX={{install_path}}",
                                build_path='.', src_path='.'))

register(name="polipo", website="https://www.irif.fr/~jch/software/polipo/",
         url="https://github.com/jech/polipo/archive/polipo-{{version}}.tar.gz",
         builder=builder_helper(type="custom", cmd="make && cp {{repo_path}}/polipo {{install_path}}/bin",
                                build_path='.', src_path='.'))
register(name="rapidjson", website="http://rapidjson.org/",
         url="git@github.com:Tencent/rapidjson.git",
         builder=cmake_helper(args="-DRAPIDJSON_BUILD_DOC=OFF"
                              " -DRAPIDJSON_BUILD_EXAMPLES=OFF"
                              " -DRAPIDJSON_BUILD_TESTS=OFF"))