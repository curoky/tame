#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        : manage mirror file


import queue
import importlib
from .package import Target
from .package.base import simple_repos


class TargetManager(object):

    def __init__(self, root, cache, name, deps_version=None):
        self.root = root
        self.name = name
        self.cache = cache
        self.deps_version = deps_version or {}

        self.all_deps = set()
        self.instances = []
        self.instances_map = {}

        self._get_all_deps(name)
        self._sort_all_deps()

    def _get_repo(self, name):
        if name in simple_repos:
            return Target.from_config(
                root=self.root, cache=self.cache,
                config=simple_repos[name], version=self.deps_version.get(name, None))
        try:
            repo = importlib.import_module("src.package.%s" % name)
        except ImportError:
            name = "lib" + name
            repo = importlib.import_module("src.package.%s" % name)
        return getattr(repo, name)

    def _get_all_deps(self, name):
        if name in self.instances_map:
            return

        ins = self._get_repo(name)
        self.instances.append(ins)
        self.instances_map[name] = ins

        self.all_deps.update(ins.deps)
        for dep in ins.deps:
            self._get_all_deps(dep)

    def _sort_all_deps(self):
        self.all_deps = []
        q = queue.Queue()
        for ins in self.instances:
            if len(ins.deps) == 0:
                q.put(ins)
                self.all_deps.append(ins.name)

        while not q.empty():
            front = q.get()
            for ins in self.instances:
                if front.name in ins.deps:
                    ins.deps.remove(front.name)
                    if len(ins.deps) == 0:
                        self.all_deps.append(ins.name)
