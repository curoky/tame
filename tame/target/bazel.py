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
from pathlib import Path
from typing import Dict

import giturlparse
import jinja2

from tame.model import Recipe


class Bazel:
    TPL_git_repository: jinja2.Template = jinja2.Template('''
    git_repository(
        name={{ name }},
        tag = "{{ tag }}",
        remote = "{{ remote }}",
    )
    ''')
    TPL_new_git_repository: jinja2.Template = jinja2.Template('''
    new_git_repository(
        name="{{ name }}",
        remote = "{{ remote }}",
        build_file = "{{ build_file }}",
        tag = "{{ tag }}",
    )
    ''')

    TPL_http_archive: jinja2.Template = jinja2.Template('''
    http_archive(
        name = "{{ name }}",
        urls = ["{{ url }}"],
        strip_prefix = "{{ strip_prefix }}",
        {% if build_file %}
        build_file = "{{ build_file }}",
        {% endif %}
        {% if patch_files %}
        patch_args = ["-p1"],
        patches = [
            {{ patch_files|join(",\n            ") }}
        ],
        {% endif %}
        {% if patch_cmds %}
        patch_cmds = [
            {{ patch_cmds|join(",\n            ") }}
        ],
        {% endif %}
    )
    ''')

    def __init__(self, recipes: Dict[str, Recipe]) -> None:
        self.recipes = recipes
        self.logger = logging.getLogger(__class__.__name__)

    def generate(self, output: Path):
        buf = io.StringIO()
        buf.write('''
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
def pkg_rules_dependencies():
        ''')
        for _, r in self.recipes.items():
            for t in r.target:
                self.logger.info(f'generate {r.meta.name}')
                if t.type == 'bazel':
                    name = t.bazel_name or t.retriever.url.replace(
                        'https://github.com/', 'com_github_').replace('/', '_').replace(
                            '-', '_').lower()

                    patch_files = []
                    patch_cmds = []
                    if t.retriever.patch:
                        if t.retriever.patch.type == 'file':
                            patch_files = map(
                                lambda f: f'"@com_curoky_rules_pkg//:recipes/{r.meta.name}/{f}"',
                                t.retriever.patch.file,
                            )
                        elif t.retriever.patch.type == 'cmd':
                            patch_cmds = map(
                                lambda f: f'"{f}"',
                                t.retriever.patch.cmd,
                            )

                    if t.bazel_type == 'new_git_repository':
                        # self.TPL_new_git_repository.render(
                        #     name=r.meta.name,
                        #     remote=t.retriever.url,
                        #     build_file='',
                        #     tag=t.retriever.ref,
                        # )

                        git = giturlparse.parse(t.retriever.url)

                        buf.write(
                            self.TPL_http_archive.render(
                                name=name,
                                url=f'{git.url2https[:-4]}/archive/refs/{t.retriever.ref}.tar.gz',
                                build_file=
                                f'@com_curoky_rules_pkg//:recipes/{r.meta.name}/{t.bazel_build}',
                                strip_prefix=
                                f'{git.name}-{t.retriever.ref.split("/")[1].removeprefix("v")}',
                                patch_files=patch_files,
                                patch_cmds=patch_cmds,
                            ))

                    elif t.bazel_type == 'git_repository':
                        git = giturlparse.parse(t.retriever.url)
                        buf.write(
                            self.TPL_http_archive.render(
                                name=name,
                                url=f'{git.url2https[:-4]}/archive/refs/{t.retriever.ref}.tar.gz',
                                strip_prefix=
                                f'{git.name}-{t.retriever.ref.split("/")[1].removeprefix("v")}',
                                patch_files=patch_files,
                                patch_cmds=patch_cmds,
                            ))
                    elif t.bazel_type == 'http_archive':
                        buf.write(
                            self.TPL_http_archive.render(
                                name=t.bazel_name,
                                url=t.retriever.url,
                                build_file=
                                f'@com_curoky_rules_pkg//:recipes/{r.meta.name}/{t.bazel_build}',
                                strip_prefix=t.bazel_strip_prefix,
                                patch_files=patch_files,
                                patch_cmds=patch_cmds,
                            ))

        output.write_text(buf.getvalue())
