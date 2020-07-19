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
    name='brpc',
    git_options=GitOption(url='https://github.com/apache/incubator-brpc',),
    include_dirs=[
        '.',
    ],
    # link_libraries=['brpc'],
    patches=['master.patch'],
    cmake_options=[
        CmakeOption(key='WITH_THRIFT', value='ON'),
        CmakeOption(key='WITH_MESALINK', value='OFF'),
        # CmakeOption(key='WITH_GLOG', value='ON'),
        # CmakeOption(key='GLOG_INCLUDE_PATH', value='${CPM_BINARY_DIR}/glog/glog', mode='NORMAL'),
        # CmakeOption(key='GLOG_LIB', value='glog', mode='NORMAL'),
        CmakeOption(key='PROTOC_LIB', value='libprotoc', mode='NORMAL'),
        CmakeOption(key='PROTOBUF_PROTOC_EXECUTABLE', value='$<TARGET_FILE:protoc>', mode='NORMAL'),
        CmakeOption(key='PROTOBUF_INCLUDE_DIR',
                    value='${CPM_SOURCE_DIR}/protobuf/protobuf/src',
                    mode='NORMAL'),
        CmakeOption(key='PROTOBUF_INCLUDE_DIRS',
                    value='${CPM_SOURCE_DIR}/protobuf/protobuf/src',
                    mode='NORMAL'),
        CmakeOption(key='PROTOBUF_LIBRARIES', value='libprotobuf', mode='NORMAL'),
        CmakeOption(key='LEVELDB_INCLUDE_PATH',
                    value='${CPM_SOURCE_DIR}/leveldb/leveldb/include',
                    mode='NORMAL'),
        CmakeOption(key='LEVELDB_LIB', value='leveldb', mode='NORMAL'),
        CmakeOption(key='GFLAGS_NS', value='gflags', mode='NORMAL'),
        CmakeOption(key='GFLAGS_INCLUDE_PATH',
                    value='${CPM_BINARY_DIR}/gflags/include',
                    mode='NORMAL'),
        CmakeOption(key='GFLAGS_LIBRARY', value='gflags', mode='NORMAL'),
    ],
    cmake_extras='''
target_include_directories(SOURCES_LIB
  PRIVATE
    ${CPM_BINARY_DIR}/thrift
    ${CPM_SOURCE_DIR}/thrift/thrift/lib/cpp/src
    ${CPM_BINARY_DIR}/glog
    ${CPM_SOURCE_DIR}/glog/glog/src
    ${CPM_BINARY_DIR}/gflags/include
)
''')
