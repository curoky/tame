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

from .make_builder import MakeBuilder


class ConfigureBuilder(MakeBuilder):

    def __init__(self, options):
        super().__init__(options)
        self.autoreconf = options.autoreconf

    def command_prepare(self):
        index = self.index_path
        if os.path.isfile(index):
            pass
        elif os.path.isdir(index):
            index = os.path.join(index, 'configure')
        autoreconf_cmd = ''
        if self.autoreconf:
            autoreconf_cmd = 'autoreconf -ivf && '
        return autoreconf_cmd + '{} --prefix={} {}'.format(
            index,
            self.install_path,
            self.args,
        )
