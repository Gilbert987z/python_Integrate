# -*- coding:utf-8 -*-

import time


def now():
    '''
    :return:当前时间
    '''
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def get_second():
    """
    :return: 获取精确到秒时间戳，10位
    """
    return int(time.time())


def get_millisecond():
    """
    :return: 获取精确毫秒时间戳,13位
    """
    millis = int(round(time.time() * 1000))
    return millis


def timestamp13_to_time(timestamp13):
    """13位时间戳转换为日期格式字符串"""
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp13 / 1000))



if __name__ == '__main__':
    print(now())