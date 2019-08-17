#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


import os
import sys
import git
import shutil
import logging
import tarfile
import requests
import subprocess
from io import BytesIO
from abc import ABCMeta, abstractmethod

from ..utils import get_mirror


# class Target(metaclass=ABCMeta):
class Target(object):
    """
    """
    __metaclass__ = ABCMeta

    def __init__(self, root, name, version, url=None, cache=None,
                 thread_num=2,
                 website=None,
                 deps=None, build_config=None):

        self.root = root
        self.name = name
        self.url = url
        self.version = version
        self.website = website
        self.repo_name = "%s_%s" % (self.name, self.version)

        self.cache = cache
        self.thread_num = thread_num
        self.logger = logging.getLogger(name)

        # 目前只有cmake automake支持在指定路径build, 其它情况默认在项目根路径build

        self.repo_path = os.path.join(root, self.repo_name)
        self.deps_path = os.path.join(root, "install_deps")
        self.deps = set(deps) if deps else set()

        self.build_config = build_config

        self.env = None
        self.prepare_env()

    @staticmethod
    def from_config(root, cache, config, version=None):
        """
        :param config:
            dict(
                name=name,
                url=url,
                version=version,
                config=config,
                website=website,
                deps=deps
            )
        :return:
        """
        version = version or config["version"]
        return Target(root=root, cache=cache,
                      version=version, name=config["name"], url=config["url"],
                      website=config["website"], deps=config["deps"],
                      build_config=config["build_config"])

    def update(self):
        if "git@" in self.url:
            self.update_git_repo()
        elif self.url:
            self.update_archive_repo()
        else:
            raise RuntimeError()

    def update_git_repo(self):
        if os.path.isdir(self.repo_path):
            try:
                repo = git.Repo(path=self.repo_path)
            except git.InvalidGitRepositoryError:
                repo = None

            if repo and not repo.head.is_detached:
                if str(repo.active_branch) == str(self.version):
                    repo.git.reset('--hard')
                    repo.git.clean('-xdf')
                    repo.remotes.origin.pull()
                    logging.info("git:%s exists, just pull", self.url)
                    return
            elif repo:
                if str(repo.head.commit) == repo.git.execute(["git", "rev-list", "-1", self.version]):
                    repo.git.reset('--hard')
                    repo.git.clean('-xdf')
                    logging.info("git:%s exists, commit equal", self.url)
                    return

            logging.warning("%s exists, but branch not equal(%s->%s), remove",
                            self.repo_path, repo.active_branch, self.version)
            shutil.rmtree(self.repo_path)
        logging.info("Save To: %s", self.repo_path)
        try:
            git.Repo.clone_from(url=self.url, to_path=self.repo_path, branch=self.version, depth=1)
        except git.GitCommandError as e:
            logging.error("%s", e.stderr)
        logging.info("[%s]: success to clone", self.repo_name)

    def update_archive_repo(self):
        download_file_name = os.path.basename(self.url)
        f = self.cache.get(download_file_name)
        if f is None:
            f = BytesIO()
            f.write(requests.get(get_mirror(self.url)).content)
            logging.info("success to download %s", download_file_name)
            self.cache.set(download_file_name, f)

        t = tarfile.open(fileobj=f, mode="r:%s" % download_file_name.split(".")[-1])
        for m in t.getmembers():
            m.path = "/".join(m.path.split('/')[1:])
        t.extractall(self.repo_path)

    def prepare_env(self):
        self.env = os.environ.copy()
        self.env["PATH"] = os.path.join(self.deps_path, "bin") + ":" + self.env["PATH"]
        self.env["PKG_CONFIG_PATH"] = os.path.join(self.deps_path, "lib")

    def build(self, install_path):

        build_command = self.get_build_cmd(install_path)
        if "cmake" in build_command or "configure" in build_command:
            build_path = os.path.join(self.repo_path, "_build")
            if not os.path.exists(build_path):
                os.makedirs(build_path)
        else:
            build_path = self.repo_path

        self.logger.info('[%s]: start to build\n build cmd: [%s]', self.repo_name, build_command)

        res = subprocess.Popen(build_command, cwd=build_path, env=self.env,
                               shell=True, stdout=sys.stdout, stderr=sys.stderr)
        return res.wait()

    @abstractmethod
    def get_build_cmd(self, install_path):
        if self.build_config:
            if self.build_config["type"] == "cmake":
                return self.cmake_cmd(install_path,
                                      src=self.build_config["src"],
                                      mat=self.build_config["mat"],
                                      *self.build_config["args"]
                                      )
            elif self.build_config["type"] == "configure":
                return self.configure_cmd(install_path,
                                          autogen=self.build_config["autogen"],
                                          mat=self.build_config["mat"],
                                          *self.build_config["args"]
                                          )
            raise RuntimeError("unreachable")

    def cmake_cmd(self, install_path, src=".", mat="", *args):
        return 'cmake -S %s -DCMAKE_PREFIX_PATH="%s" -DCMAKE_INSTALL_PREFIX=%s %s' % (
            os.path.join(self.repo_path, src),
            self.deps_path,
            install_path,
            mat % args) + " && " + self.make_cmd()

    def configure_cmd(self, install_path, autogen=False, mat="", *args):
        pre = "" if not autogen else "bash %s/autogen.sh && " % self.repo_path
        return pre + "bash %s/configure --prefix=%s %s" % (
            self.repo_path, install_path,
            mat % args) + " && " + self.make_cmd()

    def make_cmd(self):
        return "make -j %d && make install" % self.thread_num
