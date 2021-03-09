# -*- coding: utf-8 -*- 
# @Time : 2021/3/9 16:29 
# @Author : Luciya 
# @File : test_add_member.py
from HomeWork.wxOaWebHomeWork.pages.main_page import MainPage


class TestAddMember:
    def setup(self):
        # 从首页入口开始
        self.mainPage = MainPage()


    def teardown(self):
        self.mainPage.quit()

    def test_add_member(self):
        username = "小小2"
        account = "xiao02"
        phone = "13589652631"
        page = self.mainPage.goto_member()
        page.add_member(username, account, phone)
        names = page.get_member()
        assert username in names


    def test_get_member(self):
        self.mainPage.goto_member_list().get_member()





