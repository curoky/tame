#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


import codecs
import json
import logging
import os
import subprocess
import sys
import time

from jinja2 import Template


def make_helper():
    return ""


def cmake_helper(src=".", build_path="_build", args=""):
    return dict(cmd='cmake -B {{repo_path}}/%s -S {{repo_path}}/%s -DCMAKE_PREFIX_PATH="{{cmake_prefix}}" '
                    ' -DCMAKE_INSTALL_PREFIX={{install_path}} %s' % (
                        build_path, src, args) + " && make -j {{thread_num}} && make install",
                type="cmake", build_path=build_path)


def configure_helper(src="./", build_path="_build", args=""):
    return dict(cmd="{{repo_path}}/%s/configure --prefix={{install_path}} %s" % (
        src, args) + " && make -j {{thread_num}} && make install",
                type="configure", build_path=build_path)


global_build_cmd = {
    'autoconf': configure_helper(),
    'automake': configure_helper(),
    'bison': configure_helper(),
    'gettext': configure_helper(),
    'gmp': configure_helper(),
    'mpfr': configure_helper(),
    'mpc': configure_helper(),
    'gcc': configure_helper(args='--disable-multilib --enable-checking=release'
                                 ' --enable-languages=c,c++ --with-system-zlib'),
    'help2man': configure_helper(),
    'ncurses': configure_helper(args=' --with-ticlib --with-shared --disable-tic-depends'
                                     ' --with-pkg-config  --enable-pc-files'),
    'libtool': configure_helper(),
    'm4': configure_helper(),
    'pcre': configure_helper(),
    'pkg-config': configure_helper(args='--with-internal-glib'),
    'curl': configure_helper(),
    'libev': configure_helper(),
    'libevent': configure_helper(),
    'libsodium': configure_helper(),
    'lzma': configure_helper(),
    'protobuf': configure_helper(),
    'zlib': configure_helper(),
    'python': configure_helper(args='--enable-optimizations'),
    'tmux': configure_helper(),
    'flex': configure_helper(),
    'mosh': configure_helper(args='CPPFLAGS=-std=c++11'),
    'cmake': configure_helper(),
    'shadowsocks-libev': configure_helper(args='--disable-documentation'),
    'git': configure_helper(),

    'zstd': cmake_helper(src="build/cmake"),
    'gflags': cmake_helper(args='-DBUILD_SHARED_LIBS=ON'),
    'glog': cmake_helper(),
    'lz4': cmake_helper(src="contrib/cmake_unofficial"),
    'snappy': cmake_helper(args='-DSNAPPY_BUILD_TESTS=OFF'),
    'mstch': cmake_helper(),
    'mbedtls': cmake_helper(),
    'c_ares': cmake_helper(),
    'double-conversion': cmake_helper(),
    'gtest': cmake_helper(),
    'fizz': cmake_helper(),
    'folly': cmake_helper(),
    'wangle': cmake_helper(),
    'fbthrift': cmake_helper(),
    'yarpl': cmake_helper(args='-DBUILD_TESTS=OFF -DBUILD_EXAMPLES= -DBUILD_BENCHMARKS=OFF'),

    'vim': configure_helper(build_path='.'),
    'zsh': dict(
        cmd='{{repo_path}}/configure --prefix={{install_path}} --with-term-lib="ncurses"'
            ' && make -j {{thread_num}} && make install',
        type="configure", build_path='.'),

    'openssl': dict(
        cmd="{{repo_path}}/config --prefix={{install_path}} --openssldir={{install_path}}/ssl" + " && " + make_helper(),
        type="configure", build_path="."),

    'krb5': dict(
        cmd="cd src && autoreconf -ivf && {{repo_path}}/configure --prefix={{install_path}}" + " && " + make_helper(),
        type="configure", build_path="."),

    'boost': dict(
        cmd='./bootstrap.sh --prefix={{install_path}} && ./b2 install --prefix={{install_path}} -j{{thread_num}}',
        type="custom", build_path="."),

    'tree': dict(
        cmd="make && cp {{repo_path}}/tree {{install_path}}/bin",
        type="custom", build_path="."),
}


class TargetInfo(object):
    def __init__(self, name, version, install_path, force_build):
        self.name = name
        self.version = version
        self.install_path = install_path
        self.force_build = force_build


class Builder(object):

    def __init__(self, root, thread_num):
        self.root = root
        self.logger = logging.getLogger(__name__)
        self.thread_num = thread_num
        self.env = None

    def _prepare_env(self, install_paths):
        self.env = dict()
        self.env["PATH"] = ":".join(
            [os.path.join(p, "bin") for p in install_paths]) + ":" + os.environ["PATH"]

        self.env["PKG_CONFIG_PATH"] = ":".join(
            [os.path.join(p, "lib") for p in install_paths])

        # Just use for automake
        self.dep_libs = ""
        self.dep_incs = ""
        for p in install_paths:
            self.dep_libs += "-L%s " % os.path.join(p, "lib")
            self.dep_incs += "-I%s " % os.path.join(p, "include")
        self.env["LDFLAGS"] = '%s' % self.dep_libs
        self.env["CPPFLAGS"] = '%s' % self.dep_incs
        self.env["CFLAGS"] = self.env["CPPFLAGS"]
        # self.env["LIBS"] = '-lncurses'
        # self.env["CXXFLAGS"] = '-I%s' % os.path.join(self.deps_path, "include")

    def build(self, name, totle_target: {str, TargetInfo}):
        install_paths = set([os.path.join(self.root, t.install_path) for t in totle_target.values()])

        repo_name = name + "_" + totle_target[name].version
        repo_path = os.path.join(self.root, repo_name)
        install_path = totle_target[name].install_path
        force_build = totle_target[name].force_build

        if self._check_build_mark(repo_name) and not force_build:
            self.logger.info("[%s]: already build", repo_name)
            return 0

        config = global_build_cmd[name]

        if config["type"] == "cmake":
            cmd = Template(config["cmd"]).render(
                cmake_prefix=";".join(install_paths),
                install_path=install_path, repo_path=repo_path,
                thread_num=self.thread_num)
        elif config["type"] == "configure":
            self._prepare_env(install_paths)
            cmd = Template(config["cmd"]).render(
                install_path=install_path, repo_path=repo_path, thread_num=self.thread_num)
        else:
            cmd = Template(config["cmd"]).render(
                install_path=install_path, repo_path=repo_path, thread_num=self.thread_num)

        build_path = os.path.join(repo_path, config["build_path"])
        if not os.path.exists(build_path):
            os.makedirs(build_path)

        self.logger.info("start to build %s\n\t with cmd: %s\n\t with env: %s",
                         str(totle_target[name]), cmd, self.env)
        res = subprocess.Popen(cmd, cwd=build_path, env=self.env,
                               shell=True, stdout=sys.stdout, stderr=sys.stderr)
        retcode = res.wait()
        if retcode == 0:
            self._write_build_mark(repo_name)
        return retcode

    def _check_build_mark(self, repo_name):
        mark = self._load_build_mark()
        if mark and repo_name in mark:
            return True
        return False

    def _write_build_mark(self, repo_name):
        mark_path = os.path.join(self.root, "VERSION")
        mark = self._load_build_mark()
        if not mark:
            mark = {}
        if repo_name not in mark:
            mark[repo_name] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime())
            with codecs.open(mark_path, "w", "utf8") as f:
                f.write(json.dumps(mark))
        self.logger.info("[%s] write build version", repo_name)

    def _load_build_mark(self):
        mark_path = os.path.join(self.root, "VERSION")
        if os.path.isfile(mark_path):
            with codecs.open(mark_path, "r", "utf8") as f:
                return json.loads(f.read())
