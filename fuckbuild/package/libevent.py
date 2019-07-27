#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class libevent(Target):

    def __init__(self, root, version="release-2.1.8-stable", install_root=None):
        super(libevent, self).__init__(
            root, "libevent", version, install_root,
            website="http://libevent.org",
            git_uri="git@github.com:libevent/libevent.git")

    def get_build_cmd(self):
        return "./autogen.sh && " + self.configure_cmd()
