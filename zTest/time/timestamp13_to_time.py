# -*- coding:utf-8 -*-

import time




def millisecond_to_time(millis):
    """13位时间戳转换为日期格式字符串"""
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(millis / 1000))


if __name__ == "__main__":


    createTime=1599556509836 #2020-09-08 17:07:37 2020-09-08 17:09:04
                            #2020-09-06 17:10:04 2020-09-08 17:10:53
                            #2020-09-06 17:15:09 2020-09-08 17:15:09
    # now = int(round(time.time() * 1000))
    # print(now)


    t3 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(createTime / 1000))
    # t3 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now / 1000))
    print(t3)