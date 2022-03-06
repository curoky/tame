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
import os

from . import Package
from .builder import Builder
from .depender import Depender
from .downloader import Downloader
from .helper import ConfigHelper, EnvHelper


class Chafer(object):

    def __init__(self, root):
        if not os.path.exists(root):
            os.makedirs(root)

        self.root = root
        self.archive_prefix = os.path.join(self.root, 'archive')
        self.extract_prefix = os.path.join(self.root, 'extract')
        self.install_prefix = os.path.join(self.root, 'install')
        os.makedirs(self.root, exist_ok=True)
        os.makedirs(self.archive_prefix, exist_ok=True)
        os.makedirs(self.extract_prefix, exist_ok=True)
        os.makedirs(self.install_prefix, exist_ok=True)

        self.pkg_list = []
        self.config_helper = ConfigHelper()
        self.modules = self.config_helper.get_modules()

        self.depender = Depender(self.modules)
        self.downloader = Downloader()
        self.builder = Builder()

        self.logger = logging.getLogger('main')

    def prepare(self, name, with_deps, inc_list: [str] = None):
        if with_deps:
            deps = self.depender.get_deps(name)
            deps = self.depender.sort_deps(deps)
        else:
            deps = [name]
        inc_list = inc_list or []
        inc_map = {}
        self.pkg_list.clear()
        for d in deps:
            pkg = Package(d, self.archive_prefix, self.extract_prefix, self.install_prefix,
                          self.modules[d])
            inc_map[d] = pkg.install_path
            inc_list.append(pkg.install_path)
            pkg.prepare_build_opt(inc_list, inc_map)
            self.pkg_list.append(pkg)

        self.logger.info('build target list: %s', [p.name for p in self.pkg_list])

    def download(self):
        self.downloader.download(self.pkg_list)

    def build(self):
        self.builder.build(self.pkg_list)

    def gen(self):
        bash_file = os.path.join(self.root, 'main.sh')
        cmake_file = os.path.join(self.root, 'FindCmakePrefixConfig.cmake')
        EnvHelper.generator_bash_file(self.install_prefix, bash_file)
        EnvHelper.generator_cmake_file(self.install_prefix, cmake_file)
