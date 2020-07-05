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
    name='llvm',
    git_options=GitOption(url='https://github.com/llvm/llvm-project',),
    include_dirs=[
        'llvm/include',
    ],
    cmake_path='llvm',
    cmake_options=[
        CmakeOption(key='LLVM_INCLUDE_TESTS', value='OFF'),
        CmakeOption(key='LLVM_INCLUDE_GO_TESTS', value='OFF'),
        CmakeOption(key='LLVM_INCLUDE_DOCS', value='OFF'),
        CmakeOption(key='LLVM_ENABLE_OCAMLDOC', value='OFF'),
        CmakeOption(key='LLVM_BUILD_BENCHMARKS', value='OFF'),
        CmakeOption(key='LLVM_INCLUDE_BENCHMARKS', value='OFF'),
        CmakeOption(key='LLVM_INCLUDE_EXAMPLES', value='OFF'),
        # The target `AVR' is experimental and must be passed via LLVM_EXPERIMENTAL_TARGETS_TO_BUILD.
        CmakeOption(key='LLVM_EXPERIMENTAL_TARGETS_TO_BUILD', value='AVR', type='STRING'),
    ],
    # link_libraries=['llvm'],
)
