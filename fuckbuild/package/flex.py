#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target
from .bison import Bison
from .gettext import Gettext
from .automake import Automake


class Flex(Target):
    """
    need gettext [autopoint]

    need install v2.6.4 before master
    """
    def __init__(self, prefix_path):
        super(Flex, self).__init__(prefix_path,
                                   name="flex",
                                   version="v2.6.4",
                                   # version="master",
                                   website="https://www.gnu.org/software/flex/",
                                   git_uri="git@github.com:westes/flex.git")
        self.deps = [Gettext(self.prefix_path), Automake(self.prefix_path), Bison(self.prefix_path)]

    def get_build_cmd(self):
        env = "export PATH=%s:$PATH && " % ":".join([dep.get_bin() for dep in self.deps])
        return env + "./autogen.sh && " + self.configure_cmd()
