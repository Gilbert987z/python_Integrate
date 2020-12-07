import pytest

if 1 == 1:
    pytest.skip('skip all tests', allow_module_level=True)


def test_1():
    pass


def test_2():
    pass
