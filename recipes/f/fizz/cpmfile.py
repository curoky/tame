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
    name='fizz',
    git_options=GitOption(url='https://github.com/facebookincubator/fizz',),
    include_dirs=[
        '.',
    ],
    link_libraries=['fizz'],
    cmake_path='fizz',
    cmake_options=[
        CmakeOption(key='BUILD_TESTS', value='OFF'),
        CmakeOption(key='BUILD_EXAMPLES', value='OFF'),
    ],
    cmake_extras='''
target_include_directories(fizz
  PUBLIC
    $<BUILD_INTERFACE:${CPM_SOURCE_DIR}/fizz/fizz>
  PRIVATE
    ${CPM_SOURCE_DIR}/folly/folly
    ${CPM_BINARY_DIR}/folly
    ${CPM_BINARY_DIR}/glog
    ${CPM_SOURCE_DIR}/glog/glog/src
    ${CPM_BINARY_DIR}/gflags/include
    ${CPM_SOURCE_DIR}/double-conversion/double-conversion
)
target_link_libraries(fizz
  PRIVATE
    folly
)

add_library(fizz::fizz ALIAS fizz)
''',
)
