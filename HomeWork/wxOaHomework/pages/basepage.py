# -*- coding: utf-8 -*- 
# @Time : 2021/3/6 14:42 
# @Author : Luciya 
# @File : basepage.py
from typing import List

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        self.driver.find_element(by, locator)

    def find_click(self, by, locator):
        self.driver.find_element(by, locator).click()

    def send(self, by, locator, value):
        self.driver.find_element(by, locator).send_keys(value)

    def scroll_click(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()

    def set_params(self, path, fun_name):
        with open(path, "r", encoding="utf-8") as f:
            function = yaml.safe_load(f)
            steps: List[dict] = function[fun_name]
        for step in steps:
            if step["action"] == "click":
                self.find_click(step["by"], step["locator"])
            elif step["action"] == "send":
                self.send(step["by"], step["locator"], step["value"])

