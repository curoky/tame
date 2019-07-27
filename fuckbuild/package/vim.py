#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target
from .ncurses import ncurses


class Vim(Target):
    def __init__(self, root, version="v8.1.0996", install_root=None):
        super(Vim, self).__init__(
            root,
            "vim",
            version,
            install_root,
            website="https://www.vim.org/",
            git_uri="git@github.com:vim/vim.git",
            deps=[ncurses])

    def get_build_cmd(self):
        LD_LIBRARY_PATH = self.deps[0].install_lib
        LDFLAGS = "-L%s" % self.deps[0].install_lib
        return "export LD_LIBRARY_PATH=%s && " % LD_LIBRARY_PATH + \
               self.configure_cmd('LDFLAGS="%s"', LDFLAGS)
