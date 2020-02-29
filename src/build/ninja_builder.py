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

from .builder import Builder


class NinjaBuilder(Builder):

    def __init__(self, options):
        super().__init__(options)

    def command_prepare(self):
        return 'meson {} --prefix={} --libdir=lib'.format(self.index_path, self.install_path)

    def command_build(self):
        return 'ninja -j %d' % self.thread_num

    def command_install(self):
        return 'ninja install'

    def command_test(self):
        return ''