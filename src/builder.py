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
from .build import BuilderFactory


class Builder(object):

    def __init__(self):
        self.logger = logging.getLogger('builder')

    def build(self, pkg_list: [Package], force: bool = False):
        deps_paths = {}
        for pkg in pkg_list:
            if os.path.isdir(pkg.install_path) and os.listdir(pkg.install_path) and not force:
                self.logger.info('[%s]: already build', pkg.dirname)
                continue
            builder = BuilderFactory.create(pkg.type, pkg.build_options)
            # TODO: run test
            steps = [builder.prepare, builder.build, builder.install]
            for step in steps:
                ret = step()
                if ret != 0:
                    self.logger.critical('compile step %s error with code %s', str(step), str(ret))
