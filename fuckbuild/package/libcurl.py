#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class libcurl(Target):
    """
    如果有其他依赖于curl的库, 则需要配置环境变量`CURLDIR=${your_path}
    """

    def __init__(self, root, version="7.64.0", install_root=None):
        archive_uri = "https://curl.haxx.se/download/curl-%s.tar.gz" % version
        super(libcurl, self).__init__(
            root, "libcurl", version, install_root,
            website="https://curl.haxx.se/",
            archive_uri=archive_uri)

    def get_build_cmd(self):
        return self.configure_cmd()
