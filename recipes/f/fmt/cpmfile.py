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
    name='fmt',
    git_options=GitOption(url='https://github.com/fmtlib/fmt',),
    include_dirs=[
        'include',
    ],
    cmake_options=[
        CmakeOption(key='FMT_DOC', value='OFF'),
        CmakeOption(key='FMT_TEST', value='OFF'),
        CmakeOption(key='FMT_TEST', value='OFF'),
    ],
    patches=[
        '0001-enable-master-project.patch',
    ],
    link_libraries=[
        'fmt',
    ],
)
