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

from .builder import Builder, BuilderOptions
from .make_builder import MakeBuilder
from .cmake_builder import CmakeBuilder
from .configure_builder import ConfigureBuilder
from .custom_builder import CustomBuilder
from .perl_builder import PerlBuilder
from .ninja_builder import NinjaBuilder


class BuilderFactory(object):
    builder_map = {
        'make': MakeBuilder,
        'cmake': CmakeBuilder,
        'perl': PerlBuilder,
        'ninja': NinjaBuilder,
        'configure': ConfigureBuilder,
        'custom': CustomBuilder,
    }

    @staticmethod
    def create(name, options):
        if name not in BuilderFactory.builder_map:
            logging.critical('unsupport Builder type %s ', name)
        return BuilderFactory.builder_map[name](options)
