#!/ usr / bin / env python
# - * - coding : utf - 8 - * -
# @Author : IceCory(icecory520 @gmail.com)
# @Copyright(C) : GPL 3.0
# @desc:

from . import Target
from .boost import Boost
from .lz4 import Lz4
from .snappy import Snappy
from .gflags import Gflags
from .lzma import Lzma
from .glog import Glog
from .zstd import Zstd
from .double_conversion import DoubleConversion
from .libevent import Libevent
from .openssl import Openssl


class Folly(Target):

    def __init__(self, prefix_path):
        super(Folly, self).__init__(prefix_path,
                                    name="folly",
                                    version="v2018.08.20.00",
                                    website="",
                                    git_uri="git@github.com:facebook/folly")

        self.deps = [
            Boost(self.prefix_path),
            Lz4(self.prefix_path),
            Snappy(self.prefix_path),
            Gflags(self.prefix_path),
            Lzma(self.prefix_path),
            Glog(self.prefix_path),
            Openssl(self.prefix_path),
            Zstd(self.prefix_path),
            DoubleConversion(self.prefix_path),
            Libevent(self.prefix_path)]

    def get_build_cmd(self):
        prefix_path = [dep.install_path() for dep in self.deps]
        return self.cmake_cmd('-DCMAKE_PREFIX_PATH="%s"', ";".join(prefix_path))
