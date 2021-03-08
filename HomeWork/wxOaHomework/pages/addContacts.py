# -*- coding: utf-8 -*- 
# @Time : 2021/3/6 15:53 
# @Author : Luciya 
# @File : addContacts.py
from Pyhomework.wxOaHomework.pages.basepage import BasePage


class AddContacts(BasePage):
    def goto_add(self):
        self.set_params("", "add")
