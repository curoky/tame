#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class vim(Target):
    """
    http://mirrors.ustc.edu.cn/vim/
    """

    def __init__(self, root, version):
        version = version or "v8.1.0996"
        super(vim, self).__init__(
            root, "vim", version,
            website="https://www.vim.org/",
            url="git@github.com:vim/vim.git",
            deps=["ncurses"])

    def get_build_cmd(self, install_path):
        return self.configure_cmd(install_path)
