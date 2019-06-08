#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target


class Protobuf(Target):
    def __init__(self, prefix_path):
        super(Protobuf, self).__init__(prefix_path,
                                       name="protobuf",
                                       version="v3.6.1",
                                       website="https://developers.google.com/protocol-buffers/",
                                       git_uri="git@github.com:protocolbuffers/protobuf.git")

    def get_build_cmd(self):
        return "./autogen.sh && " + self.configure_cmd()
