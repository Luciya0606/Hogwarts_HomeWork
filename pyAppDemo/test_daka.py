# -*- coding: utf-8 -*- 
# @Time : 2021/3/3 14:41 
# @Author : Luciya 
# @File : test_daka.py
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestTouchAction:
    def setup(self):
        disert_caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            # "appActivity": ".view.WelcomeActivityAlias",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": True,
            "dontStopAppReset": True,
            "skipDeviceInitialization": True,
            "unicodeKeyBoard": True,
            "resetKeyBoard": True,
            "settings[waitForIdleTimeout]": 0
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", disert_caps)
        self.driver.implicitly_wait(10)


    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                       'new UiScrollable(new UiSelector().'
                                       'scrollable(true).instance(0)).'
                                       'scrollIntoView(new UiSelector().'
                                       f'text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")
