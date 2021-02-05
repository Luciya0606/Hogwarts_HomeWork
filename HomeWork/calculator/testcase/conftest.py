# -*- coding: utf-8 -*- 
# @Time : 2021/2/4 16:11 
# @Author : Luciya 
# @File : conftest.py
import pytest
import yaml

from HomeWork.calculator import Calculator

@pytest.fixture(scope="session")
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc


with open("../data/calc.yml") as f:
    # 获取整个yaml文件参数
    datas = yaml.safe_load(f)
    # 获取加法参数
    add_data = datas['add']['add_datas']
    add_ids = datas['add']['add_ids']
    print(f"{add_data}, {add_ids}")
    print(add_data[0])
    print(add_ids[0])
#
#     # 获取减法参数
#     sub_data = datas['sub']['sub_datas']
#     sub_ids = datas['sub']['sub_ids']
#     print(f"{sub_data}, {sub_ids}")
#
#     # 获取乘法参数
#     mul_data = datas['mul']['mul_datas']
#     mul_ids = datas['mul']['mul_ids']
#     print(f"{mul_data}, {mul_ids}")
#
#     # 获取除法参数
#     div_data = datas['div']['div_datas']
#     div_ids = datas['div']['div_ids']
#     print(f"{div_data}, {div_ids}")
#
#
# @pytest.fixture(params=add_data, ids=add_ids)
# def get_add_datas(request):
#     print("开始加法计算")
#     data = request.param
#     print(f"测试数据为：{data}")
#     yield data
#     print("结束加法计算")
#
#
# @pytest.fixture(params=sub_data, ids=sub_ids)
# def get_sub_datas(request):
#     print("开始减法计算")
#     data = request.param
#     print(f"测试数据为：{data}")
#     yield data
#     print("结束减法计算")
#
#
# @pytest.fixture(params=mul_data, ids=mul_ids)
# def get_mul_datas(request):
#     print("开始乘法计算")
#     data = request.param
#     print(f"测试数据为：{data}")
#     yield data
#     print("结束乘法计算")
#
#
# @pytest.fixture(params=div_data, ids=div_ids)
# def get_div_datas(request):
#     print("开始除法计算")
#     data = request.param
#     print(f"测试数据为：{data}")
#     yield data
#     print("结束除法计算")

