# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 17:55 
# @Author : Luciya 
# @File : base_page.py
import json
from typing import List, Dict

import allure
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from HomeWork.wxOaHomework.conftest import root_log


class BasePage:
    # 定义传入值
    _params = {}
    # 添加异常弹框黑名单
    _black_list = [(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gu_']")]

    # 设置弹框次数上限
    _error_num = 0
    _error_max = 5

    # 基类初始化driver以便于子类调用时可以省掉初始化driver，直接进行复用
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, by, locator):
        """
        新增黑名单操作
        """
        root_log.info(f"find: by= {by}, locator= {locator}")
        try:
            element = self.driver.find_element(by, locator)
            self._error_num = 0
            self.wait_implicitly_step(10)
            return element
        except Exception as e:
            root_log.error("未找到元素")
            self.wait_implicitly_step(2)
            # 异常截图
            self.driver.get_screenshot_as_file("tmp.png")
            # 添加异常截图到测试报告中
            allure.attach.file("tmp.png", attachment_type=allure.attachment_type.PNG)
            if self._error_num >= self._error_max:
                self._error_num = 0
                self.wait_implicitly_step(10)
                raise e
            self._error_num += 1
            for black in self._black_list:
                # *解包功能
                # blacks = self.driver.find_elements(*black)
                blacks = self.finds(*black)
                if len(blacks) > 0:
                    # 如果黑名单列表长度大于0，就执行黑名单点击操作
                    blacks[0].click()
                    # 黑名单操作完成，继续查找需要查找的元素
                    return self.find(by, locator)
            raise e

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def find_click(self, by, locator):
        return self.find(by, locator).click()

    def send(self, by, locator, value):
        return self.find(by, locator).send_keys(value)

    def swipe_scroll(self, text):
        element = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                           'new UiScrollable(new UiSelector().'
                                           'scrollable(true).instance(0)).'
                                           'scrollIntoView(new UiSelector().'
                                           f'text("{text}").instance(0));').click()
        return element

    # 显示等待
    def wait_for(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    # 隐式等待
    def wait_implicitly_step(self, timeout):
        return self.driver.implicitly_wait(timeout)

    def set_params(self, path, fun_name):
        # 读取数据流，传入路径，r表示方式为读取
        with open(path, "r", encoding="utf-8") as f:
            # 定义一个函数名，可以用于一个yaml对应多个用例
            function = yaml.safe_load(f)
            # 关键字为列表格式，循环读取列表
            steps: List[Dict] = function[fun_name]
            """
            json.dumps()序列化
            json.loads()反序列化
            """
            raw = json.dumps(steps)
            for key, value in self._params.items():
                raw = raw.replace("${" + key + "}", value)
            steps = json.loads(raw)
            print(steps)
            for step in steps:
                if step["action"] == "find":
                    self.find(step["by"], step["locator"])
                elif step["action"] == "click":
                    self.find_click(step["by"], step["locator"])
                elif step["action"] == "send":
                    value: str = step['text']
                    for param in self._params:
                        # 重写value，以self._values[重写value]替代'{%s}'%value
                        value = value.replace('{%s}' % param, self._params[param])
                    self.send(step["by"], step["locator"], value)
                elif step["action"] == "swipe":
                    self.swipe_scroll(value)
