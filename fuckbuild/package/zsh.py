#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target
from .ncurses import ncurses


class zsh(Target):
    """
    1. error
        checking if tcsetpgrp() actually works... error
        solution: add --with-tcsetpgrp for configure
    """

    def __init__(self, root, version="zsh-5.7.1", install_root=None):
        super(zsh, self).__init__(
            root,
            "zsh",
            version,
            install_root,
            website="http://www.zsh.org",
            git_uri="git@github.com:zsh-users/zsh.git",
            deps=[ncurses])

    def get_build_cmd(self):
        """
        ./configure --prefix=$HOME CPPFLAGS="-I$HOME/include/ncurses" LDFLAGS="-L$HOME/lib"
        :return:
        """
        CPPFLAGS = "-I" + self.deps[0].install_inc + "/ncurses"
        LDFLAGS = "-L" + self.deps[0].install_lib
        pre = "./Util/preconfig && export C_INCLUDE_PATH=%s && " % (self.deps[0].install_inc)
        return pre + './configure --prefix=%s --datadir=%s --with-tcsetpgrp CPPFLAGS="%s" LDFLAGS="%s"' % (
            self.install_root, self.install_root + "/doc", CPPFLAGS, LDFLAGS
        ) + " && " + self.make_cmd()
