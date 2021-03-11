# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 17:55 
# @Author : Luciya 
# @File : base_page.py
from typing import List, Dict

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 定义传入值
    _params = {}

    # 基类初始化driver以便于子类调用时可以省掉初始化driver，直接进行复用
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(MobileBy.XPATH, locator)

    def find_click(self, locator):
        return self.find(locator).click()

    def send(self, locator, value):
        return self.find(locator).send_keys(value)

    def swipe_scroll(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()

    def wait_for(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))


    def set_params(self, path, fun_name):
        # 读取数据流，传入路径，r表示方式为读取
        with open(path, "r", encoding="utf-8") as f:
            # 定义一个函数名，可以用于一个yaml对应多个用例
            function = yaml.safe_load(f)
            # 关键字为列表格式，循环读取列表
            steps: List[Dict] = function[fun_name]
            for step in steps:
                if step["action"] == "click":
                    self.find_click(step["locator"])
                elif step["action"] == "find":
                    self.find(step["locator"])
                elif step["action"] == "send":
                    value: str = step['value']
                    for param in self._params:
                        # 重写value，以self._values[重写value]替代'{%s}'%value
                        value = value.replace('{%s}' % param, self._params[param])
                    self.send(step["locator"], value)
                elif step["action"] == "swipe":
                    self.swipe_scroll(step["text"])

