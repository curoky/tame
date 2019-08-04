#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        : manage mirror file


_MIRRORS = {
    "ftp.gnu.org": "mirrors.tuna.tsinghua.edu.cn",
    "www.python.org/ftp": "npm.taobao.org/mirrors",
}


def get_mirror(url):
    for k in _MIRRORS:
        if k in url:
            return url.replace(k, _MIRRORS[k])
    return url
