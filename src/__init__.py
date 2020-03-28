#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

import logging
import os
import sys

import jinja2

from .build import BuilderOptions
from .helper import EnvHelper, MirrorHelper


class Package(object):

    def __init__(self,
                 name,
                 archive_prefix,
                 extract_prefix,
                 install_prefix,
                 module,
                 version: str = None,
                 verbose: bool = False,
                 thread_num: int = None,
                 stdout=None,
                 stderr=None):

        ####################### base ############################
        self.name = name
        self.archive_prefix = archive_prefix
        self.extract_prefix = extract_prefix
        self.install_prefix = install_prefix
        self.module = module
        self.version = version or module['version'][0]
        self.dirname = '{}-{}'.format(self.name, self.version)
        self.verbose = verbose
        ####################### base ############################

        ##################### download ##########################
        # download url
        self.url = jinja2.Template(module['archive']).render(version=self.version)
        self.mirror = MirrorHelper.get_mirror(self.url)
        # archive file path
        self.archive_path = os.path.join(self.archive_prefix,
                                         self.dirname + '.' + self.get_archive_suffix(self.url))
        # extract file to
        self.extract_path = os.path.join(self.extract_prefix, self.dirname)
        ##################### download ##########################

        ##################### build #############################
        self.env = {}
        self.args = ''
        self.install_args = ''
        self.type = None  # cmake or configure or custom
        self.thread_num = thread_num
        self.build_options = None
        self.index_path = ''
        self.build_path = ''
        self.stdout = stdout or sys.stdout
        self.stderr = stderr or sys.stderr
        self.install_path = os.path.join(self.install_prefix, self.dirname)
        self.cmake_prefix_path = ''
        self.step = ''
        self.autoreconf = False
        ##################### build #############################

        self.logger = logging.getLogger(self.name)

    def prepare_build_opt(self, inc_list, inc_map):
        self.env = EnvHelper.get_env_from_path(inc_list)
        compile = self.module['compile']
        self.type = compile['type']

        build_path = compile.get('build_path', '_build')
        self.build_path = os.path.join(self.extract_path, build_path)

        if self.type in ('cmake', 'configure', 'perl', 'ninja', 'make'):

            index_path = compile.get('index', '.')
            self.index_path = os.path.join(self.extract_path, index_path)

            self.args = compile.get('args', '')
            if self.args:
                if isinstance(self.args, list):
                    self.args = ' '.join(self.args)
                try:
                    self.args = jinja2.Template(self.args).render(inc_map=inc_map,
                                                                  install_path=self.install_path)
                except TypeError:
                    self.logger.critical('Template (%s) with type(%s) render error', self.args,
                                         type(self.args))

            if self.type == 'cmake':
                self.cmake_prefix_path = ';'.join(inc_list)
            if self.type == 'configure':
                self.autoreconf = compile.get('autoreconf', False)
            if self.type == 'make':
                self.install_args = compile.get('install_args', '')
                self.install_args = jinja2.Template(self.install_args).render(
                    inc_map=inc_map, install_path=self.install_path)
        elif self.type == 'custom':
            step = ' && '.join(compile.get('step', []))
            self.step = jinja2.Template(step).render(inc_map=inc_map,
                                                     install_path=self.install_path,
                                                     thread_num=self.thread_num)
        else:
            self.logger.critical('compile type %s is not support!!!', self.type)

        self.debug()

        self.build_options = BuilderOptions(
            self.name,
            self.env,
            self.thread_num,
            self.stdout,
            self.stderr,
            index_path=self.index_path,
            build_path=self.build_path,
            install_path=self.install_path,
            autoreconf=self.autoreconf,
            cmake_prefix_path=self.cmake_prefix_path,
            args=self.args,
            install_args=self.install_args,
            step=self.step,
            verbose=self.verbose,
        )

    def debug(self):
        output = 'name: %s\nenv: %s\nbuild_path: %s\nindex_path: %s\nthread_num: %d\n' % (
            self.dirname,
            self.env,
            self.build_path,
            self.index_path,
            self.thread_num,
        )
        return self.logger.info(output)

    @staticmethod
    def get_archive_suffix(url):
        support_suffix = ['tar.gz', 'tgz', 'zip', 'tar.xz']
        for suf in support_suffix:
            if url.endswith(suf):
                return suf
        else:
            return url.rsplit('.', 1)[1]

    def __str__(self):
        return str(self.__dict__)

    __repr__ = __str__
