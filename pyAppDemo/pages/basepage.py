# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 14:16 
# @Author : Luciya 
# @File : base_page.py
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    # 基类初始化driver 以便于子类调用基类时复用driver 免掉了子类再进行初始化
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, locator):
        self.driver.find_element(MobileBy.XPATH, locator)

    def find_click(self, locator):
        self.driver.find_element(MobileBy.XPATH, locator).click()

    def send(self, locator, value):
        self.driver.find_element(MobileBy.XPATH, locator).send_keys(value)

    def swipe_scroll(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                       'new UiScrollable(new UiSelector().'
                                       'scrollable(true).instance(0)).'
                                       'scrollIntoView(new UiSelector().'
                                       f'text("{text}").instance(0));').click()

    def set_parmas(self):
        pass