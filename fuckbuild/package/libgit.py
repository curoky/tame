#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target
from .gettext import gettext
from .libcurl import libcurl


class libgit(Target):
    """
    1. fatal: Unable to find remote helper for 'https'
        resolution: --with-libcurl=path_to_curl
    """

    def __init__(self, root, version="2.19.2", install_root=None):
        archive_uri = "https://mirrors.edge.kernel.org/pub/software/scm/git/git-%s.tar.gz" % version
        super(libgit, self).__init__(
            root, "git", version, install_root,
            website="https://git-scm.com/",
            archive_uri=archive_uri,
            deps=[libcurl, gettext])

    def get_build_cmd(self):
        env = "export PATH=%s:$PATH && " % self.deps[1].install_bin
        return env + self.configure_cmd("--with-libcurl=%s", self.deps[0].install_root)
