# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 14:18 
# @Author : Luciya 
# @File : sign_page.py
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from pyAppDemo.pages.basepage import BasePage


class SignPage(BasePage):
    def sign(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")