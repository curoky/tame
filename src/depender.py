# Copyright 2021 curoky(cccuroky@gmail.com).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
