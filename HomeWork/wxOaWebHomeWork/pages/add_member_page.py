# -*- coding: utf-8 -*- 
# @Time : 2021/3/9 15:45 
# @Author : Luciya 
# @File : add_member_page.py
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from HomeWork.wxOaWebHomeWork.pages.base_page import BasePage


class AddMemberPage(BasePage):
    def add_member(self, username, account, phone):
        """
        手动输入联系人信息
        点击保存
        """
        # self.driver.find_element(By.ID, "username").send_keys("luciya")
        # self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("202020")
        # self.driver.find_element(By.ID, "memberAdd_phone").send_keys("13895652563")
        # 当页面有多个相同元素时，通过find_element会找到第一个元素
        # self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        """
        通过继承基类，调用基类封装的定位方法
        """
        self.find(By.ID, "username").send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        self.find(By.ID, "memberAdd_phone").send_keys(phone)

        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return True


    def get_member(self):
        """
        获取联系人信息
        """
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".member_colRight_memberTable_th_Checkbox")))
        locator = (By.CSS_SELECTOR, ".member_colRight_memberTable_th_Checkbox")
        self.wait_for_click(10, locator)
        ele_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        print(ele_list)
        names = []
        for ele in ele_list:
            names.append(ele.get_attribute("title"))
        return names






