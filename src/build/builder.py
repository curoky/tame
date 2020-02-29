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

from abc import ABCMeta, abstractmethod
import subprocess
import logging
import os


class BuilderOptions(object):

    def __init__(self,
                 name,
                 env,
                 thread_num,
                 stdout,
                 stderr,
                 index_path='.',
                 build_path='.',
                 install_path='.',
                 cmake_prefix_path='.',
                 autoreconf=False,
                 args='',
                 install_args='',
                 step='',
                 verbose=False):
        self.name = name
        self.env = env
        self.thread_num = thread_num
        self.stdout = stdout
        self.stderr = stderr
        self.index_path = index_path
        self.build_path = build_path
        self.install_path = install_path
        self.verbose = verbose
        self.args = args
        self.install_args = install_args

        # for cmake
        self.cmake_prefix_path = cmake_prefix_path
        # for configure
        self.autoreconf = autoreconf
        # for custom
        self.step = step


class Builder(metaclass=ABCMeta):

    def __init__(self, options: BuilderOptions):
        self.name = options.name
        self.env = options.env
        self.thread_num = options.thread_num

        self.stdout = options.stdout
        self.stderr = options.stderr

        self.install_path = options.install_path
        self.index_path = options.index_path
        self.build_path = options.build_path

        self.args = options.args
        self.install_args = options.install_args
        self.verbose = options.verbose

        self.logger = logging.getLogger(options.name)

    def exec(self, command: str, path: str):
        if not command:
            return 0
        self.logger.info('start to exec: %s', command)
        if not os.path.exists(path):
            os.makedirs(path)
        res = subprocess.Popen(command,
                               cwd=path,
                               env=self.env,
                               shell=True,
                               stdout=self.stdout,
                               stderr=self.stderr)
        return res.wait()

    @abstractmethod
    def command_prepare(self):
        pass

    @abstractmethod
    def command_build(self):
        pass

    @abstractmethod
    def command_install(self):
        pass

    @abstractmethod
    def command_test(self):
        pass

    def prepare(self):
        return self.exec(self.command_prepare(), self.build_path)

    def build(self):
        return self.exec(self.command_build(), self.build_path)

    def install(self):
        return self.exec(self.command_install(), self.build_path)

    def test(self):
        return self.exec(self.command_test(), self.build_path)
