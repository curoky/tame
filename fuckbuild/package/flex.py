#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target
from .automake import automake
from .bison import bison
from .gettext import gettext


class flex(Target):
    """
    need gettext [autopoint]

    need install v2.6.4 before master
    """

    def __init__(self, root, version="v2.6.4", install_root=None):
        super(flex, self).__init__(
            root, "flex", version, install_root,
            website="https://www.gnu.org/software/flex/",
            git_uri="git@github.com:westes/flex.git",
            deps=[gettext, automake, bison])

    def get_build_cmd(self):
        return "./autogen.sh && " + self.configure_cmd()
