#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


import importlib


def get_repo(name):
    try:
        repo = importlib.import_module("fuckbuild.package.%s" % name)
    except ImportError:
        name = "lib" + name
        repo = importlib.import_module("fuckbuild.package.%s" % name)
    return getattr(repo, name)
