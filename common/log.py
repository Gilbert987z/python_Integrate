
import logging
import logging.handlers
import os
import time


class Logger(object):
    def __init__(self, log_name='python_log', console_level='INFO',log_level='INFO'):
        self.logger = logging.getLogger("")
        # 设置输出的等级
        # 级别
        # self.logger.setLevel(level)
        # 创建文件目录
        logs_dir = "python_log"
        if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
            pass
        else:
            os.mkdir(logs_dir)
        # 修改log保存位置
        timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
        logfilename = '%s%s.txt' % (log_name,timestamp)
        logfilepath = os.path.join(logs_dir, logfilename)

        rotatingFileHandler = logging.handlers.RotatingFileHandler(filename=logfilepath,
                                                                   maxBytes=1024 * 1024 * 50,
                                                                   backupCount=5)
        # 设置输出格式
        formatter = logging.Formatter('%(asctime)s %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s] %(message)s')
        rotatingFileHandler.setFormatter(formatter)
        # 控制台句柄
        console = logging.StreamHandler()
        console.setLevel(console_level)
        console.setFormatter(formatter)
        # 添加内容到日志句柄中
        self.logger.addHandler(rotatingFileHandler)
        self.logger.addHandler(console)
        # self.logger.setLevel(logging.NOTSET)
        self.logger.setLevel(log_level)  #默认输出到log日志里的是INFO

    def get_log(self):
        return self.logger


#外部直接导入，直接调用就可以了
log = Logger(log_name='JAC_OTA', console_level='INFO', log_level='INFO').get_log()


if __name__ == '__main__':
    log = Logger(console_level='INFO').get_log()
    log.debug('logger debug message') #详细信息，一般只在调试问题时使用。
    log.info('logger info message') #证明事情按预期工作。
    log.warning('logger warning message') #某些没有预料到的事件的提示，或者在将来可能会出现的问题提示。例如：磁盘空间不足。但是软件还是会照常运行
    log.error('logger error message') #由于更严重的问题，软件已不能执行一些功能了
    log.critical('logger critical message') #由于更严重的问题，软件已不能执行一些功能了