# -*- coding: utf-8 -*- 
# @Time : 2021/3/10 16:45 
# @Author : Luciya 
# @File : test_login_ngboss.py
import pytest
from pySeleDemo.pages.login_page import LoginPage


class TestLoginNGBoss:
    def setup(self):
        self.loginPage = LoginPage()

    # def teardown(self):
    #     self.loginPage.quit()


    def test_login_ngboss(self):
        username = "91110069"
        password = "Asia!@34"
        self.loginPage.goto_index_page(username, password)
        assert True


    @pytest.mark.skip
    def test_login_group(self):
        group_id = "89191553680"
        self.indexPage.goto_login_group(group_id)

