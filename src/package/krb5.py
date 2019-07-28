#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target
from .bison import bison


class krb5(Target):
    """
    need bison 3.3.1
    """

    def __init__(self, root, version="krb5-1.16.1-final", install_root=None):
        super(krb5, self).__init__(
            root, "krb5", version, install_root,
            git_uri="git@github.com:krb5/krb5.git",
            deps=[bison])

    def get_build_cmd(self):
        return "cd src && autoreconf -ivf && " + self.configure_cmd()
