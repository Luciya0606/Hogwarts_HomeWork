# -*- coding: utf-8 -*- 
# @Time : 2021/3/5 12:54 
# @Author : Luciya 
# @File : base.py
import os

import yaml
from selenium import webdriver

class Base:
    def setup(self):
        # 判断浏览器
        browser = os.getenv("browser")
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'IE':
            self.driver = webdriver.Ie()
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

