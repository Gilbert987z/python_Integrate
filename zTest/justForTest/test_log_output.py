import sys

"""
将运行之后的控制框的输出信息 输出到 log日志中
"""
class Logger(object):
    def __init__(self, filename='default.log', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'w')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

print('12121')
sys.stdout = Logger('D:\\a.log', sys.stdout)
print('test111',sys.stdout)
sys.stderr = Logger('D:\\a.log_file', sys.stderr)
print('test222',sys.stderr )
print(1111)