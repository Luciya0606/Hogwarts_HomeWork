# -*- coding: utf-8 -*- 
# @Time : 2021/2/4 18:29 
# @Author : Luciya 
# @File : test_calc_case1.py

import allure
import pytest
import yaml

with open("../data/calc.yml") as f:
    # 获取整个yaml文件参数
    datas = yaml.safe_load(f)
    # 获取加法参数
    add_data = datas['add']['add_datas']
    add_ids = datas['add']['add_ids']
    print(f"{add_data}, {add_ids}")
    print(add_data[0])
    print(add_ids[0])

    # 获取减法参数
    sub_data = datas['sub']['sub_datas']
    sub_ids = datas['sub']['sub_ids']
    print(f"{sub_data}, {sub_ids}")

    # 获取乘法参数
    mul_data = datas['mul']['mul_datas']
    mul_ids = datas['mul']['mul_ids']
    print(f"{mul_data}, {mul_ids}")

    # 获取除法参数
    div_data = datas['div']['div_datas']
    div_ids = datas['div']['div_ids']
    print(f"{div_data}, {div_ids}")


@pytest.fixture(params=add_data, ids=add_ids)
def get_add_datas(request):
    print("开始加法计算")
    data = request.param
    print(f"测试数据为：{data}")
    yield data
    print("结束加法计算")


@pytest.fixture(params=sub_data, ids=sub_ids)
def get_sub_datas(request):
    print("开始减法计算")
    data = request.param
    print(f"测试数据为：{data}")
    yield data
    print("结束减法计算")


@pytest.fixture(params=mul_data, ids=mul_ids)
def get_mul_datas(request):
    print("开始乘法计算")
    data = request.param
    print(f"测试数据为：{data}")
    yield data
    print("结束乘法计算")


@pytest.fixture(params=div_data, ids=div_ids)
def get_div_datas(request):
    print("开始除法计算")
    data = request.param
    print(f"测试数据为：{data}")
    yield data
    print("结束除法计算")

# 测试计算器类
@allure.feature("测试计算器类")
class TestCalc:


    @allure.story("加法测试案例")
    def test_add(self, get_calc, get_add_datas):
        """
        get_calc实例化计算器类
        get_add_datas:获取测试数据
        """
        with allure.step("计算两个数的和"):
            # 获取yaml文件内参数
            result = get_calc.add(get_add_datas[0], get_add_datas[1])
            # 如果相加数为float型 ，保留两位小数
        if isinstance(result, float):
            result = round(result, 2)
            # 结果添加断言
        assert result == get_add_datas[2]


    @allure.story("除法测试案例")
    def test_div(self, get_calc, get_div_datas,):
        """
        get_calc实例化计算器类
        get_div_datas:获取测试数据
        """
        with allure.step("计算两个数的相除结果"):
            # 获取yaml文件内参数
            result = get_calc.div(get_div_datas[0], get_div_datas[1])
            # 如果相加数为float型 ，保留两位小数
        if isinstance(result, float):
            result = round(result, 2)
            # 结果添加断言
        assert result == get_div_datas[2]


    @allure.story("加法测试案例")
    def test_sub(self, get_calc, get_sub_datas):
        """
        get_calc实例化计算器类
        get_sub_datas:获取测试数据
        """
        with allure.step("计算两个数的余"):
            # 获取yaml文件内参数
            result = get_calc.add(get_sub_datas[0], get_sub_datas[1])
            # 如果相加数为float型 ，保留两位小数
        if isinstance(result, float):
            result = round(result, 2)
            # 结果添加断言
        assert result == get_sub_datas[2]




    @allure.story("乘法测试案例")
    def test_add(self, get_calc, get_mul_datas):
        """
        get_calc实例化计算器类
        get_mul_datas:获取测试数据
        """
        with allure.step("计算两个数的积"):
            # 获取yaml文件内参数
            result = get_calc.add(get_mul_datas[0], get_mul_datas[1])
            # 如果相加数为float型 ，保留两位小数
        if isinstance(result, float):
            result = round(result, 2)
            # 结果添加断言
        assert result == get_mul_datas[2]
