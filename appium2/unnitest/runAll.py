# -*- coding:UTF-8 -*-
from case import *
from unittest import TestSuite, makeSuite
from HTMLTestRunner import HTMLTestRunner  # 需要将HTMLTestRunner文件放到C:Python\Lib目录下

#
# 执行脚本模块
#

T = TestSuite()

T.addTest(makeSuite(Login))  # 执行所有Login类的测试用例
# T.addTest(Login('test1')) #分别执行Login类的测试用例的test1
# T.addTest(Login('test2'))
# T.addTest(Login('test3'))
# T.addTest(Login('test4'))
fp = file('./result.html', 'wb')
fb = HTMLTestRunner(fp, title=u'自动化测试报告', description=u'测试用例执行结果：')
fb.run(T)
fp.close()

