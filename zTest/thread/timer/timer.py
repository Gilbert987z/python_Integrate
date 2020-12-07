# encoding: UTF-8
'''
线程延迟5秒后执行。
'''

import threading

def func():
    print ('hello timer!')

timer = threading.Timer(5, func)
timer.start()