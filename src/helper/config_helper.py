#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

import codecs
import logging
import os

from ruamel.yaml import YAML


class ConfigHelper(object):

    def __init__(self):
        abs_path = os.path.dirname(os.path.abspath(__file__))
        self.config_dir = os.path.join(abs_path, "../..", "modules")
        self.logging = logging.getLogger("config")

    def get_modules(self):
        modules = {}
        files = os.listdir(self.config_dir)
        for f in files:
            if not f.endswith(".yml"):
                continue
            self.logging.debug("read ymal file %s", f)
            with codecs.open(os.path.join(self.config_dir, f)) as target:
                content = YAML().load(target.read())
                if "depend" in content and content["depend"] is None:
                    content.pop("depend")
                modules[f[:-4]] = content
        logging.info("load modules size %d", len(modules))
        return modules
