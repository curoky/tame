#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


from . import Target
from .c_ares import c_ares
from .libev import libev
from .libsodium import libsodium
from .mbedtls import mbedtls
from .pcre import pcre


class sslibev(Target):
    """
    3.2.5 编译不过
    """

    def __init__(self, root, version="v3.2.4", install_root=None):
        super(sslibev, self).__init__(
            root, "ss_libev", version, install_root,
            git_uri="git@github.com:shadowsocks/shadowsocks-libev.git",
            deps=[pcre, mbedtls, libsodium, c_ares, libev]
        )

    def get_build_cmd(self):
        submod = "git submodule update --init --recursive && "
        return submod + "./autogen.sh && " + \
               self.configure_cmd(" --disable-documentation"
                                  " --with-pcre=%s"
                                  " --with-mbedtls=%s"
                                  " --with-sodium=%s"
                                  " --with-cares=%s"
                                  " --with-ev=%s",
                                  self.deps[0].install_root,
                                  self.deps[1].install_root,
                                  self.deps[2].install_root,
                                  self.deps[3].install_root,
                                  self.deps[4].install_root,
                                  )
