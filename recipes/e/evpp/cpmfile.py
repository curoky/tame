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
    name='evpp',
    git_options=GitOption(url='https://github.com/Qihoo360/evpp',),
    include_dirs=[
        '.',
    ],
    link_libraries=['evpp'],
    cmake_options=[
        CmakeOption(key='EVPP_VCPKG_BUILD', value='ON'),
        CmakeOption(key='HTTPS', value='OFF'),
    ],
    cmake_extras='''
target_include_directories(evmc PRIVATE ${TARO_INCLUDE_DIRS})
target_include_directories(evmc_static PRIVATE ${TARO_INCLUDE_DIRS})

target_include_directories(evnsq PRIVATE ${TARO_INCLUDE_DIRS})
target_include_directories(evnsq_static PRIVATE ${TARO_INCLUDE_DIRS})

target_include_directories(evpp PRIVATE ${TARO_INCLUDE_DIRS})
target_include_directories(evpp_static PRIVATE ${TARO_INCLUDE_DIRS})
target_include_directories(evpp_boost PRIVATE ${TARO_INCLUDE_DIRS})
target_include_directories(evpp_boost_static PRIVATE ${TARO_INCLUDE_DIRS})
target_include_directories(evpp_concurrentqueue PRIVATE ${TARO_INCLUDE_DIRS})
target_include_directories(evpp_concurrentqueue_static PRIVATE ${TARO_INCLUDE_DIRS})
target_include_directories(evpp_lite_static PRIVATE ${TARO_INCLUDE_DIRS})
''',
)
