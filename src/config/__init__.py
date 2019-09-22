#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

import logging

from .shell_tool import *
from .other import *
from .facebook import *
from .google import *
from .gun import *

global_config = {}


def register(name, url, builder, website=None, deps=None):
    if name in global_config:
        logging.critical("%s already in global_config!!!", name)
    global_config[name] = dict(
        name=name,
        website=website,
        deps=deps or set(),
        url=url,
        builder=builder,
    )


def builder_helper(type, cmd, src_path, build_path):
    return dict(type=type, cmd=cmd, src=src_path, build_path=build_path)


def make_cmd():
    return "make -j {{thread_num}} && make install"


def configure_helper(args="", src_path=".", build_path="_build"):
    return builder_helper(
        type="configure",
        cmd="{{repo_path}}/%s/configure --prefix={{install_path}} %s" %
        (src_path, args) + " && " + make_cmd(),
        src_path=src_path,
        build_path=build_path)


def cmake_helper(args="", src_path=".", build_path="_build"):
    return builder_helper(
        type="cmake",
        cmd=
        'cmake -B {{repo_path}}/%s -S {{repo_path}}/%s -DCMAKE_PREFIX_PATH="{{cmake_prefix}}"'
        ' -DCMAKE_INSTALL_PREFIX={{install_path}} %s' %
        (build_path, src_path, args) + " && " + make_cmd(),
        src_path=src_path,
        build_path=build_path)
