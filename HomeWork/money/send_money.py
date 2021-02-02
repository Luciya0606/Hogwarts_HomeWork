# -*- coding: utf-8 -*- 
# @Time : 2021/1/25 20:57 
# @Author : Luciya 
# @File : send_money.py
import money

def send_money(salary):
    print(f"未发工资前存款{money.saved_money}")
    salary +=money.saved_money
    print(f"发工资啦{salary}")
    return salary