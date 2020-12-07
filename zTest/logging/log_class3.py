#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhangjun
# @Date  : 2018/7/26 9:20
# @Desc  : Description

import logging
import logging.handlers
import os
import time


class Logger(object):
    def __init__(self, consoleLevel='DEBUG'):
        self.logger = logging.getLogger("")
        # 设置输出的等级
        # 级别
        # self.logger.setLevel(level)
        # 创建文件目录
        logs_dir = "py_log"
        if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
            pass
        else:
            os.mkdir(logs_dir)
        # 修改log保存位置
        timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
        logfilename = 'py_log%s.txt' % timestamp
        logfilepath = os.path.join(logs_dir, logfilename)
        rotatingFileHandler = logging.handlers.RotatingFileHandler(filename=logfilepath,
                                                                   maxBytes=1024 * 1024 * 50,
                                                                   backupCount=5)
        # 设置输出格式
        formatter = logging.Formatter('%(asctime)s %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')
        rotatingFileHandler.setFormatter(formatter)
        # 控制台句柄
        console = logging.StreamHandler()
        console.setLevel(consoleLevel)
        console.setFormatter(formatter)
        # 添加内容到日志句柄中
        self.logger.addHandler(rotatingFileHandler)
        self.logger.addHandler(console)
        self.logger.setLevel(logging.NOTSET)

    def getlog(self):
        return self.logger


if __name__ == '__main__':
    log = Logger(consoleLevel='INFO').getlog()
    log.critical('ere')
    log.debug('logger debug message')
    log.info('logger info message')
    log.warning('logger warning message')
    log.error('logger error message')
    log.critical('logger critical message')