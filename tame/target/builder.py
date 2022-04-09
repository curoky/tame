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
'''
layout
root/
    xxx/
        download/
        buildtree/
        installed/
    yyy/
        download/
        buildtree/
        installed/
'''

import logging
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import List

import requests
from pydantic import BaseModel

from tame.model import Recipe


class PathMetaInfo(BaseModel):
    download_path: Path
    buildtree_path: Path
    install_path: Path


def PrepareEnvironment(include_paths):
    env = dict()
    base_path = os.path.expanduser('~/.local/bin') + ':/usr/local/bin:/usr/bin/:/usr/sbin/:/bin'

    env['PATH'] = ':'.join([os.path.join(p, 'bin') for p in include_paths]) + ':' + base_path

    env['PKG_CONFIG_PATH'] = ':'.join([os.path.join(p, 'lib/pkgconfig') for p in include_paths] +
                                      [os.path.join(p, 'share/pkgconfig') for p in include_paths])

    env['LD_LIBRARY_PATH'] = ':'.join([os.path.join(p, 'lib') for p in include_paths])
    env['DYLD_LIBRARY_PATH'] = env['LD_LIBRARY_PATH']
    # Just use for automake
    dep_libs = ''
    dep_incs = ''
    for p in include_paths:
        dep_libs += '-L%s ' % os.path.join(p, 'lib')
        dep_incs += '-I%s ' % os.path.join(p, 'include')
    env['LDFLAGS'] = '%s' % dep_libs
    env['CPPFLAGS'] = '%s' % dep_incs
    env['CFLAGS'] = env['CPPFLAGS']

    env['CXXFLAGS'] = env['CPPFLAGS']
    # for perl
    env['PERL5LIB'] = ':'.join([os.path.join(p, 'lib/perl5') for p in include_paths])
    return env


class Builder:

    def __init__(self, recipe: Recipe):
        self.recipe = recipe

    def exec(self, command: List[str], path: Path):
        logging.info('start to exec: %s', command)
        os.makedirs(path, exist_ok=True)
        res = subprocess.run(
            args=command,
            cwd=path,
            #    env=self.env,
            # shell=True,
            stdout=sys.stdout,
            stderr=sys.stderr)
        # return res.wait()


class CmakeBulder(Builder):

    def build(self, pmi: PathMetaInfo):
        # return 'cmake -B {} -S {} -DCMAKE_PREFIX_PATH="{}" -DCMAKE_INSTALL_PREFIX={} {}'.format(
        #     self.build_path, self.index_path, self.cmake_prefix_path, self.install_path, self.args)
        self.exec([
            'cmake',
            '-B',
            (pmi.buildtree_path / '_build').as_posix(),
            '-S',
            pmi.buildtree_path.as_posix(),
            f'-DCMAKE_INSTALL_PREFIX={pmi.install_path.as_posix()}',
        ], pmi.buildtree_path)
        self.exec(['make', '-j', '90'], pmi.buildtree_path / '_build')
        self.exec(['make', 'install'], pmi.buildtree_path / '_build')


class PerlBuilder(Builder):

    def build(self, pmi: PathMetaInfo):
        self.exec(['perl', 'Makefile.PL', f'INSTALL_BASE={pmi.install_path.as_posix()}'],
                  pmi.buildtree_path)
        self.exec(['make'], pmi.buildtree_path)
        self.exec(['make', 'install'], pmi.buildtree_path)


class MakeBuilder(Builder):

    def build(self, pmi: PathMetaInfo):
        self.exec(['make'], pmi.buildtree_path)
        self.exec(['make', 'install', f'PREFIX={pmi.install_path.as_posix()}'], pmi.buildtree_path)


class ConfigureBuilder(Builder):

    def __init__(self) -> None:
        pass

    def build(self, pmi: PathMetaInfo):
        self.exec(['./configure', '--prefix', pmi.install_path.as_posix()], pmi.buildtree_path)
        self.exec(['make'], pmi.buildtree_path)
        self.exec(['make', 'install'], pmi.buildtree_path)


class Dispatcher:

    def __init__(self, rootPath: Path) -> None:
        self.rootPath = rootPath

    def download(self, target: Recipe.BuildTarget, pmi: PathMetaInfo):
        downloadPath = pmi.download_path / os.path.basename(target.retriever.url)
        downloadPath.write_bytes(requests.get(target.retriever.url).content)
        shutil.rmtree(pmi.buildtree_path, ignore_errors=True)
        shutil.unpack_archive(downloadPath, pmi.buildtree_path)

        # remove leading dir in zip
        for d in pmi.buildtree_path.iterdir():
            for dd in d.iterdir():
                shutil.move(dd, dd.parent.parent / dd.name)

    def build(self, recipe: Recipe):
        t: Recipe.BuildTarget = [t for t in recipe.target if t.type == 'build'][0]
        pmi = PathMetaInfo(install_path=self.rootPath / recipe.meta.name / 'installed',
                           download_path=self.rootPath / recipe.meta.name / 'download',
                           buildtree_path=self.rootPath / recipe.meta.name / 'buildtree')
        os.makedirs(pmi.download_path, exist_ok=True)
        os.makedirs(pmi.buildtree_path, exist_ok=True)
        os.makedirs(pmi.install_path, exist_ok=True)
        self.download(t, pmi)

        if t.tool.type == 'cmake':
            CmakeBulder(recipe).build(pmi)
        elif t.tool.type == 'configure':
            ConfigureBuilder().build(pmi)
        elif t.tool.type == 'make':
            MakeBuilder(recipe).build(pmi)
        elif t.tool.type == 'perl':
            PerlBuilder(recipe).build(pmi)
