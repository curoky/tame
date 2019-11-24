#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

import logging
import os


class Package(object):

    def __init__(self, root, repo_name, version):

        self.repo_name = repo_name
        self.version = version
        self.dirname = "%s_%s" % (self.repo_name, self.version)
        self.download_path = os.path.join(root, "build", self.dirname)
        self.install_path = os.path.join(root, "install", self.dirname)
        self.build_path = None

        # if not os.path.exists(self.install_path):
        #     os.makedirs(self.install_path)

    def __str__(self):
        return self.dirname

    __repr__ = __str__
