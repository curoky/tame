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
from typing import Dict, List, Literal, Optional, Union

import pydantic
import pydantic_yaml
from typing_extensions import Annotated


class Recipe(pydantic_yaml.YamlModel):

    class Meta(pydantic_yaml.YamlModel):
        name: str = ''
        homepage: Optional[pydantic.HttpUrl]
        descrition: Optional[str]
        license: Optional[str]
        _related_path: Path = pydantic.PrivateAttr()

    meta: Meta = pydantic.Field(default=Meta.construct())

    depend: Optional[List[str]]

    class FilePatch(pydantic_yaml.YamlModel):
        type: Literal['file']
        file: List[str]

    class CmdPatch(pydantic_yaml.YamlModel):
        type: Literal['cmd']
        cmd: List[str]

    _Patch: Annotated = Annotated[Union[FilePatch, CmdPatch], pydantic.Field(discriminator='type')]

    class HttpRetriever(pydantic_yaml.YamlModel):
        type: Literal['http']
        url: pydantic.HttpUrl
        patch: Optional['Recipe._Patch']

    class GitRetriever(pydantic_yaml.YamlModel):
        type: Literal['git']
        url: str
        ref: str
        patch: Optional['Recipe._Patch']

    _Retriever = Annotated[Union[HttpRetriever, GitRetriever], pydantic.Field(discriminator='type')]

    class CMakeBuildTool(pydantic_yaml.YamlModel):
        type: Literal['cmake']

    class MakeBuildTool(pydantic_yaml.YamlModel):
        type: Literal['make']

    class PerlBuildTool(pydantic_yaml.YamlModel):
        type: Literal['perl']

    class NinjaBuildTool(pydantic_yaml.YamlModel):
        type: Literal['ninja']

    class ConfigureBuildTool(pydantic_yaml.YamlModel):
        type: Literal['configure']

    _BuildTool = Annotated[Union[CMakeBuildTool, MakeBuildTool, NinjaBuildTool, PerlBuildTool,
                                 ConfigureBuildTool],
                           pydantic.Field(discriminator='type')]

    class BuildTarget(pydantic_yaml.YamlModel):
        type: Literal['build']
        # option: Dict[str, str]
        retriever: 'Recipe._Retriever'
        tool: 'Recipe._BuildTool'

    class BazelTarget(pydantic_yaml.YamlModel):
        type: Literal['bazel']
        bazel_type: str
        bazel_name: Optional[str]
        bazel_build: Optional[str]
        bazel_strip_prefix: Optional[str]

        retriever: 'Recipe._Retriever'

    class CmakeTarget(pydantic_yaml.YamlModel):
        type: Literal['cmake']
        cpm_name: Optional[str]
        option: List[str] = pydantic.Field(default=[])

        retriever: 'Recipe._Retriever'

    _Target: Optional[Annotated] = Annotated[Union[BuildTarget, BazelTarget, CmakeTarget],
                                             pydantic.Field(discriminator='type')]

    target: List[_Target]

    @staticmethod
    def loads(path: Path) -> dict[str, 'Recipe']:
        recipes = {}

        for file in sorted(path.glob('**/**/index.yaml')):
            try:
                r = Recipe.parse_raw(file.read_text())
                r.meta.name = r.meta.name or file.parent.stem
                r.meta._related_path = file.parent.relative_to(path.parent)
                recipes[r.meta.name] = r
            except Exception as e:
                logging.error(f'parse {file} failed: {e}')
                raise e

        return recipes


Recipe.BazelTarget.update_forward_refs()
Recipe.CmakeTarget.update_forward_refs()
Recipe.BuildTarget.update_forward_refs()
Recipe.HttpRetriever.update_forward_refs()
Recipe.GitRetriever.update_forward_refs()
Recipe.NinjaBuildTool.update_forward_refs()
Recipe.CMakeBuildTool.update_forward_refs()
Recipe.PerlBuildTool.update_forward_refs()
Recipe.ConfigureBuildTool.update_forward_refs()
Recipe.MakeBuildTool.update_forward_refs()
