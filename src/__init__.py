#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

import logging
import os


class TargetInfo(object):
    def __init__(self, root, name, version, install_path, force_build):
        self.root = root
        self.name = name
        self.version = version
        self.repo_name = "%s_%s" % (name, version)
        self.install_path = install_path or os.path.join(root, self.repo_name, "_install")
        self.force_build = force_build

    def __str__(self):
        return self.repo_name

    __repr__ = __str__
