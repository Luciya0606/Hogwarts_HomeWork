# -*- coding: utf-8 -*- 
# @Time : 2021/3/6 14:44 
# @Author : Luciya 
# @File : information.py
from Pyhomework.wxOaHomework.pages import mailList
from Pyhomework.wxOaHomework.pages.basepage import BasePage


class Information(BasePage):
    def goto_address(self):
        self.set_params("../data/information.yaml", "goto_address")
        return mailList(self.driver)
