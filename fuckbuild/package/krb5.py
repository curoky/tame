#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target
from .bison import Bison


class Krb5(Target):
    """
    need bison 3.3.1
    """
    def __init__(self, prefix_path):
        super(Krb5, self).__init__(prefix_path,
                                   name="krb5",
                                   version="krb5-1.16.1-final",
                                   git_uri="git@github.com:krb5/krb5.git")
        self.deps = [Bison(self.prefix_path)]

    def get_build_cmd(self):
        env = "export PATH=%s:$PATH && " % self.deps[0].get_bin()
        return env + "cd src && autoreconf -ivf && " + self.configure_cmd()
