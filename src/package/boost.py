#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class boost(Target):

    def __init__(self, root, version):
        version = version or "1.70.0"
        archive_url = "https://dl.bintray.com/boostorg/release/%s/source/boost_%s.tar.gz" % (
            version, version.replace(".", "_"))
        super(boost, self).__init__(
            root, "boost", version,
            website="https://www.boost.org/",
            url=archive_url)

    def get_build_cmd(self, install_path):
        return "./bootstrap.sh --prefix=%s" \
               " && ./b2 install --prefix=%s -j %d" % (install_path, install_path, self.thread_num)
