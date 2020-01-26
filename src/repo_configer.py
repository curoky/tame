#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

import os
import logging
import yaml
import codecs


class RepoConfiger(object):

    def __init__(self):
        pass

    def get_all(self):
        global_config = {}
        config_dir = os.path.dirname(os.path.abspath(__file__))
        config_dir = os.path.join(config_dir, "..", "modules")
        files = os.listdir(config_dir)
        for f in files:
            if not f.endswith(".yml"):
                continue
            with codecs.open(os.path.join(config_dir, f)) as target:
                content = yaml.load(target.read(), Loader=yaml.SafeLoader)
                global_config[content["name"]] = content
        logging.debug("register %d repo", len(global_config))
        return global_config