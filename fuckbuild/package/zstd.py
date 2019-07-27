#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class zstd(Target):

    def __init__(self, root, version="v1.3.5", install_root=None):
        super(zstd, self).__init__(
            root,
            "zstd",
            version, install_root,
            git_uri="git@github.com:facebook/zstd.git")

    def get_build_cmd(self):
        return self.cmake_cmd(" -S build/cmake"
                              " -B %s" % self.repo_path)
