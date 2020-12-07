# -*- coding:utf-8 -*-

import time


def timestamp13_to_time(timestamp13):
    """13位时间戳转换为日期格式字符串"""
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp13 / 1000))



