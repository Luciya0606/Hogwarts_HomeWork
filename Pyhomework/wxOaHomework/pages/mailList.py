# -*- coding: utf-8 -*- 
# @Time : 2021/3/6 14:45 
# @Author : Luciya 
# @File : mailList.py
from Pyhomework.wxOaHomework.pages.addContacts import AddContacts
from Pyhomework.wxOaHomework.pages.basepage import BasePage

class Maillist(BasePage):
    def goto_add_contacts(self):
        self.set_params("", "goto_add_contacts")
        return AddContacts(self.driver)
