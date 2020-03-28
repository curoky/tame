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
import logging
import os


class EnvHelper(object):

    @staticmethod
    def get_env_from_path(include_paths):
        env = dict()
        base_path = os.path.expanduser('~/.local/bin') + ':/usr/local/bin:/usr/bin/:/usr/sbin/:/bin'

        env['PATH'] = ':'.join([os.path.join(p, 'bin') for p in include_paths]) + ':' + base_path

        env['PKG_CONFIG_PATH'] = ':'.join(
            [os.path.join(p, 'lib/pkgconfig') for p in include_paths] +
            [os.path.join(p, 'share/pkgconfig') for p in include_paths])

        env['LD_LIBRARY_PATH'] = ':'.join([os.path.join(p, 'lib') for p in include_paths])
        env['DYLD_LIBRARY_PATH'] = env['LD_LIBRARY_PATH']
        # Just use for automake
        dep_libs = ''
        dep_incs = ''
        for p in include_paths:
            dep_libs += '-L%s ' % os.path.join(p, 'lib')
            dep_incs += '-I%s ' % os.path.join(p, 'include')
        env['LDFLAGS'] = '%s' % dep_libs
        env['CPPFLAGS'] = '%s' % dep_incs
        env['CFLAGS'] = env['CPPFLAGS']

        env['CXXFLAGS'] = env['CPPFLAGS']
        # for perl
        env['PERL5LIB'] = ':'.join([os.path.join(p, 'lib/perl5') for p in include_paths])

        # if gcc_path:
        #     gcc_path = os.path.expanduser(gcc_path)
        #     env["PATH"] = gcc_path + "/bin:" + env["PATH"]
        #     env["LD_LIBRARY_PATH"] = gcc_path + "/lib:" + env["LD_LIBRARY_PATH"]
        #     env["LD_LIBRARY_PATH"] = gcc_path + "/lib64:" + env[
        #         "LD_LIBRARY_PATH"]

        #     env["CC"] = gcc_path + "/bin/gcc"
        #     env["CXX"] = gcc_path + "/bin/g++"
        return env

    @staticmethod
    def collect_dirs(path) -> [str]:
        dirs = []
        for p in os.listdir(path):
            full_path = (os.path.join(path, p))
            if os.path.isdir(full_path):
                dirs.append(full_path)
        return dirs

    @staticmethod
    def generator_bash_file(path, file):
        dirs = EnvHelper.collect_dirs(path)
        logging.info('collect dirs(%d) in install path %s', len(dirs), path)
        bin_list = []
        lib_list = []
        for d in dirs:
            bin_list.append(os.path.join(d, 'bin'))
            lib_list.append(os.path.join(d, 'lib'))
            lib_list.append(os.path.join(d, 'lib64'))

        with codecs.open(file, 'w', 'utf8') as f:
            f.write('#!/usr/bin/env bash\n')
            f.write('bin_list=(\n')
            for d in bin_list:
                if os.path.isdir(d):
                    f.write("   '%s'\n" % d)
            f.write(')\n\n')
            f.write('for item in ${bin_list[@]}; do export PATH=${item}:$PATH ;done\n')

            f.write('lib_list=(\n')
            for d in lib_list:
                if os.path.isdir(d):
                    f.write("   '%s'\n" % d)
            f.write(')\n\n')
            f.write(
                'for item in ${lib_list[@]}; do export LD_LIBRARY_PATH=${item}:$LD_LIBRARY_PATH ;done\n'
            )
            f.write('export DYLD_LIBRARY_PATH=${LD_LIBRARY_PATH}\n')

            f.write('perl_lib_list=(\n')
            for d in lib_list:
                dd = os.path.join(d, 'perl5')
                if os.path.isdir(dd):
                    f.write("   '%s'\n" % dd)
            f.write(')\n\n')
            f.write('for item in ${perl_lib_list[@]}; do export PERL5LIB=${item}:$PERL5LIB ;done\n')

    @staticmethod
    def generator_cmake_file(path, file):
        dirs = EnvHelper.collect_dirs(path)
        with codecs.open(file, 'w', 'utf8') as f:
            f.write('set(CmakePrefixConfig_FOUND TRUE)\n\n')
            for d in dirs:
                f.write('list(APPEND CMAKE_PREFIX_PATH %s)\n' % d)
            f.write('\n')
