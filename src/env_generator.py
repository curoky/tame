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

import codecs
import os


class EnvGenerator(object):

    def __init__(self, root):
        self.root = root
        self.install_path = os.path.join(self.root, 'install')
        self.env_file_path = os.path.join(self.root, 'main.sh')
        self.cmake_file_path = os.path.join(self.root, 'FindCmakePrefixConfig.cmake')

    @staticmethod
    def collect_install_dirs(self, path):
        install_dirs = set()
        for p in os.listdir(path):
            full_path = (os.path.join(path, p))
            if os.path.isdir(full_path):
                install_dirs.add(full_path)
        return install_dirs

    def gen(self):
        install_dirs = self.collect_install_dirs()
        bin_name_list = set()
        lib_name_list = set()
        for p in install_dirs:
            bin_path = os.path.join(p, 'bin')
            lib_path = os.path.join(p, 'lib')
            if os.path.exists(bin_path):
                bin_name_list.add(os.path.basename(p))
            if os.path.exists(lib_path):
                lib_name_list.add(os.path.basename(p))

        with codecs.open(self.env_file_path, 'w', 'utf8') as f:
            f.write("""
#!/usr/bin/env bash
CHAFER_INSTALL_DIR=$(cd "$(dirname "$0")" && pwd)/install

tools_bin_list=(
""")
            for p in bin_name_list:
                f.write("    '%s'\n" % p)
            f.write("""
)
for item in ${tools_bin_list[@]}; do
    export PATH="${CHAFER_INSTALL_DIR}/${item}/bin:$PATH"
done

tools_lib_list=(
""")
            for p in lib_name_list:
                f.write("    '%s'\n" % p)
            f.write("""
)
for item in ${tools_lib_list[@]}; do
    export LD_LIBRARY_PATH="${CHAFER_INSTALL_DIR}/${item}/lib:${CHAFER_INSTALL_DIR}/${item}/lib64:$LD_LIBRARY_PATH"
done
export DYLD_LIBRARY_PATH=${LD_LIBRARY_PATH}
""")

        with codecs.open(self.cmake_file_path, 'w', 'utf8') as f:
            f.write('set(CmakePrefixConfig_FOUND TRUE)\n\n')
            for p in lib_name_list:
                f.write('list(APPEND CMAKE_PREFIX_PATH %s)\n' % os.path.join(self.install_path, p))
            f.write('\n')
