# -*- coding: utf-8 -*-
# @Time : 2021/3/6 14:43 
# @Author : Luciya 
# @File : app.py
from appium import webdriver
from Pyhomework.wxOaHomework.pages.information import Information


class App:
    def __init__(self):
        self.driver = None
        self.start()

    def start(self):
            caps = {}
            caps["platformName"] = "Android",
            caps["deviceName"] = "127.0.0.1:7555",
            caps["appPackage"] = "com.tencent.wework",
            caps["appActivity"] = ".launch.LaunchSplashActivity",
            caps["autoGrantPermissions"] = True
            # 不清空缓存启动app
            caps["noReset"] = "true"
            # 设置等待页面空闲状态时间0s,可用来处理动态页面
            caps['settings[waitForIdleTimeout]'] = 0
            print(caps)
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(10)


    def goto_information(self):
        # 传入driver以便于复用
        return Information(self.driver)