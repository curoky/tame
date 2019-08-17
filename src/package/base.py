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
    if name in simple_repos:
        raise
    simple_repos[name] = dict(
        name=name,
        url=url % tuple([version] * url.count("%s")),
        version=version,
        build_config=build_config,
        website=website,
        deps=deps
    )


register("autoconf", "2.69", "http://ftp.gnu.org/gnu/autoconf/autoconf-%s.tar.gz",
         configure())

register("automake", "1.16.1", "http://ftp.gnu.org/gnu/automake/automake-%s.tar.gz",
         configure(), deps=["autoconf"])

register("bison", "3.1", "http://ftp.gnu.org/gnu/bison/bison-%s.tar.gz",
         configure(),
         website="https://www.gnu.org/software/bison/")

register("gettext", "0.19.8", "http://ftp.gnu.org/gnu/gettext/gettext-%s.tar.gz",
         configure(),
         website="https://www.gnu.org/software/gettext/")

register("gmp", "6.1.2", "http://ftp.gnu.org/gnu/gmp/gmp-%s.tar.xz",
         configure(),
         website="https://gmplib.org/")

register("mpfr", "4.0.2", "http://ftp.gnu.org/gnu/mpfr/mpfr-%s.tar.gz",
         configure(), website="https://www.mpfr.org/", deps=["gmp"])

register("mpc", "1.1.0", "http://ftp.gnu.org/gnu/mpc/mpc-%s.tar.gz",
         configure(), deps=["gmp", "mpfr"])

register("gcc", "5.5.0", "http://ftp.gnu.org/gnu/gcc/gcc-%s/gcc-%s.tar.xz",
         configure(mat=" --disable-multilib --enable-checking=release"
                       " --enable-languages=c,c++ --with-system-zlib"),
         website="https://gcc.gnu.org",
         deps=["gmp", "mpfr", "mpc", "zlib"])

register("help2man", "1.47.9", "http://ftp.gnu.org/gnu/help2man/help2man-%s.tar.xz",
         configure())

register("ncurses", "6.1", "http://ftp.gnu.org/gnu/ncurses/ncurses-%s.tar.gz",
         configure(mat=" --with-ticlib --with-shared --disable-tic-depends"
                       " --with-pkg-config  --enable-pc-files"),
         website="https://www.gnu.org/software/ncurses/")

register("libtool", "2.4.6", "http://ftp.gnu.org/gnu/libtool/libtool-%s.tar.gz",
         configure(),
         website="https://www.gnu.org/software/libtool/")

# with bug https://www.reddit.com/r/archlinux/comments/97gsb1/glibc_update_breaks_buildroot/
register("m4", "1.4.18", "http://ftp.gnu.org/gnu/m4/m4-%s.tar.gz",
         configure())

register("pcre", "8.43", "http://ftp.pcre.org/pub/pcre/pcre-%s.tar.gz",
         configure(),
         "https://pcre.org/")

register("pkg-config", "0.29.2", "https://pkg-config.freedesktop.org/releases/pkg-config-%s.tar.gz",
         configure(mat="--with-internal-glib"))

register("curl", "7.64.0", "http://curl.haxx.se/download/curl-%s.tar.gz",
         configure(),
         website="https://curl.haxx.se/")

register("libev", "4.25", "http://dist.schmorp.de/libev/libev-%s.tar.gz",
         configure(),
         website="http://software.schmorp.de/pkg/libev.html")

register("libevent", "2.1.8-stable",
         "https://github.com/libevent/libevent/releases/download/release-%s/libevent-%s.tar.gz",
         configure(),
         website="http://libevent.org")

register("libsodium", "1.0.16",
         "https://github.com/jedisct1/libsodium/releases/download/%s/libsodium-%s.tar.gz",
         configure(),
         website="https://libsodium.org")

register("lzma", "5.2.3", "https://tukaani.org/xz/xz-%s.tar.gz",
         configure())

register("protobuf", "3.7.1",
         "https://github.com/protocolbuffers/protobuf/releases/download/v%s/protobuf-all-%s.tar.gz",
         configure(),
         website="https://developers.google.com/protocol-buffers/")

register("zlib", "v1.2.11", "git@github.com:madler/zlib.git",
         configure(),
         website="http://zlib.net/")

register("python", "3.6.3", "https://www.python.org/ftp/python/%s/Python-%s.tgz",
         configure(mat="--enable-optimizations"))

register("tmux", "2.8", "https://github.com/tmux/tmux/releases/download/2.8/tmux-2.8.tar.gz",
         configure(), deps=["ncurses", "pkg-config", "libevent"])

"""
must download github release not source
"""
register("flex", "2.6.4",
         "https://github.com/westes/flex/releases/download/v%s/flex-%s.tar.gz",
         configure(autogen=True),
         website="https://www.gnu.org/software/flex/",
         deps=["gettext", "automake", "bison", "libtool"])

register("mosh", "1.3.2",
         "https://github.com/mobile-shell/mosh/releases/download/mosh-%s/mosh-%s.tar.gz",
         configure(mat="CPPFLAGS=-std=c++11"),
         website="https://mosh.org", deps=["ncurses", "protobuf", "zlib"])

register("cmake", "v3.13.4", "git@github.com:Kitware/CMake.git",
         configure(),
         website="https://cmake.org/")

# 3.2.5 编译不过
register("shadowsocks-libev", "3.2.4",
         "https://github.com/shadowsocks/shadowsocks-libev/releases/download/v%s/shadowsocks-libev-%s.tar.gz",
         configure(mat="--disable-documentation"),
         deps=["pcre", "mbedtls", "libsodium", "c_ares", "libev"])

register("git", "2.19.2", "https://mirrors.edge.kernel.org/pub/software/scm/git/git-%s.tar.gz",
         configure(), website="https://git-scm.com/", deps=["zlib", "curl"])

# build with cmake
register("zstd", "v1.3.5", "git@github.com:facebook/zstd.git",
         cmake(src="build/cmake"))

register("gflags", "v2.2.2", "git@github.com:gflags/gflags.git",
         cmake(mat="-DBUILD_SHARED_LIBS=ON"),
         website="https://gflags.github.io/gflags/")

register("glog", "v0.4.0", "git@github.com:google/glog",
         cmake(), deps=["gflags"])

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
               "double-conversion", "libevent"])

register("wangle", "v2019.03.04.00", "git@github.com:facebook/wangle",
         cmake(src="wangle", ),
         deps=["folly", "boost", "glog", "gflags", "openssl",
               "libevent", "double-conversion", "gtest"]
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
         deps=["boost", "folly", "glog", "gflags", "double-conversion", "gtest"])
