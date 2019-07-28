#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class automake(Target):

    def __init__(self, root, version="1.16.1", install_root=None):
        archive_uri = "http://ftp.gnu.org/gnu/automake/automake-%s.tar.gz" % version
        super(automake, self).__init__(
            root, "automake", version, install_root, archive_uri=archive_uri
        )

    def get_build_cmd(self):
        return self.configure_cmd()
