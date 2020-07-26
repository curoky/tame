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
    name='wangle',
    git_options=GitOption(url='https://github.com/facebook/wangle',),
    include_dirs=[
        '.',
    ],
    link_libraries=['wangle'],
    cmake_path='wangle',
    cmake_options=[
        CmakeOption(key='BUILD_TESTS', value='OFF'),
    ],
    cmake_extras='''
target_include_directories(wangle
  PUBLIC
    $<BUILD_INTERFACE:${CPM_SOURCE_DIR}/wangle/wangle>
  PRIVATE
    ${CPM_SOURCE_DIR}/double-conversion/double-conversion
    ${CPM_SOURCE_DIR}/fizz/fizz
    ${CPM_SOURCE_DIR}/folly/folly
    ${CPM_BINARY_DIR}/folly
    ${CPM_BINARY_DIR}/glog
    ${CPM_SOURCE_DIR}/glog/glog/src
    ${CPM_BINARY_DIR}/gflags/include
    ${CPM_SOURCE_DIR}/libevent/libevent/include
    ${CPM_BINARY_DIR}/libevent/include
)
target_link_libraries(wangle
  PUBLIC
    fizz
    gflags_nothreads_static
)
add_library(wangle::wangle ALIAS wangle)
''',
)
