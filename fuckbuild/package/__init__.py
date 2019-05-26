#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :


import os
import sys
import git
import time
import shutil
import logging
import subprocess
from ..tar_util import get_fit_cmd
from abc import ABCMeta, abstractmethod


# class Target(metaclass=ABCMeta):
class Target(object):
    __metaclass__ = ABCMeta

    def __init__(self, prefix_path, name, version, website=None,
                 git_uri=None, archive_uri=None, thread_num=20):
        self.prefix_path = prefix_path
        self.name = name
        self.version = version
        self.website = website

        self.git_uri = git_uri

        self.archive_uri = archive_uri
        self.download_uri = None
        self.extract_dir_name = None

        self.thread_num = thread_num

    def file_name(self):
        return "%s_%s" % (self.name, self.version)

    def repo_path(self):
        return os.path.join(self.prefix_path, self.file_name())

    def install_path(self):
        return os.path.join(self.repo_path(), "__build")

    def get_include(self):
        return os.path.join(self.install_path(), "include")

    def get_lib(self):
        return os.path.join(self.install_path(), "lib")

    def get_bin(self):
        return os.path.join(self.install_path(), "bin")

    def update_git_repo(self):
        if os.path.isdir(self.repo_path()):
            repo = git.Repo(path=self.repo_path())

            if not repo.head.is_detached:
                if str(repo.active_branch) == str(self.version):
                    repo.git.reset('--hard')
                    repo.git.clean('-xdf')
                    repo.remotes.origin.pull()
                    logging.info("git:%s exists, just pull", self.git_uri)
                    return
            else:
                if str(repo.head.commit) == repo.git.execute(["git", "rev-list", "-1", self.version]):
                    repo.git.reset('--hard')
                    repo.git.clean('-xdf')
                    logging.info("git:%s exists, commit equal", self.git_uri)
                    return

            logging.warning("%s exists, but branch not equal(%s->%s), remove",
                            self.repo_path(), repo.active_branch, self.version)
            shutil.rmtree(self.repo_path())
        logging.info("Save To: %s", self.repo_path())
        try:
            git.Repo.clone_from(url=self.git_uri, to_path=self.repo_path(), branch=self.version, depth=1)
        except git.GitCommandError as e:
            logging.critical("%s", e.stderr)

    def update_archive_repo(self):
        temp_save_name = time.strftime("%m-%d-%H-%M_", time.localtime()) + self.file_name()

        if os.path.exists(os.path.join(self.prefix_path, self.file_name())):
            logging.info("dir %s is exits, not update", self.file_name())
            return
        update_cmd = "wget %s -O %s && tar %s %s && mv %s %s && rm %s" % (
            self.download_uri, temp_save_name,
            get_fit_cmd(self.download_uri), temp_save_name,
            self.extract_dir_name, self.file_name(),
            temp_save_name)
        logging.info("update_cmd %s", update_cmd)
        res = subprocess.Popen(update_cmd,
                               cwd=self.prefix_path,
                               shell=True, stdout=sys.stdout, stderr=sys.stderr)
        res.wait()
        return res

    @abstractmethod
    def get_build_cmd(self):
        pass

    def update(self):
        if self.git_uri:
            self.update_git_repo()
            return
        elif self.archive_uri:
            self.update_archive_repo()
            return
        logging.critical("git_uri and archive_uri is none")

    def build(self):
        logging.info("build cmd:" + self.get_build_cmd())
        if not os.path.exists(self.install_path()):
            os.makedirs(self.install_path())
        res = subprocess.Popen(self.get_build_cmd(),
                               cwd=self.repo_path(),
                               shell=True, stdout=sys.stdout, stderr=sys.stderr)
        res.wait()
        return res

    def cmake_cmd(self, mat="", *args):
        return "cmake -DCMAKE_INSTALL_PREFIX=%s %s && %s" % (
            self.install_path(), mat % args, self.make_cmd())

    def configure_cmd(self, mat="", *args):
        return "./configure --prefix=%s %s && %s" % (
            self.install_path(), mat % args, self.make_cmd())

    def make_cmd(self):
        return "make -j %d && make install" % self.thread_num
