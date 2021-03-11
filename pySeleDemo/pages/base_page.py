# -*- coding: utf-8 -*- 
# @Time : 2021/3/10 16:11 
# @Author : Luciya 
# @File : base_page.py
from appium.webdriver.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver == None:
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
        else:
            self.driver = driver
        if self.base_url != "":
            self.driver.get(self.base_url)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def click(self, by, locator):
        return self.find(by, locator).click()

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def click_send(self, by, locator, value):
        return self.find(by, locator).send_keys(value)

    def quit(self):
        self.driver.quit()

    def wait_click(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
