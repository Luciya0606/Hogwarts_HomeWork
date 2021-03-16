# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 18:06 
# @Author : Luciya 
# @File : test_addFriend.py
import pytest
import yaml

from HomeWork.wxOaHomework.pages.app import App


class TestAddFriend:
    def setup(self):
        self.app = App()

    def test_add_friend(self):
        text = "添加成员"
        username = "张张3"
        phone = "18254115621"
        mail = "zhang3@qq.com"
        address = "腾讯大厦101"
        self.app.goto_main().goto_mail_page().goto_add_friend(text).add_friend().add_info(username, phone, mail, address).verify_ok()