#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

import codecs
import logging
import os
import shutil
import tarfile
import threading
from io import BytesIO

import git
import requests
from jinja2 import Template

global_mirror = {
    "ftp.gnu.org": ["mirrors.tuna.tsinghua.edu.cn", ],
    "www.python.org/ftp": ["npm.taobao.org/mirrors", ],
}

global_url = {
    # gnu
    'autoconf': 'http://ftp.gnu.org/gnu/autoconf/autoconf-{{version}}.tar.gz',
    'automake': 'http://ftp.gnu.org/gnu/automake/automake-{{version}}.tar.gz',
    'bison': 'http://ftp.gnu.org/gnu/bison/bison-{{version}}.tar.gz',
    'gettext': 'http://ftp.gnu.org/gnu/gettext/gettext-{{version}}.tar.gz',
    'gmp': 'http://ftp.gnu.org/gnu/gmp/gmp-{{version}}.tar.xz',
    'mpfr': 'http://ftp.gnu.org/gnu/mpfr/mpfr-{{version}}.tar.gz',
    'mpc': 'http://ftp.gnu.org/gnu/mpc/mpc-{{version}}.tar.gz',
    'gcc': 'http://ftp.gnu.org/gnu/gcc/gcc-{{version}}/gcc-{{version}}.tar.xz',
    'help2man': 'http://ftp.gnu.org/gnu/help2man/help2man-{{version}}.tar.xz',
    'ncurses': 'http://ftp.gnu.org/gnu/ncurses/ncurses-{{version}}.tar.gz',
    'libtool': 'http://ftp.gnu.org/gnu/libtool/libtool-{{version}}.tar.gz',
    'm4': 'http://ftp.gnu.org/gnu/m4/m4-{{version}}.tar.gz',

    # github release
    'tmux': 'https://github.com/tmux/tmux/releases/download/2.8/tmux-2.8.tar.gz',
    'flex': 'https://github.com/westes/flex/releases/download/v{{version}}/flex-{{version}}.tar.gz',
    'libsodium': 'https://github.com/jedisct1/libsodium/releases/download/{{version}}/libsodium-{{version}}.tar.gz',
    'mosh': 'https://github.com/mobile-shell/mosh/releases/download/mosh-{{version}}/mosh-{{version}}.tar.gz',
    'libevent': 'https://github.com/libevent/libevent/'
                'releases/download/release-{{version}}/libevent-{{version}}.tar.gz',
    'protobuf': 'https://github.com/protocolbuffers/protobuf/'
                'releases/download/v{{version}}/protobuf-all-{{version}}.tar.gz',
    'shadowsocks-libev': 'https://github.com/shadowsocks/shadowsocks-libev/'
                         'releases/download/v{{version}}/shadowsocks-libev-{{version}}.tar.gz',

    # github git
    'cmake': 'git@github.com:Kitware/CMake.git',
    'zlib': 'git@github.com:madler/zlib.git',
    'zstd': 'git@github.com:facebook/zstd.git',
    'gflags': 'git@github.com:gflags/gflags.git',
    'glog': 'git@github.com:google/glog',
    'lz4': 'git@github.com:lz4/lz4.git',
    'snappy': 'git@github.com:google/snappy.git',
    'mstch': 'git@github.com:no1msd/mstch.git',
    'mbedtls': 'git@github.com:ARMmbed/mbedtls.git',
    'c_ares': 'git@github.com:c-ares/c-ares.git',
    'double-conversion': 'git@github.com:google/double-conversion.git',
    'gtest': 'git@github.com:google/googletest.git',
    'fizz': 'git@github.com:facebookincubator/fizz.git',
    'folly': 'git@github.com:facebook/folly',
    'wangle': 'git@github.com:facebook/wangle',
    'fbthrift': 'git@github.com:facebook/fbthrift',
    'yarpl': 'git@github.com:rsocket/rsocket-cpp.git',
    'vim': 'git@github.com:vim/vim.git',
    'krb5': 'git@github.com:krb5/krb5.git',

    # others
    'pcre': 'http://ftp.pcre.org/pub/pcre/pcre-{{version}}.tar.gz',
    'boost': 'https://dl.bintray.com/boostorg/release/{{version}}/source/boost_{{version|replace(".","_")}}.tar.gz',
    'pkg-config': 'https://pkg-config.freedesktop.org/releases/pkg-config-{{version}}.tar.gz',
    'curl': 'http://curl.haxx.se/download/curl-{{version}}.tar.gz',
    'libev': 'http://dist.schmorp.de/libev/libev-{{version}}.tar.gz',
    'git': 'https://mirrors.edge.kernel.org/pub/software/scm/git/git-{{version}}.tar.gz',
    'lzma': 'https://tukaani.org/xz/xz-{{version}}.tar.gz',
    'python': 'https://www.python.org/ftp/python/{{version}}/Python-{{version}}.tgz',
    'zsh': 'https://jaist.dl.sourceforge.net/project/zsh/zsh/{{version}}/zsh-{{version}}.tar.xz',
    'openssl': 'https://www.openssl.org/source/openssl-{{version}}.tar.gz',
    'tree': 'http://mama.indstate.edu/users/ice/tree/src/tree-{{version}}.tgz',
}

global_info = {
    'autoconf': dict(version=['2.69', ], website='None'),
    'automake': dict(version=['1.16.1', ], website='None'),
    'bison': dict(version=['3.1', ], website='https://www.gnu.org/software/bison/'),
    'gettext': dict(version=['0.19.8', ], website='https://www.gnu.org/software/gettext/'),
    'gmp': dict(version=['6.1.2', ], website='https://gmplib.org/'),
    'mpfr': dict(version=['4.0.2', ], website='https://www.mpfr.org/'),
    'mpc': dict(version=['1.1.0', ], website='None'),
    'gcc': dict(version=['5.5.0', ], website='https://gcc.gnu.org'),
    'help2man': dict(version=['1.47.9', ], website='None'),
    'ncurses': dict(version=['6.1', ], website='https://www.gnu.org/software/ncurses/'),
    'libtool': dict(version=['2.4.6', ], website='https://www.gnu.org/software/libtool/'),
    'm4': dict(version=['1.4.18', ], website='None'),
    'pcre': dict(version=['8.43', ], website='https://pcre.org/'),
    'pkg-config': dict(version=['0.29.2', ], website='None'),
    'curl': dict(version=['7.64.0', ], website='https://curl.haxx.se/'),
    'libev': dict(version=['4.25', ], website='http://software.schmorp.de/pkg/libev.html'),
    'libevent': dict(version=['2.1.8-stable', ], website='http://libevent.org'),
    'libsodium': dict(version=['1.0.16', ], website='https://libsodium.org'),
    'lzma': dict(version=['5.2.3', ], website='None'),
    'protobuf': dict(version=['3.7.1', ], website='https://developers.google.com/protocol-buffers/'),
    'zlib': dict(version=['v1.2.11', ], website='http://zlib.net/'),
    'python': dict(version=['3.6.3', ], website='None'),
    'tmux': dict(version=['2.8', ], website='None'),
    'flex': dict(version=['2.6.4', ], website='https://www.gnu.org/software/flex/'),
    'mosh': dict(version=['1.3.2', ], website='https://mosh.org'),
    'cmake': dict(version=['v3.13.4', ], website='https://cmake.org/'),
    'shadowsocks-libev': dict(version=['3.2.4', ], website='None'),
    'git': dict(version=['2.19.2', ], website='https://git-scm.com/'),
    'zstd': dict(version=['v1.3.5', ], website='None'),
    'gflags': dict(version=['v2.2.2', ], website='https://gflags.github.io/gflags/'),
    'glog': dict(version=['v0.4.0', ], website='None'),
    'lz4': dict(version=['v1.8.2', ], website='None'),
    'snappy': dict(version=['1.1.7', ], website='None'),
    'mstch': dict(version=['1.0.2', ], website='None'),
    'mbedtls': dict(version=['mbedtls-2.1.18', ], website='https://tls.mbed.org'),
    'c_ares': dict(version=['cares-1_15_0', ], website='https://c-ares.haxx.se/'),
    'double-conversion': dict(version=['v3.0.0', ], website='None'),
    'gtest': dict(version=['release-1.8.1', ], website='None'),
    'fizz': dict(version=['v2019.04.22.00', ], website='None'),
    'folly': dict(version=['v2019.03.04.00', ], website='None'),
    'wangle': dict(version=['v2019.03.04.00', ], website='None'),
    'fbthrift': dict(version=['v2019.03.04.00', ], website='None'),
    'yarpl': dict(version=['master', ], website='http://rsocket.io/'),

    'zsh': dict(version=['5.7.1', ], website='http://www.zsh.org'),
    'vim': dict(version=['v8.1.0996', ], website='https://www.vim.org/'),

    'openssl': dict(version=['1.1.1b', ], website="https://www.openssl.org"),
    'krb5': dict(version=['krb5-1.16.1-final', ]),
    'boost': dict(version=['1.70.0', ], website="https://www.boost.org/"),
    'tree': dict(version=['1.8.0', ]),

}


class Downloader(object):

    def __init__(self, root, thread_num):
        self.root = root
        self.thread_num = thread_num
        self.cache_dir = os.path.join(root, "_cache")
        self.logger = logging.getLogger(__name__)

        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

    def downloads(self, repos: {str: str}, proxies):
        self.logger.info('start to download \n[%s]', str(repos))
        ths = []
        for name in repos:
            th = threading.Thread(target=self._download_one, args=(name, repos[name], proxies,))
            th.start()
            ths.append(th)
        for th in ths:
            th.join()

    def _download_one(self, name, version, proxies):
        url = Template(global_url[name]).render(version=version)
        if "git@" in url:
            self._down_load_with_git(url, name, version, proxies)
        else:
            self._down_load_with_tar(url, name, version, proxies)

    def _down_load_with_git(self, url, name, version, proxies):
        repo_name = name + "_" + version
        repo_path = os.path.join(self.root, repo_name)

        if os.path.isdir(repo_path):
            try:
                repo = git.Repo(path=repo_path)
            except git.InvalidGitRepositoryError:
                repo = None

            if repo and not repo.head.is_detached:
                if str(repo.active_branch) == version:
                    repo.git.reset('--hard')
                    repo.git.clean('-xdf')
                    repo.remotes.origin.pull()
                    self.logger.info("[%s]: git exists, just pull", repo_name)
                    return
            elif repo:
                if str(repo.head.commit) == repo.git.execute(["git", "rev-list", "-1", version]):
                    repo.git.reset('--hard')
                    repo.git.clean('-xdf')
                    self.logger.info("[%s]: git exists, commit equal", repo_name)
                    return

            self.logger.warning("[%s]:exist not available remove it", repo_name, version)
            shutil.rmtree(repo_path)

        self.logger.info("[%s]:start clone ~", repo_name)
        try:
            git.Repo.clone_from(url=url, to_path=repo_path, branch=version, depth=1)
        except git.GitCommandError as e:
            self.logger.critical("%s", e.stderr)
        self.logger.info("[%s]:success to clone", repo_name)

    def _down_load_with_tar(self, url, name, version, proxies):
        # check for mirror
        for k in global_mirror:
            if k in url:
                url = url.replace(k, global_mirror[k][0])
        repo_name = name + "_" + version
        repo_path = os.path.join(self.root, repo_name)

        file_name = os.path.basename(url)
        f = self._get_cache(file_name)
        if f is None:
            f = BytesIO()
            f.write(requests.get(url, proxies=proxies).content)
            self.logger.info("success to download %s", file_name)
            self._set_cache(file_name, f)
        mode = file_name.split(".")[-1]
        if mode == "tgz":
            mode = "gz"
        t = tarfile.open(fileobj=f, mode="r:" + mode)
        for m in t.getmembers():
            m.path = "/".join(m.path.split('/')[1:])
        shutil.rmtree(repo_path, ignore_errors=True)
        t.extractall(repo_path)

    def _get_cache(self, file_name):
        rio = BytesIO()
        if os.path.exists(os.path.join(self.cache_dir, file_name)):
            self.logger.info("[%s]: find in cache", file_name)
            with codecs.open(os.path.join(self.cache_dir, file_name), "rb")as cf:
                rio.write(cf.read())
                rio.seek(0)
            return rio
        self.logger.info("[%s]: not in cache", file_name)
        return None

    def _set_cache(self, file_name, file_obj):
        if os.path.exists(os.path.join(self.cache_dir, file_name)):
            self.logger.critical('[%s] should not exists', file_name)

        with codecs.open(os.path.join(self.cache_dir, file_name), "wb") as cf:
            file_obj.seek(0)
            cf.write(file_obj.read())
            file_obj.seek(0)
        self.logger.info("[%s]: save to cache", file_name)
