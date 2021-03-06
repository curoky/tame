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
    name='czmq',
    git_options=GitOption(url='https://github.com/zeromq/czmq',),
    include_dirs=[
        'include',
    ],
    # link_libraries=['czmq::czmq'],
    cmake_options=[
        CmakeOption(key='ENABLE_DRAFTS', value='OFF'),
        CmakeOption(key='LIBZMQ_FOUND', value='ON'),
        CmakeOption(key='LIBZMQ_LIBRARIES', value='libzmq-static', mode='NORMAL'),
    ],
    cmake_extras='''
target_include_directories(czmq_objects
  PRIVATE
    $<BUILD_INTERFACE:${CPM_SOURCE_DIR}/libzmq/libzmq/include>
)
target_include_directories(zmakecert
  PRIVATE
    $<BUILD_INTERFACE:${CPM_SOURCE_DIR}/libzmq/libzmq/include>
)
target_include_directories(czmq_selftest
  PRIVATE
    $<BUILD_INTERFACE:${CPM_SOURCE_DIR}/libzmq/libzmq/include>
)
''',
)
