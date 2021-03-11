# -*- coding: utf-8 -*- 
# @Time : 2021/3/10 16:07 
# @Author : Luciya 
# @File : index_page.py
from selenium.webdriver.common.by import By

from pySeleDemo.pages.base_page import BasePage


class IndexPage(BasePage):
    base_url = "http://172.16.79.15:8088/ngboss/?service=page/ngboss.frame.pc.common.Main&listener=init"

    def goto_login_group(self, value):
        locator = (By.ID, "groupFn")
        self.wait_click(10, locator)
        self.click_send(By.ID, "groupQueryTypeValueInput", value)
        self.click(By.CSS_SELECTOR, "#")


