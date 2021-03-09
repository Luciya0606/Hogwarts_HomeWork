# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 18:06 
# @Author : Luciya 
# @File : test_add_friend.py
import pytest
import yaml

from HomeWork.wxOaHomework.pages.app import App


class TestAddFriend:
    def setup(self):
        self.app = App()

    @pytest.mark.parametrize(["send_value"], yaml.safe_load(open("../data/testdata.yaml", "r", encoding="utf-8")))
    def test_add_friend(self, send_value):
        self.app.goto_main().goto_mail_page().goto_add_friend().add_friend().add_info(send_value)
