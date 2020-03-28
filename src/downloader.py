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
import shutil
import threading
from io import BytesIO

import requests
import requests_ftp

from . import Package
from .tool.extractor import Extractor


class Downloader(object):

    def __init__(self, proxies):
        self.proxies = proxies

        self.logger = logging.getLogger('downloader')
        requests_ftp.monkeypatch_session()
        self.session = requests.Session()

    def download(self, pkg_list: [Package]):
        ths = []
        for package in pkg_list:
            th = threading.Thread(target=self.download_one, args=(package,))
            th.start()
            ths.append(th)
        for th in ths:
            th.join()

    def download_one(self, pkg: Package):
        self.logger.info('download %s with url %s', pkg.dirname, pkg.mirror)
        f = self._get_cache(pkg.archive_path)
        if self.proxies:
            self.logger.info('use proxies: %s', str(self.proxies))
        if f is None:
            f = BytesIO()
            f.write(self.session.get(pkg.mirror, proxies=self.proxies).content)
            self._set_cache(pkg.archive_path, f)
            self.logger.info('success to download %s', pkg.dirname)

        extractor = Extractor(f, mode=pkg.archive_path.rsplit('.', 1)[1])
        extractor.extract_to(pkg.extract_path)

    def _get_cache(self, file_path):
        content = BytesIO()
        if os.path.exists(file_path):
            with codecs.open(file_path, 'rb') as f:
                content.write(f.read())
                content.seek(0)
            self.logger.debug('[%s]: found in cache', file_path)
            return content
        self.logger.debug('[%s]: not in cache', file_path)
        return None

    def _set_cache(self, file_path, file_obj):
        if os.path.exists(file_path):
            self.logger.critical('[%s] should not exists', file_path)

        with codecs.open(file_path, 'wb') as cf:
            file_obj.seek(0)
            cf.write(file_obj.read())
            file_obj.seek(0)
        self.logger.debug('[%s]: save to cache', file_path)
