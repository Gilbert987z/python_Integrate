# content of test_sample.py
import pytest

'''
在测试文件test_sample.py所在的目录下，运行py.test即可。
pytest会在当前的目录下，寻找以test开头的文件（即测试文件），
找到测试文件之后，进入到测试文件中寻找test_开头的测试函数并执行。
'''

def func(x):
    return x + 1


def test_func():    #自动找test_开头的测试函数执行
    assert func(3) == 5

