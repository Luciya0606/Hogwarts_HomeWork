# -*- coding: utf-8 -*- 
# @Time : 2021/3/2 17:35 
# @Author : Luciya 
# @File : test_dwpytest.py
from time import sleep

import allure
from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
import hamcrest
from hamcrest import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDW:
    def setup(self):
        disert_caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            # "appActivity": ".view.WelcomeActivityAlias",
            "appActivity": ".common.MainActivity",
            # "noReset": False,
            # "dontStopAppReset": True,
            "skipDeviceInitialization": True,
            "unicodeKeyBoard": True,
            "resetKeyBoard": True,
            # Android引擎
            "automationName": "uiautomator2"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", disert_caps)
        self.driver.implicitly_wait(5)

    # def teardown(self):
    #     self.driver.quit()

    # 控件定位
    def test_search(self):
        print("搜索测试用例")
        """
        1.打开雪球APP
        2.点击搜索框
        3.向搜索框输入“alibaba”
        4.在搜索结果选择“阿里巴巴” ，然后点击
        5.获取这只上香港股市的阿里巴巴，并判断这只股价是否>200        
        """
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        # el3 = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        sleep(5)
        el4 = self.driver.find_element_by_xpath("//*[@text='阿里巴巴']").click()
        # el5 = self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']")
        # self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
        print("搜索成功")
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/stock_current_price").text)
        assert current_price > 200

    # 控件交互
    def test_attr(self):
        """
        1.打开雪球应用
        2.定位首页的搜索框
        3.判断搜索框是否可用，并查看搜索框name属性值
        4.打印搜索框这个元素的左上角坐标和他的高度
        5.向搜索框输入：alibaba
        6.判断【阿里巴巴】是否可见
        7.如果可见，打印搜索成功点击，如果不可见，打印搜索失败
        ：return
        """
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        search_enabled = el1.is_enabled()
        print(el1.text)
        print(el1.location)
        print(el1.size)
        if search_enabled == True:
            el1.click()
            el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            # alibaba_el2 = self.driver.find_element_by_xpath("//*[@class='android.widget.TextView' and @text='阿里巴巴']")
            alibaba_el2 = self.driver.find_element_by_xpath("//*[@text='阿里巴巴']")
            # 通过get_attribute 可以获取元素的所有属性
            print(alibaba_el2.get_attribute("displayed"))
            alibaba_displayed = alibaba_el2.get_attribute("displayed")
            if alibaba_displayed == "true":
                print("搜索成功")
            else:
                print("搜索失败")



    def test_touch_action(self):
        action = TouchAction(self.driver)
        """
        手势滑动
        获取当前屏幕的尺寸 灵活使用易于复用
        直接写坐标点不易于维护
        """
        print(self.driver.get_window_rect())
        width = self.driver.get_window_rect()['width']
        height = self.driver.get_window_rect()['height']
        x1 = int(width/2)
        y_start = int(height * 4/5)
        y_end = int(height * 1/5)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()

    def test_getprice(self):
        """
        Xpath 父子关系定位
        打开雪球APP
        搜索 阿里巴巴
        从搜索结果查找，阿里巴巴香港股票的价格
        """
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        el3 = self.driver.find_element_by_xpath("//*[@text='阿里巴巴-SW']")
        locator = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        # 显示等待作用于前端指定的方法 until和until_not
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        WebDriverWait(self.driver, 10).until( lambda x: x.find_element(*locator))
        # current_price = float(self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text)
        current_price = float(self.driver.find_element(*locator).text)
        print(current_price)
        assert current_price > 200

    def test_myinfo_login(self):
        """
        uiautomatorviwer 定位 Android原生定位方式 写法稍复杂 但是运行时间快
        1.点击我的 进入到个人信息页面
        2.点击登录 进入到登录页面
        3.输入用户名和密码
        4.点击登录
        """
        """
        组合定位
        """
        # el1 = self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        # 该方式属于组合定位 id与text组合
        el1 = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")').click()
        # 该方式属于 父子关系定位
        el2 = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/rl_login").childSelector(text("登录雪球"))').click()
        # el2 = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("登录")').click()
        el3 = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("17688843100")
        el4 = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("123456")
        el5 = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

    @allure.story("滑动定位")
    def test_scroll_find_element(self):
        el1 = self.driver.find_element(MobileBy.XPATH, "//*[@text='热门']/..//*[@resource-id='com.xueqiu.android:id/title_text']").click()
        sleep(5)
        # el2 = self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
        #                                                       'scrollable(true).instance(0)).'
        #                                                       'scrollIntoView(new UiSelector().text("专栏    如果美股崩了，A股会怎样？").instance(0));').click()
        el2 = self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0));')
        sleep(5)

    @allure.story("定位简易消息框")
    def test_toast_element(self):
        pass

    @allure.story("获取元素属性")
    def test_getattr(self):
        # search_el1 = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search")
        sleep(10)
        search_el1 = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/home_search']")
        print(search_el1.get_attribute("content-desc"))
        print(search_el1.get_attribute("resource-id"))
        print(search_el1.get_attribute("enabled"))


    def test_hamcrest_demo(self):
        assert_that(10, equal_to(10), "这是一个提示")
        # 上下浮动
        assert_that(12, close_to(10, 2))
        assert_that("cantians having string", contains_string("string"))

