#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class gettext(Target):

    def __init__(self, root, version="0.19.8", install_root=None):
        archive_uri = "https://ftp.gnu.org/gnu/gettext/gettext-%s.tar.gz" % version
        super(gettext, self).__init__(
            root, "gettext", version, install_root,
            website="https://www.gnu.org/software/gettext/",
            archive_uri=archive_uri,
        )

    def get_build_cmd(self):
        return self.configure_cmd()
