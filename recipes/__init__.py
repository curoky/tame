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
import shutil
from dataclasses import dataclass

import git
import jinja2

RECIPES_PATH = os.path.dirname(os.path.abspath(__file__))


@dataclass
class GitOption:
    url: str
    branch: str = None
    commit: str = None


@dataclass
class CmakeOption:
    key: str
    value: str = None
    type: str = 'BOOL'
    mode: str = 'CACHE'  # OR NORMAL


@dataclass
class CmakeTargetPropertie:
    key: str
    value: str


@dataclass
class AssetsFile:
    filename: str
    from_path: str = None
    copy_to: str = '.'


class CmakeRecipe(object):

    def __init__(self,
                 name,
                 git_options,
                 include_dirs,
                 link_libraries=[],
                 patches=[],
                 assets=[],
                 cmake_path='.',
                 cmake_options=[],
                 cmake_target_properties=[],
                 cmake_extras='',
                 header_only=False):
        super().__init__()
        self.name = name
        self.git_options = git_options
        self.include_dirs = include_dirs
        self.link_libraries = link_libraries

        self.patches = patches
        self.assets = assets

        self.cmake_path = cmake_path
        self.cmake_options = cmake_options
        self.cmake_target_properties = cmake_target_properties
        self.cmake_extras = cmake_extras
        self.header_only = header_only
        self.logger = logging.getLogger(name)

    def init_root_path(self, root):
        root = os.path.join(root, self.name)

        # root
        #  |- name
        #  |- cpm.cmake
        self.source_path = os.path.join(root, self.name)
        self.cmake_path = os.path.normpath(os.path.join(self.source_path, self.cmake_path))
        self.gen_path = os.path.join(root, 'cpm.cmake')

        include_dirs = self.include_dirs
        self.include_dirs = []
        for inc in include_dirs:
            if inc.startswith('@'):
                inc = inc[1:]
                self.include_dirs.append(
                    os.path.normpath(os.path.join('${CMAKE_BINARY_DIR}', 'cpm', self.name, inc)))
            else:
                self.include_dirs.append(os.path.normpath(os.path.join(self.source_path, inc)))

    def download(self, clear=False):
        self.logger.info('fetch to %s', self.source_path)
        if clear:
            shutil.rmtree(self.source_path, ignore_errors=True)
        try:
            if os.path.exists(self.source_path):
                repo = git.Repo(self.source_path)
            else:
                repo = git.Repo.clone_from(self.git_options.url,
                                           branch=self.git_options.branch,
                                           to_path=self.source_path,
                                           depth=1)
            repo.git.reset('--hard')
            repo.git.clean('-df')
            repo.git.checkout('.')

            if self.git_options.commit:
                repo.git.fetch('origin', '{}'.format(self.git_options.commit))
                repo.git.reset('--hard', '{}'.format(self.git_options.commit))

            logging.info('downlaod to %s, %s', self.source_path, repo.active_branch)
        except Exception as e:
            logging.error(str(e))

    def copy_assets(self):
        assets = self.assets
        self.assets = []
        assets_root = os.path.join(RECIPES_PATH, self.name, 'latest', 'assets')
        for asset in assets:
            asset.from_path = os.path.join(assets_root, asset.filename)
            asset.copy_to = os.path.normpath(
                os.path.join(self.source_path, asset.copy_to, asset.filename))
            if os.path.exists(asset.from_path):
                self.assets.append(asset)

        for asset in self.assets:
            shutil.copyfile(asset.from_path, asset.copy_to)

    def apply_patch(self):
        patches = self.patches
        self.patches = []
        patch_root = os.path.join(RECIPES_PATH, self.name, 'latest', 'patch')
        for patch in patches:
            patch_path = os.path.join(patch_root, patch)
            if os.path.exists(patch_path):
                self.patches.append(patch_path)

        repo = git.Repo(self.source_path)
        for patch in self.patches:
            self.logger.info('apply patch %s', patch)
            repo.git.apply(patch)

    def generate(self, template):
        render_content = template.render(
            name=self.name,
            include_dirs=self.include_dirs,
            link_libraries=self.link_libraries,
            cmake_path=self.cmake_path,
            cmake_options=self.cmake_options,
            cmake_target_properties=self.cmake_target_properties,
            cmake_extras=self.cmake_extras,
            header_only=self.header_only,
        )
        if render_content:
            with codecs.open(self.gen_path, 'w', 'utf8') as f:
                f.write(render_content)

        self.logger.info('generate to %s', self.gen_path)


class RecipesManeger(object):
    recipe_list = dict()

    def __init__(self):
        super().__init__()

        self.recipes = []
        for dir in os.listdir(RECIPES_PATH):
            recipe_path = os.path.join(RECIPES_PATH, dir, 'latest/cpmfile.py')
            if os.path.exists(recipe_path):
                exec(open(recipe_path).read())

    def get_recipe(self, name):
        return self.recipe_list[name]


def add_cmake_recipe(
    name,
    git_options,
    include_dirs,
    link_libraries=[],
    patches=[],
    assets=[],
    cmake_path='.',
    cmake_options=[],
    cmake_target_properties=[],
    cmake_extras='',
    header_only=False,
):
    RecipesManeger.recipe_list[name] = CmakeRecipe(
        name=name,
        git_options=git_options,
        include_dirs=include_dirs,
        link_libraries=link_libraries,
        patches=patches,
        assets=assets,
        cmake_path=cmake_path,
        cmake_options=cmake_options,
        cmake_target_properties=cmake_target_properties,
        cmake_extras=cmake_extras,
        header_only=header_only,
    )
