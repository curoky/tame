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

import codecs
import logging
import os

from ruamel.yaml import YAML


class ConfigHelper(object):

    def __init__(self):
        abs_path = os.path.dirname(os.path.abspath(__file__))
        self.modules_dir = os.path.join(abs_path, '../..', 'modules')
        self.logging = logging.getLogger('config')

    def get_modules(self):
        modules = {}
        for root, dirs, files in os.walk(self.modules_dir, topdown=False):
            for name in files:
                f = os.path.join(root, name)
                if not f.endswith('.yml'):
                    continue
                self.logging.debug('read file %s', f)
                with codecs.open(f, 'r', 'utf8') as target:
                    content = YAML().load(target.read())
                    if 'depend' in content and content['depend'] is None:
                        content.pop('depend')
                    modules[os.path.basename(f)[:-4]] = content
        logging.info('load modules size %d', len(modules))
        return modules

    def new(self, name):
        sub_dir = os.path.join(self.modules_dir, name[0])
        os.makedirs(sub_dir, exist_ok=True)
        config_path = os.path.join(sub_dir, name + '.yml')
        self.logging.info('write config to %s', config_path)
        with codecs.open(config_path, 'w', 'utf8') as target:
            target.write('website:\n')
            target.write('description:\n')
            target.write('version:\n')
            target.write('  -\n\n')
            target.write('git:\n')
            target.write('archive:\n')
            target.write('depend:\n\n')
            target.write('compile:\n')
            target.write('  type: cmake\n')
