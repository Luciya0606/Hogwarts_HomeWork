# -*- coding: utf-8 -*- 
# @Time : 2021/3/10 16:06 
# @Author : Luciya 
# @File : login_page.py
from selenium.webdriver.common.by import By

from pySeleDemo.pages.base_page import BasePage
from pySeleDemo.pages.index_page import IndexPage


class LoginPage(BasePage):
    base_url = "http://172.16.79.15:8080/ngboss/?service=page/ngboss.frame.pc.common.Login"
    # base_url = "https://www.baidu.com"

    # def goto_back_login(self):
    #     self.click(By.ID, "back")
    #     return LoginPage(self.driver)

    def goto_index_page(self, username, password):
        self.click(By.ID, "back")
        self.click_send(By.ID, "STAFF_ID", username)
        self.click_send(By.ID, "PASSWORD", password)
        self.click(By.ID, "loginBtn")
        return IndexPage(self.driver)



