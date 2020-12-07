# -*- coding:utf-8 -*-

import time


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


def get_delta(t1, t2):
    """
    :param t1: 13位时间戳
    :param t2: 13位时间戳
    :return: 两个时间戳相减，返回秒数
    """
    res = int((t2 - t1) / 1000)
    return res


def millisecond_to_time(millis):
    """13位时间戳转换为日期格式字符串"""
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(millis / 1000))


if __name__ == "__main__":
    print(get_second()) #当前时间戳
    print(time.time())
    time1 = get_millisecond()
    print(time1)

    k1 = 1567412375458
    k2 = 1567412395853

    now = int(round(time.time() * 1000))
    print(now)
    t1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(k1 / 1000))
    t2 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(k2 / 1000))
    print(t1)
    print(t2)
    print(get_delta(k1, k2))
