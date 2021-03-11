# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 17:53 
# @Author : Luciya 
# @File : addinfopage.py
from HomeWork.wxOaHomework.pages.basepage import BasePage


class AddInfoPage(BasePage):
    def add_info(self, username, phone, mail, address):
        self._params["username"] = username
        self._params["phone"] = phone
        self._params["mail"] = mail
        self._params["address"] = address
        self.set_params("../data/addinfopage.yaml", "add_info")
        assert "添加成功"


