#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class Curl(Target):
    """
    如果有其他依赖于curl的库, 则需要配置环境变量`CURLDIR=${your_path}
    """

    def __init__(self, prefix_path):
        super(Curl, self).__init__(prefix_path,
                                   name="curl",
                                   version="7.64.0",
                                   website="https://curl.haxx.se/",
                                   archive_uri="https://curl.haxx.se/download/curl-%s.tar.gz")
        self.download_uri = self.archive_uri % self.version
        self.extract_dir_name = "curl-%s" % self.version

    def get_build_cmd(self):
        return self.configure_cmd()
