#coding=utf-8
from element import *

#
# 检查点模块
#

def l_success_check():
    if l_success_text() == u'''×
登录成功''':
        print 'Pass'
    else:
        print 'Fail'


def l_fail_check():
    if l_fail_text() == u'''×
用户名或密码错误！''':
        print 'Pass'
    elif l_fail_text() == u'''×
请正确输入用户名和密码！''':
        print 'Pass'
    else:
        print 'Fail'