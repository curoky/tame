#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class Libevent(Target):

    def __init__(self, prefix_path):
        super(Libevent, self).__init__(prefix_path,
                                       name="libevent",
                                       version="release-2.1.8-stable",
                                       website="http://libevent.org",
                                       git_uri="git@github.com:libevent/libevent.git")

    def get_build_cmd(self):
        return "./autogen.sh && " + self.configure_cmd()
