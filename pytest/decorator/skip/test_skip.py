import pytest

#教程https://blog.csdn.net/maoxuexue/article/details/106114771
'''def func(x):
    return x + 1


def test_func():    #自动找test_开头的测试函数执行
    assert func(3) == 5'''


@pytest.mark.skip(reason='feature not implemented')
def test_1():
    pass
