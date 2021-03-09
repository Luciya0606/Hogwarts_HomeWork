# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 17:49 
# @Author : Luciya 
# @File : addfriendpage.py
from appium.webdriver.common.mobileby import MobileBy

from HomeWork.wxOaHomework.pages.basepage import BasePage
from HomeWork.wxOaHomework.pages.addinfopage import AddInfoPage

class AddFriendPage(BasePage):
    def add_friend(self):
        # 指定对应的yaml文件和函数名
        self.set_params("../data/addfriendpage.yaml", "add_friend")
        return AddInfoPage(self.driver)