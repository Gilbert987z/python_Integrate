import requests
import time
import json

'''
PC端-开瑞新能源管理平台-远程寻车功能
'''
proxy_addr = {
    # 'https': 'https://127.0.0.1:8888',  # 本地fiddler代理端口
    # 'http': 'http://127.0.0.1:8888'
}


# 登录开瑞新能源管理平台
def login_chery():
    print("------登录开瑞新能源管理平台--------")
    url = chery_url + "api/signin"
    data = {
        "password": "yundong123",
        "userName": "yundong"
    }
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    r_login = requests.post(url=url, data=json.dumps(data),headers=header,proxies=proxy_addr)  # post请求

    print("状态码：", r_login.status_code)  # 打印返回的状态码
    print("打印正文：", r_login.text)  # 打印返回的正文
    cookies = requests.utils.dict_from_cookiejar(r_login.cookies)
    return cookies  # 返回cookie的值


# 远程控制-VIN搜索
def remote_control_getvin():
    print('------远程控制-VIN搜索--------')
    url = chery_url + 'api/getJVehInfo'
    params = {
        'vin': VIN
    }

    r = requests.get(url=url, params=params, cookies=cookies,proxies=proxy_addr)
    print("状态码：", r.status_code)  # 打印返回的状态码
    print("打印正文：", r.text)  # 打印返回的正文

    jsonData = json.loads(r.text)
    response_vin = jsonData.get('data').get('vin')  # 获取得到vin
    return response_vin


# 远程控制-远程寻车
def remote_control_sendcommandfuel():
    print('------远程控制-远程寻车--------')
    url = chery_url + 'api/sendCommandFuel'
    data = {"deviceId": VIN, "cmdCode": "00122", "dataSources": "tsp", "webSocketNum": "", "operationMode": "FV",
            "operator": "yundong", "appId": "999",
            "params": "[{\"code\":\"encryptionModel\",\"value\":\"NONE\"},{\"code\":\"seekWay\",\"value\":0}]"}

    r = requests.post(url=url, data=data, cookies=cookies,proxies=proxy_addr)
    print("状态码：", r.status_code)  # 打印返回的状态码
    print("打印正文：", r.text)  # 打印返回的正文


if __name__ == '__main__':
    chery_url = "http://nev.mychery.com/"
    process_num = 1  # 程序进行了多少次

    try:
        flag = True
        while flag:
            print('#捷途车联网管理平台-远程寻车功能#')
            cookies = login_chery()  # 登录并保存cookie

            # 输入VIN的校验
            while True:
                try:
                    VIN = input('请输入VIN(例子：X70TESTVIN0000038):')  # X70TESTVIN0000038
                    if VIN == remote_control_getvin():
                        break
                except BaseException:
                    print('ERROR:没有对应的VIN码，请重新输入！')

            # 输入循环次数的校验的校验
            while True:
                try:
                    num = int(input('请输入循环次数:'))
                    if num >= 1:
                        break
                    else:
                        print('ERROR:输入错误，要求输入数字为正整数，请重新输入！')
                except BaseException:
                    print('ERROR:输入错误，要求输入为正整数，请重新输入！')

            # 输入循环多少秒的校验的校验
            while True:
                try:
                    times = int(input('每次循环大概多少秒：'))
                    if times >= 1:
                        break
                    else:
                        print('ERROR:输入错误，要求输入数字为正整数，请重新输入！')
                except BaseException:
                    print('\nERROR:输入错误，要求输入为正整数，请重新输入！')

            for num in range(1, num + 1):
                print('\n####开启第%d次循环####' % num)
                remote_control_sendcommandfuel()  # 远程控制-远程寻车

                print('\n开始读秒（10秒输出一次，共%d秒）' % times)
                for cycle_time in range(0, times + 1, 10):
                    print('%ds ' % cycle_time, end='', flush=True)
                    time.sleep(10)  # 睡眠10秒

                print('\n####结束第%d次循环####' % num)

            print('\n<<<<循环完毕>>>>')

            print('\n请输入\"exit\"或\"1\"。exit为结束运行,并关闭当前窗口，1为重新运行程序')
            while True:
                try:
                    flag = input("请输入你的选择:")  # str型的

                    if flag == '1':
                        process_num = process_num+1
                        print('\n<<<<重新执行程序-%d>>>>' % process_num)
                        break
                    elif flag == 'exit':
                        print('\n<<<<正在关闭当前窗口>>>>')
                        break
                    else:
                        print('ERROR:输入错误，请重新输入！')
                except BaseException:
                    print('ERROR:输入错误，请重新输入！')

            if flag == 1:
                flag = True
            elif flag == 'exit':
                for times in range(1, 6):
                    print('。', end='', flush=True)
                    time.sleep(1)  # 睡眠1秒
                break
    except Exception as e:   #抓取所有的报错信息
        print(e)
        time.sleep(999999)