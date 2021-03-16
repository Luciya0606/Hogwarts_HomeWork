# -*- coding: utf-8 -*- 
# @Time : 2021/3/15 17:44 
# @Author : Luciya 
# @File : test_deleteFriend.py
from HomeWork.wxOaHomework.pages.app import App


class TestDeleteMember:
    def setup(self):
        self.app = App()

    def test_del_member(self):
        text = "张张3"
        self.app.goto_main().goto_mail_page().goto_detail_friend(text).goto_del_friend()
