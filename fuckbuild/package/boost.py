#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class boost(Target):

    def __init__(self, root, version="1.67.0", install_root=None):
        archive_uri = "https://dl.bintray.com/boostorg/release/%s/source/boost_%s.tar.gz" % (
            version, version.replace(".", "_"))
        super(boost, self).__init__(
            root, "boost", version, install_root,
            website="https://www.boost.org/",
            archive_uri=archive_uri)

    def get_build_cmd(self):
        return "./bootstrap.sh --prefix=%s" \
               " && ./b2 install --prefix=%s -j 20" % (self.install_root, self.install_root)
