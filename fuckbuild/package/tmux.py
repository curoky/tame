#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target
from .ncurses import Ncurses
from .libevent import Libevent


class Tmux(Target):

    def __init__(self, prefix_path):
        super(Tmux, self).__init__(prefix_path,
                                   name="tmux",
                                   version="2.8",
                                   git_uri="git@github.com:tmux/tmux.git")
        self.deps = [Ncurses(self.prefix_path), Libevent(self.prefix_path)]

    # def install_path(self):
    #     return "/data01/home/liqiming.icecory/.local"

    def get_build_cmd(self):
        """
        seem not need libevent_lib in LDFLAGS
        :return:
        """
        CPPFLAGS = "-I%s -I%s -I%s" % (self.deps[0].get_include(),
                                       self.deps[0].get_include() + "/ncurses",
                                       self.deps[1].get_include())
        LDFLAGS = "-static -L%s -L%s -lncurses" % (self.deps[0].get_lib(),
                                                   self.deps[1].get_lib())
        return "./autogen.sh && " + \
               self.configure_cmd('CPPFLAGS="%s" LDFLAGS="%s"', CPPFLAGS, LDFLAGS)
