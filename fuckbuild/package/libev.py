#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class Libev(Target):

    def __init__(self, prefix_path):
        super(Libev, self).__init__(prefix_path,
                                    name="libev",
                                    version="4.25",
                                    website="http://software.schmorp.de/pkg/libev.html",
                                    archive_uri="http://dist.schmorp.de/libev/libev-%s.tar.gz")

        self.download_uri = self.archive_uri % self.version
        self.extract_dir_name = "libev-%s" % self.version

    def get_build_cmd(self):
        return self.configure_cmd()
