# content of test_expectation.py

# coding:utf-8


import pytest

test_input = [("3+5", 8),("2+4", 6),("6 * 9", 42), ]
# @pytest.mark.parametrize("test_input,expected",
#                          [("3+5", 8),
#                           ("2+4", 6),
#                           ("6 * 9", 42),
#                          ])
@pytest.mark.parametrize("test_input,expected",test_input)
def test_eval(test_input, expected):
    assert eval(test_input) == expected

if __name__ == "__main__":
    pytest.main(["-s", "test_parameter1.py"])