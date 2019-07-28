#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target
from .ncurses import ncurses


class vim(Target):
    """
    http://mirrors.ustc.edu.cn/vim/
    """
    def __init__(self, root, version="v8.1.0996", install_root=None):
        super(vim, self).__init__(
            root, "vim", version, install_root,
            website="https://www.vim.org/",
            # archive_uri="https://github.com/vim/vim/archive/%s.tar.gz" % version,
            git_uri="git@github.com:vim/vim.git",
            deps=[ncurses])

    def get_build_cmd(self):
        LDFLAGS = "-L%s" % self.deps[0].install_lib
        return self.configure_cmd('LDFLAGS="%s"', LDFLAGS)
