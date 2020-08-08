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
    name='libevent',
    git_options=GitOption(url='https://github.com/libevent/libevent',),
    include_dirs=[
        'include',
    ],
    # link_libraries=['libevent::libevent'],
    cmake_options=[
        CmakeOption(key='EVENT__DISABLE_TESTS', value='ON'),
        CmakeOption(key='EVENT__DISABLE_BENCHMARK', value='ON'),
        CmakeOption(key='EVENT__DISABLE_SAMPLES', value='ON'),
        CmakeOption(key='EVENT__ENABLE_VERBOSE_DEBUG', value='ON'),
    ],
    cmake_extras='''
#TODO: export event_static/event_shared
#export(TARGETS "event_shared"
#    NAMESPACE ""
#    FILE "${PROJECT_BINARY_DIR}/LibeventTargets-${TYPE}.cmake"
#    APPEND
#)
''')
