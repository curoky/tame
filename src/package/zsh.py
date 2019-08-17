#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class zsh(Target):
    """
    1. error
        checking if tcsetpgrp() actually works... error
        solution: add --with-tcsetpgrp for configure
    """

    def __init__(self, root, version):
        version = version or "5.7.1"
        super(zsh, self).__init__(
            root, "zsh", version,
            website="http://www.zsh.org",
            # url="http://www.zsh.org/pub/zsh-%s.tar.xz"
            url="https://jaist.dl.sourceforge.net/project/zsh/zsh/%s/zsh-%s.tar.xz",
            deps=["ncurses"])

    def get_build_cmd(self, install_path):
        return self.configure_cmd(install_path, mat='--with-term-lib="ncurses"')
