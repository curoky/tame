#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


simple_repos = {}


def configure(autogen=False, mat="", *args):
    return dict(type="configure", autogen=autogen, mat=mat, args=args)


def cmake(src=".", mat="", *args):
    return dict(type="cmake", src=src, mat=mat, args=args)


def register(name, version, url, build_config, website="", deps=None):
    simple_repos[name] = dict(
        name=name,
        url=url % tuple([version] * url.count("%s")),
        version=version,
        build_config=build_config,
        website=website,
        deps=deps
    )


register("automake", "1.16.1", "http://ftp.gnu.org/gnu/automake/automake-%s.tar.gz",
         configure())

register("bison", "3.1", "http://ftp.gnu.org/gnu/bison/bison-%s.tar.gz",
         configure(),
         website="https://www.gnu.org/software/bison/")

register("gettext", "0.19.8", "https://ftp.gnu.org/gnu/gettext/gettext-%s.tar.gz",
         configure(),
         website="https://www.gnu.org/software/gettext/")

register("gmp", "6.1.2", "https://ftp.gnu.org/gnu/gmp/gmp-%s.tar.xz",
         configure(),
         website="https://gmplib.org/")

register("help2man", "1.47.9", "https://ftp.gnu.org/gnu/help2man/help2man-%s.tar.xz",
         configure())


# with bug https://www.reddit.com/r/archlinux/comments/97gsb1/glibc_update_breaks_buildroot/
register("m4", "1.4.18", "https://ftp.gnu.org/gnu/m4/m4-%s.tar.gz",
         configure(), deps=["m4"])

register("curl", "7.64.0", "https://curl.haxx.se/download/curl-%s.tar.gz",
         configure(),
         website="https://curl.haxx.se/")

register("libev", "4.25", "http://dist.schmorp.de/libev/libev-%s.tar.gz",
         configure(),
         website="http://software.schmorp.de/pkg/libev.html")

register("libevent", "release-2.1.8-stable", "git@github.com:libevent/libevent.git",
         configure(autogen=True),
         website="http://libevent.org")

register("libsodium", "1.0.16", "git@github.com:jedisct1/libsodium.git",
         configure(autogen=True),
         website="https://libsodium.org")

register("libtool", "2.4.6", "http://mirrors.ustc.edu.cn/gnu/libtool/libtool-%s.tar.gz",
         configure(),
         website="https://www.gnu.org/software/libtool/")

register("lzma", "5.2.3", "https://tukaani.org/xz/xz-%s.tar.gz",
         configure())

register("pcre", "8.35", "https://ftp.pcre.org/pub/pcre/pcre-%s.tar.gz",
         configure(),
         "https://pcre.org/")

register("protobuf", "v3.6.1", "git@github.com:protocolbuffers/protobuf.git",
         configure(autogen=True),
         website="https://developers.google.com/protocol-buffers/")

register("zlib", "v1.2.11", "git@github.com:madler/zlib.git",
         configure(),
         website="http://zlib.net/")

register("python", "3.6.3", "https://www.python.org/ftp/python/%s/Python-%s.tgz",
         configure(mat="--enable-optimizations"))

"""
    need gettext [autopoint]

    need install v2.6.4 before master
"""
register("flex", "v2.6.4", "git@github.com:westes/flex.git",
         configure(autogen=True),
         website="https://www.gnu.org/software/flex/",
         deps=["gettext", "automake", "bison"])

register("mosh", "mosh-1.3.2", "git@github.com:mobile-shell/mosh.git",
         configure(autogen=True, mat="CPPFLAGS=-std=c++11"),
         website="https://mosh.org", deps=["ncurses", "protobuf"])

# cmake
register("zstd", "v1.3.5", "git@github.com:facebook/zstd.git",
         cmake(src="build/cmake"))

register("gflags", "v2.1.2", "git@github.com:gflags/gflags.git",
         cmake(mat="-DBUILD_SHARED_LIBS=ON"),
         website="https://gflags.github.io/gflags/")

register("lz4", "v1.8.2", "git@github.com:lz4/lz4.git",
         cmake(src="contrib/cmake_unofficial"))

register("snappy", "1.1.7", "git@github.com:google/snappy.git",
         cmake())

register("mstch", "1.0.2", "git@github.com:no1msd/mstch.git",
         cmake(), deps=["boost"])

register("mbedtls", "mbedtls-2.1.18", "git@github.com:ARMmbed/mbedtls.git",
         cmake(),
         website="https://tls.mbed.org")

register("c_ares", "cares-1_15_0", "git@github.com:c-ares/c-ares.git",
         cmake(),
         website="https://c-ares.haxx.se/")

register("double-conversion", "v3.0.0", "git@github.com:google/double-conversion.git",
         cmake())

register("gtest", "release-1.8.1", "git@github.com:google/googletest.git",
         cmake())

register("fizz", "v2019.03.18.00", "git@github.com:facebookincubator/fizz.git",
         cmake(src="fizz"), deps=["openssl"])

register("folly", "v2019.03.04.00", "git@github.com:facebook/folly",
         cmake(),
         deps=["boost", "lz4", "snappy", "gflags", "lzma", "glog", "openssl", "zstd",
               "double_conversion", "libevent"])

register("wangle", "v2019.03.04.00", "git@github.com:facebook/wangle",
         cmake(src="wangle", ),
         deps=["folly", "boost", "glog", "gflags", "openssl",
               "libevent", "double_conversion", "gtest"]
         )

"""
2018.08.20.00
    - need bison 3.1 and flex 2.6.4
    - thrift/lib/cpp2/async/SemiStream-inl.h mf->f

"""
register("fbthrift", "v2019.03.04.00", "git@github.com:facebook/fbthrift",
         cmake(),
         deps=["openssl", "boost", "bison", "flex", "mstch", "folly", "glog",
               "krb5", "gflags", "wangle", "zlib", "zstd", "gtest"])

# ff6466ab59406a6f6233e46485d29d6e4584ea21
register("yarpl", "master", "git@github.com:rsocket/rsocket-cpp.git",
         cmake(mat=' -DBUILD_TESTS=OFF -DBUILD_EXAMPLES= -DBUILD_BENCHMARKS=OFF'),
         website="http://rsocket.io/",
         deps=["boost", "folly", "glog", "gflags", "double_conversion", "gtest"])
