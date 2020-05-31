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
    name='curl',
    git_options=GitOption(url='https://github.com/curl/curl',),
    include_dirs=[
        'include',
    ],
    cmake_options=[
        CmakeOption(key='ENABLE_DEBUG', value='ON'),
        CmakeOption(key='ENABLE_CURLDEBUG', value='ON'),
        CmakeOption(key='BUILD_TESTING', value='OFF'),
        CmakeOption(key='BUILD_CURL_EXE', value='OFF'),
        CmakeOption(key='ENABLE_MANUAL', value='OFF'),
    ],
    link_libraries=['libcurl'],
)
