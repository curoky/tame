#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target
from .libevent import libevent
from .ncurses import ncurses


class tmux(Target):

    def __init__(self, root, version="2.8", install_root=None):
        super(tmux, self).__init__(
            root, "tmux", version, install_root,
            git_uri="git@github.com:tmux/tmux.git",
            deps=[ncurses, libevent])

    def get_build_cmd(self):
        """
        seem not need libevent_lib in LDFLAGS
        :return:
        """
        CPPFLAGS = "-I%s -I%s" % (self.deps[0].install_inc, self.deps[1].install_inc)
        LDFLAGS = "-static -L%s -L%s -lncurses" % (self.deps[0].install_lib,
                                                   self.deps[1].install_lib)
        return "./autogen.sh && " + \
               self.configure_cmd('CPPFLAGS="%s" LDFLAGS="%s"', CPPFLAGS, LDFLAGS)
