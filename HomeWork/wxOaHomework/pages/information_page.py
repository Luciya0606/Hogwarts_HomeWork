# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 17:46 
# @Author : Luciya 
# @File : information_page.py
from appium.webdriver.common.mobileby import MobileBy

from HomeWork.wxOaHomework.pages.basepage import BasePage
from HomeWork.wxOaHomework.pages.maillist_page import MailListPage


class InformationPage(BasePage):
    def goto_mail_page(self):
        # 指定对应的yaml文件和函数名
        self.set_params("../data/information.yaml", "goto_mail_page")
        return MailListPage(self.driver)