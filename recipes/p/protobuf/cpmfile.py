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

from cpm.recipes import CmakeOption, GitOption, add_cmake_recipe

add_cmake_recipe(
    name='protobuf',
    git_options=GitOption(url='https://github.com/protocolbuffers/protobuf',),
    include_dirs=[
        'src',
    ],
    cmake_path='cmake',
    cmake_options=[
        CmakeOption(key='protobuf_MSVC_STATIC_RUNTIME', value='OFF'),
        CmakeOption(key='protobuf_BUILD_TESTS', value='OFF'),
        CmakeOption(key='protobuf_WITH_ZLIB', value='ON'),
    ],
    link_libraries=['libprotobuf'],
)
