#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class krb5(Target):
    """
    need bison 3.3.1
    """

    def __init__(self, root, version):
        version = version or "krb5-1.16.1-final"
        super(krb5, self).__init__(
            root, "krb5", version,
            url="git@github.com:krb5/krb5.git",
            deps=["bison", "automake"])

    def get_build_cmd(self, install_path):
        return "cd src && autoreconf -ivf && " + self.configure_cmd(install_path, src='src')
