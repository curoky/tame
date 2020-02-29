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

from .make_builder import MakeBuilder


class CmakeBuilder(MakeBuilder):

    def __init__(self, options):
        super().__init__(options)
        self.cmake_prefix_path = options.cmake_prefix_path

    def command_prepare(self):
        return 'cmake -B {} -S {} -DCMAKE_PREFIX_PATH="{}" -DCMAKE_INSTALL_PREFIX={} {}'.format(
            self.build_path, self.index_path, self.cmake_prefix_path, self.install_path, self.args)
