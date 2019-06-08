#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class Tree(Target):

    def __init__(self, prefix_path):
        super(Tree, self).__init__(prefix_path,
                                   name="tree",
                                   version="1.8.0",
                                   archive_uri="http://mama.indstate.edu/users/ice/tree/src/tree-%s.tgz")
        self.download_uri = self.archive_uri % self.version
        self.extract_dir_name = "tree-%s" % self.version

    def get_build_cmd(self):
        return "make"
