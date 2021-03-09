# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 17:47 
# @Author : Luciya 
# @File : maillist_page.py
from appium.webdriver.common.mobileby import MobileBy

from HomeWork.wxOaHomework.pages.basepage import BasePage
from HomeWork.wxOaHomework.pages.addfriendpage import AddFriendPage


class MailListPage(BasePage):
    def goto_add_friend(self):
        # 指定对应的yaml文件和函数名
        self.set_params("../data/maillistpage.yaml", "goto_add_friend")
        return AddFriendPage(self.driver)