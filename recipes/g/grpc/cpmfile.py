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
    name='grpc',
    git_options=GitOption(url='https://github.com/grpc/grpc',),
    include_dirs=[
        '.',
    ],
    link_libraries=[
        'grpc',
        'grpc++',
    ],
    cmake_options=[
        CmakeOption(key='gRPC_BUILD_TESTS', value='OFF'),
        CmakeOption(key='gRPC_BUILD_CSHARP_EXT', value='OFF'),
        CmakeOption(key='gRPC_BUILD_GRPC_CSHARP_PLUGIN', value='OFF'),
        CmakeOption(key='gRPC_BUILD_GRPC_NODE_PLUGIN', value='OFF'),
        CmakeOption(key='gRPC_BUILD_GRPC_OBJECTIVE_C_PLUGIN', value='OFF'),
        CmakeOption(key='gRPC_BUILD_GRPC_PHP_PLUGIN', value='OFF'),
        CmakeOption(key='gRPC_BUILD_GRPC_PYTHON_PLUGIN', value='OFF'),
        CmakeOption(key='gRPC_BUILD_GRPC_RUBY_PLUGIN', value='OFF'),
        CmakeOption(key='gRPC_ZLIB_PROVIDER', value='package', type='STRING'),
        CmakeOption(key='gRPC_SSL_PROVIDER', value='package', type='STRING'),
        CmakeOption(key='gRPC_CARES_PROVIDER', value='package', type='STRING'),
        CmakeOption(key='gRPC_PROTOBUF_PROVIDER', value='none', type='STRING'),
        CmakeOption(key='gRPC_RE2_PROVIDER', value='none', type='STRING'),
        CmakeOption(key='_gRPC_RE2_LIBRARIES', value='re2::re2', mode='NORMAL'),
        CmakeOption(key='_gRPC_RE2_INCLUDE_DIR', value='${CPM_SOURCE_DIR}/re2/re2', mode='NORMAL'),
        CmakeOption(key='gRPC_ABSL_PROVIDER', value='none', type='STRING'),
        CmakeOption(key='gRPC_BENCHMARK_PROVIDER', value='none', type='STRING'),
        CmakeOption(key='gRPC_GFLAGS_PROVIDER', value='none', type='STRING'),
        CmakeOption(key='_gRPC_PROTOBUF_PROTOC_EXECUTABLE',
                    value='$<TARGET_FILE:protoc>',
                    mode='NORMAL'),
        CmakeOption(key='_gRPC_PROTOBUF_LIBRARIES', value='libprotobuf libprotoc', mode='NORMAL'),
        CmakeOption(key='_gRPC_PROTOBUF_PROTOC', value='protoc', mode='NORMAL'),
        CmakeOption(key='_gRPC_PROTOBUF_WELLKNOWN_INCLUDE_DIR',
                    value='${CPM_SOURCE_DIR}/protobuf/protobuf/src',
                    mode='NORMAL'),
    ],
)
