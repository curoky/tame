#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        : manage cache file


import os
import time
import json
import codecs
import logging
from io import BytesIO



class CacheManager(object):

    def __init__(self, root):
        self.root = root
        self.cache_dir = os.path.join(root, "_cache")
        self.logger = logging.getLogger(__name__)

        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

    def get(self, file_name):
        rio = BytesIO()
        if os.path.exists(os.path.join(self.cache_dir, file_name)):
            logging.info("[%s]: find in cache", file_name)
            with codecs.open(os.path.join(self.cache_dir, file_name), "rb")as cf:
                rio.write(cf.read())
                rio.seek(0)
            return rio
        self.logger.info("[%s]: not in cache", file_name)
        return None

    def set(self, file_name, file_obj):
        if os.path.exists(os.path.join(self.cache_dir, file_name)):
            logging.fatal('[%s] should not exists', file_name)
        with codecs.open(os.path.join(self.cache_dir, file_name), "wb") as cf:
            file_obj.seek(0)
            cf.write(file_obj.read())
            file_obj.seek(0)
        self.logger.info("[%s]: save to cache", file_name)

    def _load_mark(self):
        mark_path = os.path.join(self.root, "VERSION")
        if os.path.isfile(mark_path):
            with codecs.open(mark_path, "r", "utf8") as f:
                return json.loads(f.read())

    def check_mark(self, name):
        mark = self._load_mark()
        if mark and name in mark:
            self.logger.info("[%s]: already build", name)
            return True
        return False

    def write_mark(self, name):
        mark_path = os.path.join(self.root, "VERSION")
        mark = self._load_mark()
        if not mark:
            mark = {}
        if name not in mark:
            mark[name] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime())
            with codecs.open(mark_path, "w", "utf8") as f:
                f.write(json.dumps(mark))
        self.logger.info("[%s] write build version", name)
