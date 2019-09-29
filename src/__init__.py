#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

import logging
import os


class Target(object):
    """
    @name: repo name
    @version: repo build version
    """

    def __init__(self, root, repo_name, version, install_path, need_build):
        self.repo_name = repo_name
        self.version = version
        self.repo_path = "%s/%s_%s" % (root, repo_name, version)

        self.install_path = install_path or os.path.join(
            self.repo_path, "_install")

        self.need_build = need_build

    def __str__(self):
        return self.repo_name

    __repr__ = __str__
