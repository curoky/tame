#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target
from .ncurses import Ncurses
from .libevent import Libevent


class Zsh(Target):
    """
    1. error
        checking if tcsetpgrp() actually works... error
        solution: add --with-tcsetpgrp for configure
    """

    def __init__(self, prefix_path):
        super(Zsh, self).__init__(prefix_path,
                                  name="zsh",
                                  version="zsh-5.7.1",
                                  website="http://www.zsh.org",
                                  git_uri="git@github.com:zsh-users/zsh.git")

        self.deps = [Ncurses(self.prefix_path)]

    # def install_path(self):
    #     return "/data01/home/liqiming.icecory/.local"

    def get_build_cmd(self):
        """
        ./configure --prefix=$HOME CPPFLAGS="-I$HOME/include/ncurses" LDFLAGS="-L$HOME/lib"
        :return:
        """
        CPPFLAGS = "-I" + self.deps[0].get_include() + "/ncurses"
        LDFLAGS = "-L" + self.deps[0].get_lib()
        pre = "./Util/preconfig && export C_INCLUDE_PATH=%s && " % (self.deps[0].get_include())
        return pre + './configure --prefix=%s --datadir=%s --with-tcsetpgrp CPPFLAGS="%s" LDFLAGS="%s"' % (
            self.install_path(), self.install_path() + "/doc", CPPFLAGS, LDFLAGS
        ) + " && " + self.make_cmd()
