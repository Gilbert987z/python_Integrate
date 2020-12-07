# content of test_class.py
class TestClass:
    def test_one(self):
        print(111111111)
        x = "check"
        assert 'h' in x,'不在'

    def test_two(self):
        print(2222222222)
        x = "hello"
        assert hasattr(x, 'check')  # hasattr() 函数用于判断对象是否包含对应的属性。


