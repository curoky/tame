#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

import logging
import queue

global_deps = {
    'automake': {'autoconf'},
    'mpfr': {'gmp'},
    'mpc': {'mpfr', 'gmp'},
    'gcc': {'mpc', 'mpfr', 'zlib', 'gmp'},
    'tmux': {'pkg-config', 'ncurses', 'libevent'},
    'flex': {'libtool', 'automake', 'gettext', 'bison'},
    'mosh': {'ncurses', 'zlib', 'protobuf'},
    'shadowsocks-libev': {'libsodium', 'pcre', 'c_ares', 'libev', 'mbedtls'},
    'git': {'curl', 'zlib'},
    'glog': {'gflags'},
    'mstch': {'boost'},
    'snappy': {'gtest'},
    'fizz': {'libsodium', 'libevent', 'openssl', 'double-conversion', 'folly'},
    'folly': {'gflags', 'boost', 'libevent', 'openssl', 'lz4', 'lzma', 'snappy',
              'glog', 'double-conversion', 'zstd'},
    'wangle': {'fizz', 'gflags', 'boost', 'libevent', 'openssl', 'gtest', 'glog',
               'double-conversion', 'folly'},
    'fbthrift': {'wangle', 'fizz', 'boost', 'gflags', 'zlib', 'mstch', 'openssl',
                 'gtest', 'glog', 'flex', 'bison', 'zstd', 'folly', 'krb5'},
    'yarpl': {'gflags', 'boost', 'gtest', 'glog', 'double-conversion', 'folly'},
    'vim': {'ncurses'},
    'zsh': {'ncurses'},
    'krb5': {"bison", "automake"}
}


class Depender(object):

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def _prepare_deps(self, name, deps: set):
        sub_deps = global_deps.get(name, None) or set()
        deps.update(sub_deps)
        for dep in sub_deps:
            self._prepare_deps(dep, deps)

    def _sort_deps(self, deps: set):
        ret = []
        temp_deps_map = global_deps.copy()

        q = queue.Queue()
        for dep in deps:
            if dep not in temp_deps_map or len(temp_deps_map[dep]) == 0:
                q.put(dep)
                ret.append(dep)

        while not q.empty():
            front = q.get()
            for dep in deps:
                if dep not in temp_deps_map:
                    continue
                if temp_deps_map[dep] and front in temp_deps_map[dep]:
                    temp_deps_map[dep].remove(front)
                    if len(temp_deps_map[dep]) == 0:
                        q.put(dep)
                        ret.append(dep)
        return ret

    def get_deps_list(self, name):
        deps = set()
        self._prepare_deps(name, deps)
        self.logger.info("get ori deps [%s]", str(deps))
        sorted_deps = self._sort_deps(deps)
        sorted_deps.append(name)
        self.logger.info("get soted deps [%s]", str(sorted_deps))
        return sorted_deps

    def get_deps_map(self, name):
        pass
