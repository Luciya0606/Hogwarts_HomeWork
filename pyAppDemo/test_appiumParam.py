# -*- coding: utf-8 -*- 
# @Time : 2021/3/4 14:48 
# @Author : Luciya 
# @File : test_appiumParam.py
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *
from selenium.webdriver.support.wait import WebDriverWait


class TestAppParam:
    def setup(self):
        desire_caps={
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            # "appActivity": ".view.WelcomeActivityAlias",
            "appActivity": ".common.MainActivity",
            "noReset": False,
            "dontStopAppReset": True,
            "skipDeviceInitialization": True,
            "unicodeKeyBoard": True,
            "resetKeyBoard": True,
            "automationName": "uiautomator2"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass

    @pytest.mark.parametrize('searchKeys', [('alibaba')])
    def test_search_param(self, searchKeys):
        el1 = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        el2 = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(searchKeys)
        el3 = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/name")
        locator = "//*[@text='阿里巴巴']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']"
        WebDriverWait(self.driver, 10).until(lambda x:x.find_element(*locator))
        # el4_price = self.driver.find_element_by_xpath("//*[@text='阿里巴巴']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        el4_price = self.driver.find_element(MobileBy.XPATH, *locator).text
        print(el4_price)
        expect_price = 200
        assert_that(el4_price, close_to(expect_price, expect_price*0.1))

