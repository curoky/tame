# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

import codecs
import io
import logging
import os
import shutil
import tarfile
import zipfile


class Extractor(object):

    def __init__(self, name, mode):
        self.content = None
        self.mode = mode
        self.logger = logging.getLogger('Extractor')
        if isinstance(name, str):
            with codecs.open(name, 'rb') as f:
                self.content = f.read()
        elif isinstance(name, io.BytesIO):
            self.content = name
        if self.content is None:
            self.logger.critical('file content is empty')

    def extract_to(self, path):
        if self.mode == 'tgz':
            self.mode = 'gz'
        shutil.rmtree(path, ignore_errors=True)

        if self.mode in ('gz', 'bz2', 'xz'):
            with tarfile.open(fileobj=self.content, mode='r:' + self.mode) as tf:
                for m in tf.getmembers():
                    m.path = '/'.join(m.path.split('/')[1:])
                tf.extractall(path)
        elif self.mode == 'zip':
            with zipfile.ZipFile(self.content, mode='r') as zf:
                real_paths = []
                for m in zf.infolist():
                    real_path = m.filename
                    m.filename = '/'.join(m.filename.split('/')[1:])
                    if m.filename:
                        real_paths.append(real_path)
                zf.extractall(path, real_paths)
