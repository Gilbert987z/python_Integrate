import pytest

android_sys = 6.0


# 条件表达式成立，此用例会被跳过
@pytest.mark.skipif(condition='android_sys > 5.0', reason='feature not implemented')
def test_1():
    assert 1 == 1

