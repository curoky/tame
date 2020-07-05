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
    name="fbthrift",
    git_options=GitOption(url="https://github.com/facebook/fbthrift",),
    include_dirs=[
        '.',
        '@.',
    ],
    link_libraries=[
        "async",
        "concurrency",
        "protocol",
        "thrift-core",
        "transport",
        "thriftcpp2",
        "thriftfrozen2",
        "thriftmetadata",
        "thriftprotocol",
        "thrift2",
        "compiler_ast",
        "compiler_lib",
        "mustache_lib",
        "compiler_base",
        "compiler_generators",
        "compiler_generate_templates",
    ],
    patches=['master.patch'],
    cmake_options=[
        CmakeOption(key='Boost_INCLUDE_DIRS',
                    value='/opt/vcpkg/installed/x64-linux/include',
                    mode='NORMAL'),
        CmakeOption(
            key='Boost_LIBRARIES',
            value=
            '/opt/vcpkg/installed/x64-linux/lib/libboost_context.a;/opt/vcpkg/installed/x64-linux/lib/libboost_filesystem.a;/opt/vcpkg/installed/x64-linux/lib/libboost_program_options.a;/opt/vcpkg/installed/x64-linux/lib/libboost_regex.a;/opt/vcpkg/installed/x64-linux/lib/libboost_system.a;/opt/vcpkg/installed/x64-linux/lib/libboost_thread.a;-pthread;/opt/vcpkg/installed/x64-linux/lib/libboost_chrono.a;/opt/vcpkg/installed/x64-linux/lib/libboost_date_time.a;/opt/vcpkg/installed/x64-linux/lib/libboost_atomic.a',
            mode='NORMAL'),
        CmakeOption(key='ZSTD_INCLUDE_DIRS', value='/opt/vcpkg/installed/x64-linux/',
                    mode='NORMAL'),
        CmakeOption(key='ZSTD_LIBRARIES',
                    value='/opt/vcpkg/installed/x64-linux/lib/libzstd.a',
                    mode='NORMAL'),
    ],
    cmake_extras='''
target_include_directories(thriftcpp2
  PRIVATE
    ${CPM_SOURCE_DIR}/rsocket/rsocket
    ${CPM_SOURCE_DIR}/fizz/fizz
)
''',
)
