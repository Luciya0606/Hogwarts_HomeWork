# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 17:53 
# @Author : Luciya 
# @File : addinfopage.py
from HomeWork.wxOaHomework.pages.basepage import BasePage


class AddInfoPage(BasePage):
    def add_info(self, send_value):
        self.set_params("../data/addinfopage.yaml", "add_info", send_value)
        return self.find("//*[class='android.widget.TextView']").text


