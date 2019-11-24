#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

import codecs
import logging
import os
import shutil
import tarfile
import zipfile
import threading
import sys
from io import BytesIO
import requests
import requests_ftp
from jinja2 import Template

import requests
import requests_ftp

from . import Package

global_mirror = {
    "ftp.gnu.org": [
        "mirrors.cloud.tencent.com",
        "mirrors.tuna.tsinghua.edu.cn",
    ],
    "www.python.org/ftp": [
        "npm.taobao.org/mirrors",
    ],
    "ftp.gnome.org/pub/gnome/": [
        "mirrors.ustc.edu.cn/gnome/",
    ],
    "www.openssl.org": ["mirrors.cloud.tencent.com/openssl"]
}


class Downloader(object):

    def __init__(self, root, global_config, thread_num):
        self.root = root
        self.global_config = global_config
        self.thread_num = thread_num

        self.archive_path = os.path.join(root, "archive")

        self.logger = logging.getLogger('downloader')
        requests_ftp.monkeypatch_session()
        self.session = requests.Session()
        if not os.path.exists(self.archive_path):
            os.makedirs(self.archive_path)

    def downloads(self, package_list, proxies):
        ths = []
        for package in package_list:
            th = threading.Thread(target=self._download_one,
                                  args=(
                                      package.repo_name,
                                      package.download_path,
                                      package.version,
                                      proxies,
                                  ))
            th.start()
            ths.append(th)
        for th in ths:
            th.join()

    def _download_one(self, repo_name, download_path, version, proxies):
        config = self.global_config[repo_name]

        raw_url = config["download"].get("archive-url")
        url = Template(raw_url).render(version=version)
        self._download_with_tar(url, download_path, version, proxies)

    def _download_with_tar(self, url, download_path, version, proxies):
        # check for mirror
        for k in global_mirror:
            if k in url:
                url = url.replace(k, global_mirror[k][0])
        self.logger.debug("real download url %s", url)
        file_name = os.path.basename(url)
        f = self._get_cache(file_name)
        if f is None:
            f = BytesIO()
            f.write(self.session.get(url, proxies=proxies).content)
            self.logger.info("success to download file %s", file_name)
            self._set_cache(file_name, f)
        mode = file_name.split(".")[-1]
        if mode == "tgz":
            mode = "gz"
        if mode in ("gz", "bz2", "xz"):
            t = tarfile.open(fileobj=f, mode="r:" + mode)
            for m in t.getmembers():
                m.path = "/".join(m.path.split('/')[1:])
            shutil.rmtree(download_path, ignore_errors=True)
            t.extractall(download_path)
        elif mode in ("zip"):
            t = zipfile.ZipFile(f, mode="r")
            t.extractall(download_path)

    def _get_cache(self, file_name):
        rio = BytesIO()
        if os.path.exists(os.path.join(self.archive_path, file_name)):
            self.logger.info("[%s]: find in cache", file_name)
            with codecs.open(os.path.join(self.archive_path, file_name),
                             "rb") as cf:
                rio.write(cf.read())
                rio.seek(0)
            return rio
        self.logger.info("[%s]: not in cache", file_name)
        return None

    def _set_cache(self, file_name, file_obj):
        if os.path.exists(os.path.join(self.archive_path, file_name)):
            self.logger.critical('[%s] should not exists', file_name)

        with codecs.open(os.path.join(self.archive_path, file_name),
                         "wb") as cf:
            file_obj.seek(0)
            cf.write(file_obj.read())
            file_obj.seek(0)
        self.logger.info("[%s]: save to cache", file_name)
