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
import concurrent.futures
import os
import sys
from sys import version

import jinja2
from conans.client.output import ConanOutput, colorama_initialize

from cpm.recipes import RECIPES_PATH, RecipesManeger
from cpm.template import TEMPLATE_PATH


class CpmApp(object):

    def __init__(self):
        super().__init__()

        self.prefix = os.path.join(os.getcwd(), 'cpm')
        self.recipes_manager = RecipesManeger()

        with codecs.open(os.path.join(TEMPLATE_PATH, 'cmake.recipe.j2'), 'r', 'utf8') as f:
            self.cmake_recipe_template = jinja2.Template(f.read())
        with codecs.open(os.path.join(TEMPLATE_PATH, 'cmake.config.j2'), 'r', 'utf8') as f:
            self.cmake_config_template = jinja2.Template(f.read())
        with codecs.open(os.path.join(TEMPLATE_PATH, 'cpmfile.j2'), 'r', 'utf8') as f:
            self.cpmfile_template = jinja2.Template(f.read())
        self.cmake_config_path = os.path.join(self.prefix, 'cpm_config.cmake')


class Cpm(object):

    @classmethod
    def factory(cls):
        return cls(), None, None

    def __init__(self, output=None):
        self.app = CpmApp()
        self.color = colorama_initialize()
        self.out = output or ConanOutput(sys.stdout, sys.stderr, self.color)

    def list(self):
        result = sorted(self.app.recipes_manager.recipe_list.keys())
        for r in result:
            print('include(cpm/{}/cpm.cmake)'.format(r))

    def _gen_cmake_config(self):
        config = self.app.cmake_config_template.render(
            cpm_source_dir=self.app.prefix,
            cpm_binary_dir='${CMAKE_BINARY_DIR}/cpm',
        )
        with codecs.open(self.app.cmake_config_path, 'w', 'utf8') as f:
            f.write(config)

    def _install_one(self, recipe):
        recipe.set_root_path(self.app.prefix)
        recipe.download()
        recipe.apply_patch()
        recipe.copy_assets()
        recipe.generate(self.app.cmake_recipe_template)

    def install(self, name, requirement):
        if name and name != 'all':
            self._install_one(name)
        elif requirement:
            if not os.path.isfile(requirement):
                self.out.error('file {} not exits'.format(requirement))
                return
            names = set(self.app.recipes_manager.recipe_list.keys())
            recipes = []
            lines = []
            with codecs.open(requirement, 'r', 'utf8') as f:
                lines = f.readlines()
            self.out.info('install package {}'.format(len(lines)))
            for line in lines:
                name, commit = line.split('==')
                commit = commit.strip()
                if name in names:
                    recipe = self.app.recipes_manager.get_recipe(name)
                    recipe.git_options.commit = commit
                    recipes.append(recipe)
            with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
                executor.map(self._install_one, recipes)
        else:
            names = self.app.recipes_manager.recipe_list.keys()
            recipes = [self.app.recipes_manager.get_recipe(name) for name in names]
            with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
                executor.map(self._install_one, recipes)
        self._gen_cmake_config()

    def create(self, name, github_path):
        recipe_dir = os.path.join(RECIPES_PATH, name, 'latest')
        os.makedirs(recipe_dir, exist_ok=True)
        recipe_path = os.path.join(recipe_dir, 'cpmfile.py')
        with codecs.open(recipe_path, 'w', 'utf8') as f:
            url = 'https://github.com/{}'.format(github_path)
            f.write(self.app.cpmfile_template.render(name=name, url=url))

    def freeze(self, path):
        names = self.app.recipes_manager.recipe_list.keys()
        versions = []
        for name in names:
            recipe = self.app.recipes_manager.get_recipe(name)
            recipe.set_root_path(self.app.prefix)
            commit = recipe.freeze()
            if commit:
                versions.append([name, commit])
                self.out.info('freeze {} -> {}'.format(name, commit))
        with codecs.open(path, 'w', 'utf8') as f:
            for v in versions:
                f.write('{name}=={commit}\n'.format(name=v[0], commit=v[1]))
