#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class libev(Target):

    def __init__(self, root, version="4.25", install_root=None):
        archive_uri = "http://dist.schmorp.de/libev/libev-%s.tar.gz" % version
        super(libev, self).__init__(
            root, "libev", version, install_root,
            website="http://software.schmorp.de/pkg/libev.html",
            archive_uri=archive_uri
        )

    def get_build_cmd(self):
        return self.configure_cmd()
