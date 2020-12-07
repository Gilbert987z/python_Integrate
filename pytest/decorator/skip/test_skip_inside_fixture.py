import pytest


@pytest.fixture()
def fix():
    if 1 < 2:
        pytest.skip('1111111')


def test_2(fix):
    pass
