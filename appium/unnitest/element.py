# coding=utf-8
import time
from selenium import webdriver  # 导入selenium中的webdriver包

#
# 元素模块
#

browse = webdriver.Chrome()  # 通过webdriver调出谷歌Chrome浏览器
browse.maximize_window()  # 将浏览器窗口最大化
browse.get('http://192.168.0.212/wk')  # 输入CRM系统URL


def l_submit(username, pwd):
    browse.find_element_by_name('name').send_keys(username)  # 输入用户名
    browse.find_element_by_name('password').send_keys(pwd)  # 输入密码
    browse.find_element_by_name('submit').click()  # 点击登录


def l_success_text():
    t_success = browse.find_element_by_class_name('alert-success').text
    return t_success


def l_fail_text():
    t_error = browse.find_element_by_class_name('alert-error').text
    return t_error


def l_quite():
    browse.find_element_by_class_name('avatar').click()
    browse.find_element_by_css_selector('a[href="/wk/index.php?m=user&a=logout"]').click()
    time.sleep(3)