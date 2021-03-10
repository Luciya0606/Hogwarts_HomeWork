# -*- coding: utf-8 -*- 
# @Time : 2021/3/5 13:14 
# @Author : Luciya 
# @File : test_window.py
from pySeleDemo.base import Base
from pySeleDemo.page_baidu import PageBaidu
import pytest

class TestWindow(PageBaidu):
    @pytest.mark.skip
    def test_goto_login(self):
        self.goto_login()
        print("点击成功")

    @pytest.mark.skip
    def test_goto_switch(self):
        self.goto_switch_frame()
        print("切换成功")

    def test_js(self):
        self.goto_js_scroll()
        print("定位成功")