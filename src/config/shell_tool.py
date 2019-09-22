#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

from . import register, configure_helper, builder_helper

register(name="tmux",
         deps={'pkg-config', 'ncurses', 'libevent'},
         url="https://github.com/tmux/tmux/releases/download/2.8/tmux-2.8.tar.gz",
         builder=configure_helper())

register(name="mosh",
         website="https://mosh.org",
         deps={'ncurses', 'protobuf', 'zlib'},
         url="https://github.com/mobile-shell/mosh/releases/download/mosh-{{version}}/mosh-{{version}}.tar.gz",
         builder=configure_helper(args='CPPFLAGS=-std=c++11'))

register(name="vim",
         website="https://www.vim.org/", deps={'ncurses'}, url="git@github.com:vim/vim.git",
         builder=configure_helper(build_path='.'))

register(name="curl",
         website="https://curl.haxx.se/",
         url="http://curl.haxx.se/download/curl-{{version}}.tar.gz",
         builder=configure_helper())

register(name="git",
         website="https://git-scm.com/",
         deps={'zlib', 'curl'},
         url="https://mirrors.edge.kernel.org/pub/software/scm/git/git-{{version}}.tar.gz",
         builder=configure_helper())

register(name="zsh",
         website="http://www.zsh.org",
         deps={'ncurses'},
         url="https://jaist.dl.sourceforge.net/project/zsh/zsh/{{version}}/zsh-{{version}}.tar.xz",
         builder=configure_helper(args='--with-term-lib="ncurses"', build_path="."))

register(name="cmake",
         website="https://cmake.org/",
         url="git@github.com:Kitware/CMake.git",
         builder=configure_helper())

register(name="shadowsocks-libev",
         deps={'libsodium', 'libev', 'mbedtls', 'c_ares', 'pcre'},
         url="https://github.com/shadowsocks/shadowsocks-libev/releases/"
         "download/v{{version}}/shadowsocks-libev-{{version}}.tar.gz",
         builder=configure_helper("--disable-documentation"))

register(name="python",
         url="https://www.python.org/ftp/python/{{version}}/Python-{{version}}.tgz",
         builder=configure_helper("--enable-optimizations"))

register(name="ack",
         website="https://beyondgrep.com/",
         url="git@github.com:beyondgrep/ack2.git",
         builder=builder_helper(
             type="custom", build_path=".", src_path=".",
             cmd="mkdir -p {{install_path}}/bin && curl https://beyondgrep.com/ack-2.28-single-file > {{install_path}}/bin/ack && chmod 0755 {{install_path}}/bin/ack",
         ))
