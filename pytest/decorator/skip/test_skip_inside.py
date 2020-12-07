import pytest


def test_2():
    if 1 < 2:
        pytest.skip('1111111')   # 可以用于测试函数里，跳过测试用例
    pass
