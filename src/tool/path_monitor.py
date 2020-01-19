# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

import os


class PathMonitor(object):

    def __init__(self, path):
        self.path = path
        self.reset(path)

    def reset(self, path=None):
        self.path = path or self.path
        self.file_list = self.collect_path(path)

    @staticmethod
    def collect_path(path):
        file_list = []
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                file_list.append(os.path.join(root, name))
        return file_list

    def get_change_list(self, path):
        return list(set(self.collect_path(path)) - set(self.file_list))
