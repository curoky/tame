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

import logging
from pathlib import Path

import typer

from tame.model import Recipe
from tame.target.bazel import Bazel
from tame.target.cmake import Cmake

RECIPES_PATH = Path.cwd() / 'recipes'

app = typer.Typer()


@app.command()
def bazel(out: Path = typer.Option(Path('./bazel/recipes.bzl'), help='output directory'),):
    recipes = Recipe.loads(RECIPES_PATH)
    bazel = Bazel(recipes=recipes)
    bazel.generate(out.expanduser())
    logging.info(f'success to generate recipes, size:{len(recipes)}')


@app.command()
def cmake(out: Path = typer.Option(Path('./cmake/recipes.cmake'), help='output directory'),):
    recipes = Recipe.loads(RECIPES_PATH)
    cmake = Cmake(recipes=recipes)
    cmake.generate(out.expanduser())
    logging.info(f'success to generate recipes, size:{len(recipes)}')


@app.command()
def show(recipe: str):
    pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app()
