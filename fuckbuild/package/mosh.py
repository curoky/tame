#!/ usr / bin / env python
# - * - coding : utf - 8 - * -
# @Author : IceCory(icecory520 @gmail.com)
# @Copyright(C) : GPL 3.0
# @desc:

from . import Target
from .ncurses import ncurses
from .protobuf import protobuf


class mosh(Target):

    def __init__(self, root, version="mosh-1.3.2", install_root=None):
        super(mosh, self).__init__(
            root, "mosh", version, install_root,
            website="https://mosh.org",
            git_uri="git@github.com:mobile-shell/mosh.git",
            deps=[ncurses, protobuf])

    def get_build_cmd(self):
        PKG_CONFIG_PATH = self.deps[1].install_lib + "/pkgconfig" + ":" + self.deps[0].install_lib + "/pkgconfig"
        port = "export PATH=/usr/bin:/usr/local/bin:/bin:%s && export PKG_CONFIG_PATH=%s" % (
            self.deps[1].install_bin, PKG_CONFIG_PATH)
        return "./autogen.sh && %s && " % port + \
               self.configure_cmd(" CPPFLAGS=-std=c++11")
