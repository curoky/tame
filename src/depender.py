#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

import logging


class Depender(object):

    def __init__(self, modules):
        self.modules = modules
        self.logger = logging.getLogger('Depender')

    def get_deps(self, name) -> {str}:
        # bfs search for all deps
        all_deps = {name}
        q = queue.Queue()
        q.put(name)
        while not q.empty():
            node = q.get()
            all_deps.add(node)
            deps = self.modules[node].get('depend', [])
            for d in deps:
                q.put(d)
        return all_deps

    def sort_deps(self, deps) -> [str]:
        # topological sorting for deps
        sorted_deps = []
        q = queue.Queue()
        graph = {}
        for d in deps:
            graph[d] = set(self.modules[d].get('depend', []))
            if len(graph[d]) == 0:
                sorted_deps.append(d)
                q.put(d)

        while not q.empty():
            node = q.get()
            for d in deps:
                if node in graph[d]:
                    graph[d].remove(node)
                    if len(graph[d]) == 0:
                        q.put(d)
                        sorted_deps.append(d)
        return sorted_deps
