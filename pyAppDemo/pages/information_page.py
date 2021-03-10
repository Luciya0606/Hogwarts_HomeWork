# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 14:17 
# @Author : Luciya 
# @File : information_page.py
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from pyAppDemo.pages.basepage import BasePage
from pyAppDemo.pages.work_page import WorkPage


class InformationPage(BasePage):
    def goto_work_page(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        # self.find_click(self, "")
        return WorkPage(self.driver)