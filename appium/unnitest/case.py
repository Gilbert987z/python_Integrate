# -*- coding:UTF-8 -*-
from unittest import TestCase
from selenium_test import webdriver  # 导入selenium中的webdriver包
from data import *
from element import *
from check import *
from unittest import TestCase

#
# 用例模块
#

class Login(TestCase):
    @classmethod
    def setUpClass(self):
        self.n = 1

    @classmethod
    def setUp(self):
        l_submit(readExcel('login', self.n, 0), readExcel('login', self.n, 1))
        self.n = self.n + 1

    def test1(self):
        l_success_check()
        l_quite()

    def test1(self):
        l_success_check()
        l_quite()

    def test2(self):
        l_success_check()
        l_quite()

    def test3(self):
        l_fail_check()
        l_quite()

    def test4(self):
        l_fail_check()
        l_quite()