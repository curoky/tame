#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

import logging
import queue

from src.config import repo_config


class Depender(object):

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def _prepare_deps(self, name, all_deps: set):
        child_deps = repo_config[name]["depend"]["lib"] or set()
        all_deps.update(child_deps)
        for dep in child_deps:
            self._prepare_deps(dep, all_deps)

    def _sort_deps(self, deps: set):
        ret = []
        cp_repo_config = repo_config.copy()

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
