import logging
from logging.handlers import RotatingFileHandler

class MyLoggerV2(logging.Logger):

    def __init__(self, name, level='DEBUG', file=None, encoding='utf-8'):

        # 日志收集器
        # self.logger = logging.getLogger(name)
        super().__init__(name) # Logger(name)
        # 级别
        self.setLevel(level)
        # 格式
        fmt = '%(asctime)s %(filename)s %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s'
        ft = logging.Formatter(fmt)
        # 初始化输出渠道
        if file:
            file_handle = RotatingFileHandler(file, encoding, maxBytes=1024*1024*10, backupCount=10)
            file_handle.setLevel('INFO')
            file_handle.setFormatter(ft)
            self.addHandler(file_handle)
        # 设置handle2
        h2 = logging.StreamHandler()
        h2.setFormatter(ft)
        # 将handle添加到logger
        self.addHandler(h2)

l = MyLoggerV2(name='haha', file='test1.log')
l.info('info级别')