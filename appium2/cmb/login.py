# coding=utf-8
import time
from cmb.setting.driver import *
import pytest
# from appium import webdriver
# from appium.webdriver.common.touch_action import TouchAction
#
# desired_caps = {
#     "platformName": "Android",
#     "deviceName": "f7c5caec",
#     "platformVersion": "6.0",
#     "appPackage": "com.idougong.caipifa",
#     "appActivity": "com.idougong.caipifa.module.ui.FlickerScreenActivity",
#     "unicodeKeyboard": True,
#     "resetKeyboard": True}  # 隐藏键盘
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

driver.implicitly_wait(10)
print ("智能等待时间结束")

timestr = time.strftime('%Y-%m-%d_%H_%M_%S')  # 定义截图名称即时间戳，字符串类型
driver.get_screenshot_as_file('C://Users//Administrator//Desktop//' + timestr + '.png')
print ("上传截图成功")

driver.implicitly_wait(10)
print ("智能等待时间结束")


try:
    print("输入手机号码")
    driver.find_element_by_id('com.idougong.caipifa:id/et_phone').send_keys(17376597890)
    print("输入验证码")
    driver.find_element_by_id('com.idougong.caipifa:id/et_code_show').send_keys(9526)
    print("点击登录")
    driver.find_element_by_id('com.idougong.caipifa:id/tv_user_login').click()
except:
    driver.implicitly_wait(10)
    print("登录失败")
    driver.get_screenshot_as_file('C://Users//Administrator//Desktop//' + timestr + '.png')
    print("失败截图")