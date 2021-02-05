# -*- coding: utf-8 -*- 
# @Time : 2021/2/4 16:11 
# @Author : Luciya 
# @File : conftest.py
import pytest
import yaml

from calculator.python_code.calc import Calculator

@pytest.fixture(scope="module")
def get_calc():
    # 获取计算器实例
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")



with open("../data/calc.yml") as f:
    # 获取整个yaml文件参数
    datas = yaml.safe_load(f)
    # 获取加法参数
    add_data = datas['add']['add_datas']
    add_ids = datas['add']['add_ids']

    # 获取减法参数
    sub_data = datas['sub']['sub_datas']
    sub_ids = datas['sub']['sub_ids']

    # 获取乘法参数
    mul_data = datas['mul']['mul_datas']
    mul_ids = datas['mul']['mul_ids']

    # 获取除法参数
    div_data = datas['div']['div_datas']
    div_ids = datas['div']['div_ids']


@pytest.fixture(scope="module", params=add_data, ids=add_ids)
def get_add_datas(request):
    print("开始加法计算")
    data = request.param
    print(f"测试数据为：{data}")
    print(f"测试结果为：{data[2]}")
    yield data
    print("结束加法计算")


@pytest.fixture(scope="module", params=sub_data, ids=sub_ids)
def get_sub_datas(request):
    print("开始减法计算")
    data = request.param
    print(f"测试数据为：{data}")
    print(f"测试结果为：{data[2]}")
    yield data
    print("结束减法计算")



@pytest.fixture(scope="module", params=mul_data, ids=mul_ids)
def get_mul_datas(request):
    print("开始乘法计算")
    data = request.param
    print(f"测试数据为：{data}")
    print(f"测试结果为：{data[2]}")
    yield data
    print("结束乘法计算")


@pytest.fixture(scope="module", params=div_data, ids=div_ids)
def get_div_datas(request):
    print("开始除法计算")
    data = request.param
    print(f"测试数据为：{data}")
    print(f"测试结果为：{data[2]}")
    yield data
    print("结束除法计算")

