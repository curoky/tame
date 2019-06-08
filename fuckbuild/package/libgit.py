#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target
from .curl import Curl
from .gettext import Gettext


class Libgit(Target):
    """
    1. fatal: Unable to find remote helper for 'https'
        resolution: --with-curl=path_to_curl
    """

    def __init__(self, prefix_path):
        super(Libgit, self).__init__(prefix_path,
                                     name="git",
                                     version="2.19.2",
                                     website="https://git-scm.com/",
                                     archive_uri="https://mirrors.edge.kernel.org/pub/software/scm/git/git-%s.tar.gz")
        self.download_uri = self.archive_uri % self.version
        self.extract_dir_name = "git-%s" % self.version
        self.deps = [Curl(self.prefix_path), Gettext(self.prefix_path)]

    # def install_path(self):
    #     return "/data01/home/liqiming.icecory/.local"

    def get_build_cmd(self):
        env = "export PATH=%s:$PATH && " % self.deps[1].get_bin()
        return env + self.configure_cmd("--with-curl=%s", self.deps[0].install_path())
