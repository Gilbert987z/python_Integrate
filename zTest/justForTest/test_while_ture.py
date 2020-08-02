'''
while True:
    try:
        num = int(input('请输入一个整数：'))
        break
    except ValueError:
        print('输入的不是整数，请重新输入')
'''

while True:
    try:
        num = int(input('请输入一个整数：'))
        assert num == 2
        print('输入正确')
        break
    except AssertionError:
        print('输入的不正确，请重新输入')
    except ValueError:
        print('输入的不是整数，请重新输入')
