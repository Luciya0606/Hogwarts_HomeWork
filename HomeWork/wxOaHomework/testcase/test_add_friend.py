# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 18:06 
# @Author : Luciya 
# @File : test_add_friend.py
import pytest
import yaml

from HomeWork.wxOaHomework.pages.app import App


class TestAddFriend:
    def setup(self):
        self.app = App()

    def test_add_friend(self):
        username = "张张4"
        phone = "18254125631"
        mail = "zhang4@qq.com"
        address = "腾讯大厦101"
        self.app.goto_main().goto_mail_page().goto_add_friend().add_friend().add_info(username, phone, mail, address)
