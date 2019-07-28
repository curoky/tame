#!/ usr / bin / env python
# - * - coding : utf - 8 - * -
# @Author : IceCory(icecory520 @gmail.com)
# @Copyright(C) : GPL 3.0
# @desc:

from . import Target
from .boost import boost
from .double_conversion import double_conversion
from .gflags import gflags
from .glog import glog
from .libevent import libevent
from .lz4 import lz4
from .lzma import lzma
from .openssl import openssl
from .snappy import snappy
from .zstd import zstd


class folly(Target):

    def __init__(self, root, version="v2018.08.20.00", install_root=None):
        super(folly, self).__init__(
            root, "folly", version, install_root,
            git_uri="git@github.com:facebook/folly",
            deps=[boost, lz4, snappy, gflags, lzma, glog, openssl, zstd,
                  double_conversion, libevent]
        )

    def get_build_cmd(self):
        return self.cmake_cmd()
