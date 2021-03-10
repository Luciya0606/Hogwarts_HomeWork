# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 16:46 
# @Author : Luciya 
# @File : app.py
from appium import webdriver

from pyAppDemo.pages.information_page import InformationPage


class App:
    def __init__(self):
        self.driver = None
        self.start()

    def start(self):
        caps = {
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
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def goto_main(self):
        return InformationPage(self.driver)