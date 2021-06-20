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

from pathlib import Path


def main():
    recipes_path: Path = Path(__file__).parent.parent / 'recipes'
    configs_path = recipes_path / 'configs.bzl'
    lines = []
    map_lines = []
    for f in sorted(recipes_path.glob('**/config.bzl')):
        sub_path = f.parent.relative_to(recipes_path)
        name = sub_path.name.replace('-', '_')
        print(f.parent.relative_to(recipes_path))

        lines.append(
            f'load("@com_curoky_tame//:recipes/{sub_path}/config.bzl", {name}_config = "config")'
        )
        map_lines.append(f'"{sub_path}": {name}_config,')
    lines.append('configs = {')
    lines += map_lines
    lines.append('}')
    configs_path.write_text('\n'.join(lines))


if __name__ == '__main__':
    main()
