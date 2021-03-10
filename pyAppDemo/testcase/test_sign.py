# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 14:36 
# @Author : Luciya 
# @File : test_sign.py
from pyAppDemo.pages.app import App
from pyAppDemo.pages.basepage import BasePage
from pyAppDemo.pages.information_page import InformationPage


class TestSign:
    def setup(self):
        self.app = App()

    def test_sign(self):
        self.app.goto_main().goto_work_page().goto_sign_page().sign()




