# D:/YOYO/test_class.py

#** 作者：上海-悠悠 QQ交流群：588402570**

import pytest

class TestClass:
        def test_one(self):
            x = "this"
            assert 'h' in x

        def test_two(self):
            x = "hello"
            assert hasattr(x, 'check')

        def test_three(self):
            a = "hello"
            b = "hello world"
            assert a in b

if __name__ == "__main__":
    pytest.main('-q test_class.py')