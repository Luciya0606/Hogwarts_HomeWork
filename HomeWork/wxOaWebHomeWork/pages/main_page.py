# -*- coding: utf-8 -*- 
# @Time : 2021/3/9 15:43 
# @Author : Luciya 
# @File : main_page.py


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from HomeWork.wxOaWebHomeWork.pages.add_member_page import AddMemberPage
from HomeWork.wxOaWebHomeWork.pages.base_page import BasePage
from HomeWork.wxOaWebHomeWork.pages.member_page import MemberPage


class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_member(self):
        """
        点击添加联系人
        """
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMemberPage(self.driver)

    def goto_member_list_add(self):
        self.find(By.ID, "menu_contacts").click()
        return MemberPage(self.driver)

    def goto_member_list(self):
        """
        点击通讯录
        """
        self.find(By.ID, "menu_contacts").click()
        return AddMemberPage(self.driver)
