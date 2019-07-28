#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author      : IceCory(icecory520@gmail.com)
# @Copyright(C): GPL 3.0
# @desc        :

import unittest

from ..cache_manager import CacheManager


class TestDemo(unittest.TestCase):
    def setUp(self):
        pass

    def test_demo(self):
        self.assertTrue(True)
        self.assertEqual(1, 1)

    def test_CacheManager(self):
        cm = CacheManager(".")
        print cm.files
