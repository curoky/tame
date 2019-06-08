#!/ usr / bin / env python
# - * - coding : utf - 8 - * -
# @Author : IceCory(icecory520 @gmail.com)
# @Copyright(C) : GPL 3.0
# @desc:

from . import Target
from .ncurses import Ncurses
from .protobuf import Protobuf


class Mosh(Target):

    def __init__(self, prefix_path):
        super(Mosh, self).__init__(prefix_path,
                                   name="mosh",
                                   version="mosh-1.3.2",
                                   website="https://mosh.org",
                                   git_uri="git@github.com:mobile-shell/mosh.git")
        self.deps = [Ncurses(self.prefix_path), Protobuf(self.prefix_path)]

    def get_build_cmd(self):
        PKG_CONFIG_PATH = self.deps[1].get_lib() + "/pkgconfig" + ":" + self.deps[0].get_lib() + "/pkgconfig"
        port = "export PATH=/usr/bin:/usr/local/bin:/bin:%s && export PKG_CONFIG_PATH=%s" % (
            self.deps[1].get_bin(), PKG_CONFIG_PATH)
        return "./autogen.sh && %s && " % port + \
               self.configure_cmd(" CPPFLAGS=-std=c++11")
