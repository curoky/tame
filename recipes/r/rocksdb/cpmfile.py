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
    name='rocksdb',
    git_options=GitOption(url='https://github.com/facebook/rocksdb',),
    include_dirs=[
        'include',
    ],
    # link_libraries=['rocksdb'],
    cmake_options=[
        CmakeOption(key='WITH_JEMALLOC', value='OFF'),
        CmakeOption(key='WITH_SNAPPY', value='OFF'),
        CmakeOption(key='WITH_LZ4', value='OFF'),
        CmakeOption(key='WITH_ZLIB', value='OFF'),
        CmakeOption(key='WITH_ZSTD', value='OFF'),
        CmakeOption(key='WITH_TBB', value='OFF'),
        CmakeOption(key='WITH_GFLAGS', value='OFF'),
        CmakeOption(key='WITH_FOLLY_DISTRIBUTED_MUTEX', value='OFF'),
        CmakeOption(key='WITH_TESTS', value='OFF'),
        CmakeOption(key='WITH_TOOLS', value='OFF'),
        CmakeOption(key='WITH_CORE_TOOLS', value='OFF'),
        CmakeOption(key='WITH_BENCHMARK_TOOLS', value='OFF'),
        # if PORTABLE OFF, -march=native will be added to gcc flags,
        # then distcc will not work
        CmakeOption(key='PORTABLE', value='ON'),
    ],
    cmake_extras='''
    set_property(GLOBAL PROPERTY RULE_LAUNCH_COMPILE "")
    set_property(GLOBAL PROPERTY RULE_LAUNCH_LINK "")
''',
)
