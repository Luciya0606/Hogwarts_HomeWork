# -*- coding: utf-8 -*- 
# @Time : 2021/3/15 19:25 
# @Author : Luciya 
# @File : deletefriendpage.py
from HomeWork.wxOaHomework.pages.basepage import BasePage


class DeleteFriendPage(BasePage):
    def goto_del_friend(self):
        self.set_params("../data/deletefriendpage.yaml", "goto_del_friend")
        assert "删除成功"
