#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

import logging
import queue

from src.config import global_config


class Depender(object):

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def _prepare_deps(self, name, deps: set):
        child_deps = global_config[name]["deps"]
        deps.update(child_deps)
        for dep in child_deps:
            self._prepare_deps(dep, deps)

    def _sort_deps(self, deps: set):
        ret = []
        cp_global_config = global_config.copy()

        q = queue.Queue()
        for dep in deps:
            if len(cp_global_config[dep]["deps"]) == 0:
                q.put(dep)
                ret.append(dep)

        while not q.empty():
            front = q.get()
            for dep in deps:
                if front in cp_global_config[dep]["deps"]:
                    cp_global_config[dep]["deps"].remove(front)
                    if len(cp_global_config[dep]["deps"]) == 0:
                        q.put(dep)
                        ret.append(dep)
        return ret

    def get_deps_list(self, name):
        deps = set()
        self._prepare_deps(name, deps)
        sorted_deps = self._sort_deps(deps)
        sorted_deps.append(name)
        return sorted_deps

    def get_deps_map(self, name):
        pass
