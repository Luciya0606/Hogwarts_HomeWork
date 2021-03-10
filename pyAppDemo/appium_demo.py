# -*- coding: utf-8 -*- 
# @Time : 2021/3/1 22:36 
# @Author : Luciya 
# @File : appium_demo.py
from appium import webdriver

desire_caps = {
  "platformName": "Android",
  "deviceName": "127.0.0.0.1:7555",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".view.WelcomeActivityAlias",
  "appActivity": ".common.MainActivity",
  "noReset": False,
  "dontStopAppReset": True,
  "skipDeviceInitialization": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
driver.implicitly_wait(5)
el3 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el3.click()
el4 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el4.send_keys("alibaba")
el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
el5.click()
el6 = driver.find_element_by_id("com.xueqiu.android:id/action_delete_text")
el6.click()
el7 = driver.find_element_by_id("com.xueqiu.android:id/action_close")
driver.find_element_by_accessibility_id()
el7.click()
driver.quit()
