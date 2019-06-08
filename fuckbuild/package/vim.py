#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target
from .ncurses import Ncurses
from .gettext import Gettext


class Vim(Target):
    def __init__(self, prefix_path):
        super(Vim, self).__init__(prefix_path,
                                  name="vim",
                                  version="v8.1.0996",
                                  website="https://www.vim.org/",
                                  git_uri="git@github.com:vim/vim.git")
        self.deps = [Ncurses(self.prefix_path)]

    # def install_path(self):
    #     return "/data01/home/liqiming.icecory/.local"

    def get_build_cmd(self):
        LD_LIBRARY_PATH = self.deps[0].get_lib()
        LDFLAGS = "-L%s" % (self.deps[0].get_lib())
        return "export LD_LIBRARY_PATH=%s && " % LD_LIBRARY_PATH + \
               self.configure_cmd('LDFLAGS="%s"', LDFLAGS)
