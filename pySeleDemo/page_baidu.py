# -*- coding: utf-8 -*- 
# @Time : 2021/3/5 12:51 
# @Author : Luciya 
# @File : page_baidu.py
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pySeleDemo.base import Base


class PageBaidu(Base):
    """
    窗口切换
    打开百度页面
    点击登录
    弹框中点击 立即注册 输入账户和密码
    返回刚才的登录页 点击登录
    输入用户名和密码 点击登录
    """
    def goto_login(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.current_window_handle)
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)
        windows = self.driver.window_handles
        # 无法直接进行定位 需要切换窗口
        self.driver.switch_to.window(windows[-1])
        # self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("luciya")
        sleep(3)
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("17688843100")
        sleep(3)
        # 打印完切换回之前的窗口
        self.driver.switch_to.window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        locator_username = self.driver.find_element(By.ID, "TANGRAM__PSP_11__userName").send_keys("17688843100")
        sleep(3)
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator_username))
        locator_password = self.driver.find_element(By.ID, "TANGRAM__PSP_11__password").send_keys("123456")
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator_password))
        sleep(3)
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()




    def goto_switch_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 切换frame
        self.driver.switch_to.frame("iframeResult")
        self.driver.find_element(By.ID, "draggable").text
        # 切换到父类frame
        self.driver.switch_to.parent_frame()
        # 表示默认的一个frame节点
        # self.driver.switch_to.default_content()
        self.driver.find_element(By.ID, "submitBTN").click()


    def goto_test_js(self):
        self.driver.get("https://www.baidu.com")
        js1 = 'return document.getElementById("kw")'
        el1 = self.driver.execute_script(js1)



