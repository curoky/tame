#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import register, configure_helper

register(name="autoconf", url="http://ftp.gnu.org/gnu/autoconf/autoconf-{{version}}.tar.gz",
         builder=configure_helper())

register(name="automake", deps={'autoconf'}, url="http://ftp.gnu.org/gnu/automake/automake-{{version}}.tar.gz",
         builder=configure_helper())

register(name="bison", website="https://www.gnu.org/software/bison/",
         url="http://ftp.gnu.org/gnu/bison/bison-{{version}}.tar.gz",
         builder=configure_helper())

register(name="gettext", website="https://www.gnu.org/software/gettext/",
         url="http://ftp.gnu.org/gnu/gettext/gettext-{{version}}.tar.gz",
         builder=configure_helper())

register(name="gmp", website="https://gmplib.org/",
         url="http://ftp.gnu.org/gnu/gmp/gmp-{{version}}.tar.xz",
         builder=configure_helper())

register(name="mpfr", website="https://www.mpfr.org/", deps={'gmp'},
         url="http://ftp.gnu.org/gnu/mpfr/mpfr-{{version}}.tar.gz",
         builder=configure_helper())

register(name="mpc", deps={'mpfr', 'gmp'},
         url="http://ftp.gnu.org/gnu/mpc/mpc-{{version}}.tar.gz",
         builder=configure_helper())

register(name="gcc", website="https://gcc.gnu.org", deps={'zlib', 'mpfr', 'mpc', 'gmp'},
         url="http://ftp.gnu.org/gnu/gcc/gcc-{{version}}/gcc-{{version}}.tar.xz",
         builder=configure_helper(args='--disable-multilib --enable-checking=release'
                                       ' --enable-languages=c,c++ --with-system-zlib'))

register(name="help2man", url="http://ftp.gnu.org/gnu/help2man/help2man-{{version}}.tar.xz",
         builder=configure_helper())

register(name="ncurses", website="https://www.gnu.org/software/ncurses/",
         url="http://ftp.gnu.org/gnu/ncurses/ncurses-{{version}}.tar.gz",
         builder=configure_helper(
             "--with-ticlib --with-shared --disable-tic-depends --with-pkg-config  --enable-pc-files"))

register(name="libtool", website="https://www.gnu.org/software/libtool/",
         url="http://ftp.gnu.org/gnu/libtool/libtool-{{version}}.tar.gz",
         builder=configure_helper())

register(name="m4", url="http://ftp.gnu.org/gnu/m4/m4-{{version}}.tar.gz",
         builder=configure_helper())

register(name="texinfo", url="http://ftp.gnu.org/gnu/texinfo/texinfo-{{version}}.tar.gz",
         builder=configure_helper())
