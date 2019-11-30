#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

import logging
import sys
if sys.version_info < (3, 4):
    import Queue as queue
else:
    import queue


class Depender(object):

    def __init__(self, global_config):
        self.global_config = global_config
        self.logger = logging.getLogger("depender")

    def _prepare_deps(self, name, all_deps):
        child_deps = self.global_config[name]["depend"]["lib"] or set()
        all_deps.update(child_deps)
        for dep in child_deps:
            self._prepare_deps(dep, all_deps)

    def _sort_deps(self, deps):
        ret = []
        cp_repo_config = self.global_config.copy()

        q = queue.Queue()
        for dep in deps:
            child_deps = cp_repo_config[dep]["depend"]["lib"] or set()
            if len(child_deps) == 0:
                q.put(dep)
                ret.append(dep)

        while not q.empty():
            front = q.get()
            for dep in deps:
                child_deps = cp_repo_config[dep]["depend"]["lib"] or set()
                if front in child_deps:
                    cp_repo_config[dep]["depend"]["lib"].remove(front)
                    if len(cp_repo_config[dep]["depend"]["lib"]) == 0:
                        q.put(dep)
                        ret.append(dep)
        return ret

    def get_deps_list(self, name):
        all_deps = set()
        self._prepare_deps(name, all_deps)
        sorted_deps = self._sort_deps(all_deps)
        sorted_deps.append(name)
        return sorted_deps

    def get_deps_map(self, name):
        pass
