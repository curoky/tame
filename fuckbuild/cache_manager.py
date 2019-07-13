#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        : manage cache file

import codecs
import logging
import os
from cStringIO import StringIO


class CacheManager(object):

    def __init__(self):
        pass

    @staticmethod
    def get(cache_dir, file_name):
        rio = StringIO()
        if os.path.exists(os.path.join(cache_dir, file_name)):
            logging.info("[%s]: find in cache", file_name)
            with codecs.open(os.path.join(cache_dir, file_name), "rb")as cf:
                rio.write(cf.read())
                rio.seek(0)
            return rio
        logging.info("[%s]: not in cache", file_name)
        return None

    @staticmethod
    def set(cache_dir, file_name, file_obj):
        if os.path.exists(os.path.join(cache_dir, file_name)):
            logging.fatal('[%s] should not exists', file_name)
        with codecs.open(os.path.join(cache_dir, file_name), "wb") as cf:
            file_obj.seek(0)
            cf.write(file_obj.read())
            file_obj.seek(0)
        logging.info("[%s]: save to cache", file_name)
