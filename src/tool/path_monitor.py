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
