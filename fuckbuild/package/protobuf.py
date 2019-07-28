#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class protobuf(Target):
    def __init__(self, root, version="v3.6.1", install_root=None):
        archive_uri = "https://github.com/protocolbuffers/protobuf/archive/.tar.gz" % version
        super(protobuf, self).__init__(
            root,
            "protobuf",
            version,
            install_root,
            website="https://developers.google.com/protocol-buffers/",
            archive_uri=archive_uri,
            git_uri="git@github.com:protocolbuffers/protobuf.git")

    def get_build_cmd(self):
        return "./autogen.sh && " + self.configure_cmd()
