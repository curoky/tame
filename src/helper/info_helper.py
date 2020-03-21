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

import json
import os


class InfoHelper(object):

    def __init__(self, modules):
        self.modules = modules

    def show(self, name):
        config = self.modules[name]

        print(json.dumps(config, sort_keys=True, indent=4, separators=(',', ':')))

    def list(self, path):
        paths = os.listdir(self.install_prefix)
        print("Already build repos:")
        for p in paths:
            info = p.split("_")
            print("\t%s:\t%s" % (info[0], info[1]))
