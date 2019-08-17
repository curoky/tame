#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


import os

from . import Target


class tree(Target):

    def __init__(self, root, version):
        version = version or "1.8.0"
        super(tree, self).__init__(
            root, "tree", version,
            url="http://mama.indstate.edu/users/ice/tree/src/tree-%s.tgz" % version
        )

    def get_build_cmd(self, install_path):
        return "make && cp tree %s" % os.path.join(install_path, "bin")
