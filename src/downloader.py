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
from io import BytesIO
import requests
import git
from jinja2 import Template

from src.config import repo_config

global_mirror = {
    "ftp.gnu.org": [
        "mirrors.tuna.tsinghua.edu.cn",
    ],
    "www.python.org/ftp": [
        "npm.taobao.org/mirrors",
    ],
}


class Downloader(object):

    def __init__(self, root):
        self.root = root
        self.cache_dir = os.path.join(root, "_cache")
        self.logger = logging.getLogger(__name__)

        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

    def downloads(self, target_list, proxies):
        ths = []
        for target in target_list:
            th = threading.Thread(target=self._download_one,
                                  args=(
                                      target.repo_name,
                                      target.repo_path,
                                      target.version,
                                      proxies,
                                  ))
            th.start()
            ths.append(th)
        for th in ths:
            th.join()

    def _download_one(self, repo_name, repo_path, version, proxies):
        config = repo_config[repo_name]
        raw_url = config["download"].get("archive-url")
        if raw_url:
            url = Template(raw_url).render(version=version)
            self._download_with_tar(url, repo_path, version, proxies)
            return
        raw_url = config["download"].get("git-url")
        if raw_url:
            url = Template(raw_url).render(version=version)
            self._download_with_git(url, repo_path, version, proxies)
            return
        raise RuntimeError("not have download url for %s" % repo_name)

    def _download_with_git(self, url, repo_path, version, proxies):

        if os.path.isdir(repo_path):
            try:
                repo = git.Repo(path=repo_path)
            except git.InvalidGitRepositoryError:
                repo = None

            if repo and not repo.head.is_detached:
                if str(repo.active_branch) == version:
                    repo.git.reset('--hard')
                    repo.git.clean('-xdf')
                    repo.remotes.origin.pull()
                    self.logger.debug("[%s]: git exists, just pull", repo_path)
                    return
            elif repo:
                if str(repo.head.commit) == repo.git.execute(
                    ["git", "rev-list", "-1", version]):
                    repo.git.reset('--hard')
                    repo.git.clean('-xdf')
                    self.logger.debug("[%s]: git exists, commit equal",
                                      repo_path)
                    return

            self.logger.warning("[%s]:exist not available remove it", repo_path)
            shutil.rmtree(repo_path)

        self.logger.info("[%s]:start clone to ", repo_path)
        try:
            git.Repo.clone_from(url=url,
                                to_path=repo_path,
                                branch=version,
                                depth=1)
        except git.GitCommandError as e:
            self.logger.critical("%s", e.stderr)
        self.logger.info("[%s]:success to clone", repo_path)

    def _download_with_tar(self, url, repo_path, version, proxies):
        # check for mirror
        for k in global_mirror:
            if k in url:
                url = url.replace(k, global_mirror[k][0])
        self.logger.debug("real download url %s", url)
        file_name = os.path.basename(url)
        f = self._get_cache(file_name)
        if f is None:
            f = BytesIO()
            f.write(requests.get(url, proxies=proxies).content)
            self.logger.info("success to download file %s", file_name)
            self._set_cache(file_name, f)
        mode = file_name.split(".")[-1]
        if mode == "tgz":
            mode = "gz"
        if mode in ("gz", "bz2", "xz"):
            t = tarfile.open(fileobj=f, mode="r:" + mode)
            for m in t.getmembers():
                m.path = "/".join(m.path.split('/')[1:])
            shutil.rmtree(repo_path, ignore_errors=True)
            t.extractall(repo_path)
        elif mode in ("zip"):
            t = zipfile.ZipFile(f, mode="r")
            t.extractall(repo_path)

    def _get_cache(self, file_name):
        rio = BytesIO()
        if os.path.exists(os.path.join(self.cache_dir, file_name)):
            self.logger.info("[%s]: find in cache", file_name)
            with codecs.open(os.path.join(self.cache_dir, file_name),
                             "rb") as cf:
                rio.write(cf.read())
                rio.seek(0)
            return rio
        self.logger.info("[%s]: not in cache", file_name)
        return None

    def _set_cache(self, file_name, file_obj):
        if os.path.exists(os.path.join(self.cache_dir, file_name)):
            self.logger.critical('[%s] should not exists', file_name)

        with codecs.open(os.path.join(self.cache_dir, file_name), "wb") as cf:
            file_obj.seek(0)
            cf.write(file_obj.read())
            file_obj.seek(0)
        self.logger.info("[%s]: save to cache", file_name)
