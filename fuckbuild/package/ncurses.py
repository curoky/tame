#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

import os
from . import Target


class Ncurses(Target):

    def __init__(self, prefix_path):
        super(Ncurses, self).__init__(prefix_path,
                                      name="ncurses",
                                      version="6.1",
                                      website="https://www.gnu.org/software/ncurses/",
                                      archive_uri="https://invisible-mirror.net/archives/ncurses/ncurses-%s.tar.gz"
                                      )

        self.download_uri = self.archive_uri % self.version
        self.extract_dir_name = "ncurses-%s" % self.version

    # def install_path(self):
    #     return "/data01/home/liqiming.icecory/.local"

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
                                  " --with-pkg-config-libdir=%s/pkgconfig", self.get_lib())
