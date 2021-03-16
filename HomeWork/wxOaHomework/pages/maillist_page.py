# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 17:47 
# @Author : Luciya 
# @File : maillist_page.py

from HomeWork.wxOaHomework.pages.basepage import BasePage
from HomeWork.wxOaHomework.pages.add_member.addfriendpage import AddFriendPage
from HomeWork.wxOaHomework.pages.delete_member.deletefriendpage import DeleteFriendPage


class MailListPage(BasePage):
    def goto_add_friend(self, text):
        # 指定对应的yaml文件和函数名
        self._params["text"] = text
        self.set_params("../data/maillistpage.yaml", "goto_add_friend")
        return AddFriendPage(self.driver)

    def goto_detail_friend(self, text):
        self._params["text"] = text
        self.set_params("../data/maillistpage.yaml", "goto_detail_info")
        return DeleteFriendPage(self.driver)
