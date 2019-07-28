#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


import logging
import os
import shutil
import subprocess
import sys
import tarfile
import threading
import git
import requests
from abc import ABCMeta, abstractmethod
from io import StringIO, BytesIO


from ..build_manager import BuildManager
from ..cache_manager import CacheManager

total_deps = {}


# class Target(metaclass=ABCMeta):
class Target(object):
    __metaclass__ = ABCMeta

    def __init__(self, root, name, version, install_root=None, website=None,
                 git_uri=None, archive_uri=None, thread_num=2, deps=None):
        self.root = root
        self.name = name
        self.version = version
        self.website = website

        self.git_uri = git_uri

        self.archive_uri = archive_uri

        self.thread_num = thread_num

        self.cache_dir = os.path.join(self.root, "_cache")

        self.repo_name = "%s_%s" % (self.name, self.version)
        self.repo_path = os.path.join(self.root, self.repo_name)

        self.deps = deps or []
        self.prepare_deps()

        self.env = None
        self.prepare_env()

        # 目前只有cmake automake支持在指定路径build, 其它情况默认在项目根路径build
        self.build_root = None
        self.prepare_build_path("")

        self.install_root = install_root or os.path.join(self.repo_path, "_install")
        self.install_bin = os.path.join(self.install_root, "bin")
        self.install_inc = os.path.join(self.install_root, "include")
        self.install_lib = os.path.join(self.install_root, "lib")

    def get_repo_sub_path(self, name):
        return os.path.join(self.repo_path, name)

    def prepare_build_path(self, build_suffix):
        self.build_root = os.path.join(self.repo_path, build_suffix)

    def prepare_deps(self):
        if not os.path.exists(self.root):
            os.makedirs(self.root)
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

        deps = [dep(root=self.root, install_root=self.install_root) for dep in self.deps]
        self.deps = deps
        for dep in self.deps:
            if dep.repo_name not in total_deps:
                total_deps[dep.repo_name] = dep

    def prepare_env(self):
        self.env = os.environ.copy()
        path = ":".join([dep.install_bin for dep in self.deps])
        self.env["PATH"] = path + ":" + self.env["PATH"]

        pkg = ":".join([dep.install_lib + "/pkgconfig" for dep in self.deps])
        self.env["PKG_CONFIG_PATH"] = pkg

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
                    logging.info("git:%s exists, just pull", self.git_uri)
                    return
            elif repo:
                if str(repo.head.commit) == repo.git.execute(["git", "rev-list", "-1", self.version]):
                    repo.git.reset('--hard')
                    repo.git.clean('-xdf')
                    logging.info("git:%s exists, commit equal", self.git_uri)
                    return

            logging.warning("%s exists, but branch not equal(%s->%s), remove",
                            self.repo_path, repo.active_branch, self.version)
            shutil.rmtree(self.repo_path)
        logging.info("Save To: %s", self.repo_path)
        try:
            git.Repo.clone_from(url=self.git_uri, to_path=self.repo_path, branch=self.version, depth=1)
        except git.GitCommandError as e:
            logging.error("%s", e.stderr)
        logging.info("[%s]: success to clone", self.repo_name)

    def update_archive_repo(self):
        download_file_name = os.path.basename(self.archive_uri)
        f = CacheManager.get(self.cache_dir, download_file_name)
        if f is None:
            f = BytesIO()
            f.write(requests.get(self.archive_uri).content)
            logging.info("success to download %s", download_file_name)
            CacheManager.set(self.cache_dir, download_file_name, f)

        t = tarfile.open(fileobj=f, mode="r:%s" % download_file_name.split(".")[-1])
        for m in t.getmembers():
            m.path = "/".join(m.path.split('/')[1:])
        t.extractall(self.repo_path)

    @abstractmethod
    def get_build_cmd(self):
        pass

    def update(self, update_deps=False):
        if update_deps:
            logging.info('[%s]: prepare all deps is %s', self.repo_name, str(total_deps))
            ths = []
            for dep in total_deps:
                th = threading.Thread(target=total_deps[dep].update)
                th.start()
                ths.append(th)
            for th in ths:
                th.join()
            logging.info("[%s]: finish to update-deps", self.repo_name)

        if self.archive_uri:
            self.update_archive_repo()
        elif self.git_uri:
            self.update_git_repo()
        else:
            logging.critical("git_uri and archive_uri is none")

    def build(self, build_deps=False, force=False):
        if build_deps:
            logging.info('[%s]: build all deps is %s', self.repo_name, str(total_deps))
            ths = []
            for dep in total_deps:
                th = threading.Thread(target=total_deps[dep].build)
                th.start()
                ths.append(th)
            for th in ths:
                th.join()
            logging.info("[%s]: finish to build-deps", self.repo_name)

        if not force and BuildManager.check_mark(self.install_root, self.repo_name):
            return
        logging.info("build cmd:" + self.get_build_cmd())
        if not os.path.exists(self.install_root):
            os.makedirs(self.install_root)
        if not os.path.exists(self.build_root):
            os.makedirs(self.build_root)
        res = subprocess.Popen(self.get_build_cmd(),
                               cwd=self.build_root,
                               env=self.env,
                               shell=True, stdout=sys.stdout, stderr=sys.stderr)
        ret = res.wait()
        if ret == 0:
            BuildManager.write_mark(self.install_root, self.repo_name)
        return res

    def cmake_cmd(self, mat="", *args):
        if "-S" not in mat:
            mat += " -S %s " % self.repo_path
        self.prepare_build_path("_build")
        cmake_prefix_path = ";".join([dep.install_root for dep in self.deps])
        return 'cmake -B %s -DCMAKE_PREFIX_PATH="%s" -DCMAKE_INSTALL_PREFIX=%s %s && %s' % (
            self.build_root, cmake_prefix_path, self.install_root,
            mat % args, self.make_cmd())

    def configure_cmd(self, autogen=False, mat="", *args):
        pre = ""
        self.prepare_build_path("_build")
        if autogen:
            pre = "bash %s/autogen.sh && " % self.repo_path
        return pre + "bash %s/configure --prefix=%s %s && %s" % (self.repo_path,
            self.install_root, mat % args, self.make_cmd())

    def make_cmd(self):
        return "make -j %d && make install" % self.thread_num
