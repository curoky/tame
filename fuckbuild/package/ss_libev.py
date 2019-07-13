#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target
from .pcre import Pcre
from .mbedtls import Mbedtls
from .libsodium import Libsodium
from .c_ares import Cares
from .libev import Libev


class Sslibev(Target):
    """
    3.2.5 编译不过
    """

    def __init__(self, prefix_path):
        super(Sslibev, self).__init__(prefix_path,
                                      name="ss_libev",
                                      version="v3.2.4",
                                      git_uri="git@github.com:shadowsocks/shadowsocks-libev.git")
        self.deps = [Pcre(self.prefix_path),
                     Mbedtls(self.prefix_path),
                     Libsodium(self.prefix_path),
                     Cares(self.prefix_path),
                     Libev(self.prefix_path)]

    def get_build_cmd(self):
        submod = "git submodule update --init --recursive && "
        return submod + "./autogen.sh && " + \
               self.configure_cmd(" --disable-documentation"
                                  " --with-pcre=%s"
                                  " --with-mbedtls=%s"
                                  " --with-sodium=%s"
                                  " --with-cares=%s"
                                  " --with-ev=%s",
                                  self.deps[0].install_path(),
                                  self.deps[1].install_path(),
                                  self.deps[2].install_path(),
                                  self.deps[3].install_path(),
                                  self.deps[4].install_path(),
                                  )
