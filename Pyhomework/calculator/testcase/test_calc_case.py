# -*- coding: utf-8 -*- 
# @Time : 2021/2/4 16:11 
# @Author : Luciya 
# @File : test_calc_case.py
import allure
import pytest


# 测试计算器类
@allure.feature("测试计算器类")
class TestCalc:


    @allure.story("加法测试案例")
    @pytest.mark.run(order=1)
    # @pytest.mark.first
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
    @pytest.mark.run(order=4)
    # @pytest.mark.fourth
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


    @allure.story("减法测试案例")
    @pytest.mark.run(order=2)
    # @pytest.mark.second
    def test_sub(self, get_calc, get_sub_datas):
        """
        get_calc实例化计算器类
        get_sub_datas:获取测试数据
        """
        with allure.step("计算两个数的余"):
            # 获取yaml文件内参数
            result = get_calc.sub(get_sub_datas[0], get_sub_datas[1])
            # 如果相加数为float型 ，保留两位小数
        if isinstance(result, float):
            result = round(result, 2)
            # 结果添加断言
        assert result == get_sub_datas[2]

    @allure.story("乘法测试案例")
    @pytest.mark.run(order=3)
    # @pytest.mark.third
    def test_mul(self, get_calc, get_mul_datas):
        """
        get_calc实例化计算器类
        get_mul_datas:获取测试数据
        """
        with allure.step("计算两个数的积"):
            # 获取yaml文件内参数
            result = get_calc.mul(get_mul_datas[0], get_mul_datas[1])
            # 如果相加数为float型 ，保留两位小数
        if isinstance(result, float):
            result = round(result, 2)
            # 结果添加断言
        assert result == get_mul_datas[2]

