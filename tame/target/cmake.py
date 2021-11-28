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

import io
import logging
import os
from pathlib import Path
from typing import Dict

import giturlparse
import jinja2
from cmakelang import configuration
from cmakelang.format import __main__ as format_main

from tame.model import Recipe


class Cmake:
    TPL: jinja2.Template = jinja2.Template('''
CPMAddPackage(
  NAME {{ name }}
  GITHUB_REPOSITORY {{ repo_path }}
  GIT_TAG {{ tag }}
  OPTIONS
    "CMAKE_BUILD_TYPE Debug"
    {% for opt in option %}
    "{{ opt }}"
    {%- endfor %}
  )
''')

    def __init__(self, recipes: Dict[str, Recipe]) -> None:
        self.recipes = recipes
        self.logger = logging.getLogger(__class__.__name__)

    def generate(self, output: Path):
        buf = io.StringIO()
        for _, r in self.recipes.items():
            for t in r.target:
                if t.type == 'cmake':
                    self.logger.info(f'generate {r.meta.name}')
                    git = giturlparse.parse(t.retriever.url)
                    buf.write(
                        self.TPL.render(
                            name=t.cpm_name or r.meta.name.replace('-', '_'),
                            repo_path=f'{git.owner}/{git.name}',
                            tag=t.retriever.ref.split('/')[1],
                            option=t.option,
                        ))

        content, _ = format_main.process_file(
            config=configuration.Configuration(**format_main.get_config(os.getcwd(), None)),
            infile_content=buf.getvalue())
        output.write_text(content)
