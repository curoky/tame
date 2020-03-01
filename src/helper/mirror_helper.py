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

from urllib.parse import urlparse


class MirrorHelper(object):
    MIRRORS = {
        'ftp.gnu.org': [
            'mirrors.cloud.tencent.com',
            'mirrors.tuna.tsinghua.edu.cn',
        ],
        'www.python.org/ftp': ['npm.taobao.org/mirrors',],
        'ftp.gnome.org/pub/gnome/': ['mirrors.ustc.edu.cn/gnome/',],
        'www.openssl.org': ['mirrors.cloud.tencent.com/openssl']
    }

    @staticmethod
    def get_mirror(url: str):
        netloc = urlparse(url).netloc
        if netloc in MirrorHelper.MIRRORS:
            return url.replace(netloc, MirrorHelper.MIRRORS[netloc][0])
        return url
