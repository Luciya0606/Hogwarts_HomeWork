# -*- coding: utf-8 -*- 
# @Time : 2021/3/9 16:09 
# @Author : Luciya 
# @File : member_page.py
from selenium.webdriver.common.by import By

from HomeWork.wxOaWebHomeWork.pages.add_member_page import AddMemberPage
from HomeWork.wxOaWebHomeWork.pages.base_page import BasePage


class MemberPage(BasePage):
    def goto_add_member(self):
        """
        点击通讯录
        添加成员
        """
        self.find(By.CSS_SELECTOR, ".js_add_member").click()
        return AddMemberPage(self.driver)