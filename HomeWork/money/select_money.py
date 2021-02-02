# -*- coding: utf-8 -*- 
# @Time : 2021/1/25 20:57 
# @Author : Luciya 
# @File : select_money.py

import send_money

def selectM(salary):
    sends_money=send_money.send_money(salary)
    print(f"发完工资存款{sends_money}")

