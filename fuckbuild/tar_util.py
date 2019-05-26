#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


def get_fit_cmd(name):
    if name.endswith("tar.xz"):
        return "xvf"
    if name.endswith("tar.gz") or name.endswith("tgz"):
        return "zxvf"
