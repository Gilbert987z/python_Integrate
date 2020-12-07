# -*- coding:utf-8 -*-

import time




def timestamp_to_date(timestamp):
    """13位时间戳转换为日期格式字符串"""
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp / 1000))

def date_to_timestamp(date):
    """日期格式字符串转换为13位时间戳"""
    return int(round(date * 1000))

if __name__ == "__main__":
    print(timestamp_to_date(1598073319837))
   # print(date_to_timestamp('2020-08-22 13:15:19'))
    print(time.time())
    print(int(round(time.time() * 1000)))
    print()