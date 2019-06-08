#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class Boost(Target):
    """
    - export BOOST_ROOT=$HOME
    - export Boost_LIBRARY_DIRS=$HOME/lib
    - export BOOST_INCLUDEDIR=$HOME/include
    """

    def __init__(self, prefix_path):
        super(Boost, self).__init__(prefix_path=prefix_path,
                                    name="boost",
                                    version="1.67.0",
                                    website="",
                                    archive_uri="https://dl.bintray.com/boostorg/release/%s/source/boost_%s.tar.gz")
        self.download_uri = self.archive_uri % (self.version, self.version.replace(".", "_"))
        self.extract_dir_name = "boost_%s" % self.version.replace(".", "_")

    def get_build_cmd(self):
        return "./bootstrap.sh --prefix=%s" \
               " && ./b2 install --prefix=%s -j 20" % (self.install_path(), self.install_path())
