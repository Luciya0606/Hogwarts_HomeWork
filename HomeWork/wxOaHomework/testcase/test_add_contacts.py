# -*- coding: utf-8 -*- 
# @Time : 2021/3/6 14:53 
# @Author : Luciya 
# @File : test_add_contacts.py
from Pyhomework.wxOaHomework.pages.app import App


class TestAddContacts:
    def setup(self):
        self.app = App()

    def test_add_contacts(self):
        self.app.goto_information()