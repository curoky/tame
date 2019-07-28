#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class ncurses(Target):

    def __init__(self, root, version="6.1", install_root=None):
        archive_uri = "https://invisible-mirror.net/archives/ncurses/ncurses-%s.tar.gz" % version
        super(ncurses, self).__init__(
            root, "ncurses", version, install_root,
            website="https://www.gnu.org/software/ncurses/",
            archive_uri=archive_uri
        )

    def get_build_cmd(self):
        return self.configure_cmd(" --with-shared"
                                  " --with-termlib"
                                  " --with-cxx"
                                  " --without-ada"
                                  " --enable-warnings"
                                  " --enable-assertions"
                                  " --disable-home-terminfo"
                                  " --enable-database"
                                  " --enable-sp-funcs"
                                  " --enable-interop"
                                  " --with-progs"
                                  " --enable-pc-files"
                                  " --with-pkg-config-libdir=%s/pkgconfig", self.install_lib)
