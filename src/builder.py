#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

import logging
import os

from . import Package
from .build import BuilderFactory


class Builder(object):

    def __init__(self):
        self.logger = logging.getLogger('builder')

    def build(self, pkg_list: [Package], force: bool = False):
        deps_paths = {}
        for pkg in pkg_list:
            if os.path.isdir(pkg.install_path) and os.listdir(pkg.install_path) and not force:
                self.logger.info('[%s]: already build', pkg.dirname)
                continue
            builder = BuilderFactory.create(pkg.type, pkg.build_options)
            # TODO: run test
            steps = [builder.prepare, builder.build, builder.install]
            for step in steps:
                ret = step()
                if ret != 0:
                    self.logger.critical('compile step %s error with code %s', str(step), str(ret))
