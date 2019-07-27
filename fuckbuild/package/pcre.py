#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import Target


class pcre(Target):
    def __init__(self, root, version="8.35", install_root=None):
        archive_uri = "https://ftp.pcre.org/pub/pcre/pcre-%s.tar.gz" % version
        super(pcre, self).__init__(
            root,
            "pcre",
            version,
            install_root,
            website="https://pcre.org/",
            archive_uri=archive_uri)

    def get_build_cmd(self):
        return self.configure_cmd()
