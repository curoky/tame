#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class tree(Target):

    def __init__(self, root, version="1.8.0", install_root=None):
        archive_uri = "http://mama.indstate.edu/users/ice/tree/src/tree-%s.tgz" % version
        super(tree, self).__init__(
            root,
            "tree",
            version,
            install_root,
            archive_uri=archive_uri
        )

    def get_build_cmd(self):
        return "make"
