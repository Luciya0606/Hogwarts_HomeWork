# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 14:17 
# @Author : Luciya 
# @File : work_page.py
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from pyAppDemo.pages.basepage import BasePage
from pyAppDemo.pages.sign_page import SignPage


class WorkPage(BasePage):
    def goto_sign_page(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                       'new UiScrollable(new UiSelector().'
                                       'scrollable(true).instance(0)).'
                                       'scrollIntoView(new UiSelector().'
                                       f'text("打卡").instance(0));').click()
        return SignPage(self.driver)
