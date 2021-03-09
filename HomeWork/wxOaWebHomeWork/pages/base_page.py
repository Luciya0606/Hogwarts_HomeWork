# -*- coding: utf-8 -*- 
# @Time : 2021/3/9 15:45 
# @Author : Luciya 
# @File : base_page.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    base_url = ""
    def __init__(self, driver: WebDriver = None):
        if driver == None:
            # 浏览器复用 定义option.debugger_address
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver
        if self.base_url != "":
            self.driver.get(self.base_url)


    def quit(self):
        return self.driver.quit()

    def find(self, locator, value):
        return self.driver.find_element(locator, value)

    def finds(self, locator, value):
        return self.driver.find_elements(locator, value)

    def wait_for_click(self, timeout, locator):
        # 局部等待，判断是否可点击
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
