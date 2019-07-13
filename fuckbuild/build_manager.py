#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


import codecs
import json
import logging
import os
import time


class BuildManager(object):

    def __init__(self):
        pass

    @staticmethod
    def load_mark(install_root):
        mark_path = os.path.join(install_root, "VERSION")
        if os.path.isfile(mark_path):
            with codecs.open(mark_path, "r", "utf8") as f:
                return json.loads(f.read())

    @staticmethod
    def check_mark(install_root, repo_name):
        mark = BuildManager.load_mark(install_root)
        if mark and repo_name in mark:
            logging.info("[%s]: already build", repo_name)
            return True
        return False

    @staticmethod
    def write_mark(install_root, repo_name):
        mark_path = os.path.join(install_root, "VERSION")
        mark = BuildManager.load_mark(install_root)
        if not mark:
            mark = {}
        if repo_name not in mark:
            mark[repo_name] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime())
            with codecs.open(mark_path, "w", "utf8") as f:
                f.write(json.dumps(mark))
        logging.info("[%s] write build version", repo_name)
