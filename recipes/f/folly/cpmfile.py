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
    name='folly',
    git_options=GitOption(url='https://github.com/facebook/folly',),
    include_dirs=[
        '.',
        '@.',
    ],
    link_libraries=['folly', 'follybenchmark'],
    cmake_options=[
        CmakeOption(key='FOLLY_HAVE_LIBGFLAGS', value='1', mode='NORMAL'),
        CmakeOption(key='FOLLY_HAVE_LIBGLOG', value='1', mode='NORMAL'),
        CmakeOption(key='FOLLY_HAVE_MEMRCHR', value='ON'),
        CmakeOption(key='FOLLY_HAVE_CLOCK_GETTIME', value='ON'),
        CmakeOption(key='FOLLY_HAVE_RECVMMSG', value='ON'),
        CmakeOption(key='LIBGFLAGS_FOUND', value='ON'),
        CmakeOption(key='BUILD_TESTS', value='OFF'),
    ],
    cmake_extras='''
target_include_directories(folly_deps
  INTERFACE
    $<BUILD_INTERFACE:/opt/vcpkg/installed/x64-linux/include>
    $<BUILD_INTERFACE:${CPM_BINARY_DIR}/gflags/include>
    $<BUILD_INTERFACE:${CPM_BINARY_DIR}/glog/glog>
    $<BUILD_INTERFACE:${CPM_SOURCE_DIR}/double-conversion/double-conversion>
    $<BUILD_INTERFACE:/usr/include/libiberty>
)
target_link_libraries(folly_deps
  INTERFACE
    glog
    double-conversion
)
target_link_libraries(logging_example
    glog double-conversion gflags_nothreads_static
)
add_library(Folly::folly ALIAS folly)
''',
)
