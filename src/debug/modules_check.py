#!/usr/bin/env python3

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
import os
import pprint
import shutil

from ruamel.yaml import YAML, RoundTripDumper


def get_module_path():
    dirname = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(dirname, '../..', 'modules')


def url_git2https(url):
    # git@github.com:xxx/yyy.git
    # https://github.com/xxx/yyy.git
    if url.startswith('git@github.com:'):
        return 'https://github.com/' + url.split(':')[1]
    else:
        return url


def url_https2git(url):
    github_prefix = 'https://github.com/'
    if url.startswith(github_prefix):
        return 'git@github.com:' + url[len(github_prefix):]
    else:
        return url


def check_module_name_equal_filename():
    module_path = get_module_path()
    yaml = YAML()
    for m in os.listdir(module_path):
        file_name = os.path.join(module_path, m)
        with codecs.open(file_name, 'r', 'utf8') as target:
            content = yaml.load(target.read())
        if os.path.basename(file_name).split('.')[0] == content['name']:
            continue
        print(content['name'], os.path.basename(file_name).split('.')[0])


def delete_module_key(key='name'):
    module_path = get_module_path()
    yaml = YAML()
    yaml.width = 200
    # yaml.explicit_start = True
    # yaml.explicit_end = True
    yaml.sort_base_mapping_type_on_output = True
    yaml.indent(mapping=2, offset=2)
    yaml.compact(seq_seq=False, seq_map=False)
    for m in os.listdir(module_path):
        file_name = os.path.join(module_path, m)
        new_name = os.path.join(module_path, m.split('.')[0] + '.yaml')
        if file_name.endswith('.yml'):
            with codecs.open(file_name, 'r', 'utf8') as target:
                content = yaml.load(target.read())
            if key in content:
                content.pop(key)
            with codecs.open(file_name, 'w', 'utf8') as target:
                yaml.dump(content, target)


def move_build_step_to_compile():
    module_path = get_module_path()
    yaml = YAML()
    yaml.width = 200
    # yaml.explicit_start = True
    # yaml.explicit_end = True
    yaml.sort_base_mapping_type_on_output = True
    yaml.indent(mapping=2, offset=2)
    yaml.compact(seq_seq=False, seq_map=False)
    for m in os.listdir(module_path):
        file_name = os.path.join(module_path, m)
        print('process %s' % file_name)
        new_name = os.path.join(module_path, m.split('.')[0] + '.yaml')
        if file_name.endswith('.yml'):
            with codecs.open(file_name, 'r', 'utf8') as target:
                content = yaml.load(target.read())
            if 'compile' in content:
                continue
            if content['build']['type'] == 'cmake':
                content.insert(7, 'compile', {})
                content['compile']['type'] = 'cmake'
            if content['build']['type'] == 'configure':
                content.insert(7, 'compile', {})
                content['compile']['type'] = 'configure'
            with codecs.open(file_name, 'w', 'utf8') as target:
                yaml.dump(content, target)
            print(file_name, content['build']['type'])


def split_modules_by_name():
    module_path = get_module_path()
    files = os.listdir(module_path)
    for sub in [chr(i) for i in range(97, 123)]:
        full_sub_path = os.path.join(module_path, sub)
        os.makedirs(full_sub_path, exist_ok=True)
        for f in files:
            if f.startswith(sub):
                shutil.move(
                    os.path.join(module_path, f),
                    os.path.join(full_sub_path, f),
                )

    # for f in files:
    # print(files)


if __name__ == '__main__':
    split_modules_by_name()
