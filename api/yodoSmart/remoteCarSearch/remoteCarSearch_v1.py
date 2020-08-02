import requests

'''
PC端-开瑞新能源管理平台-远程寻车功能
'''

# 全局变量
VIN = 'X70TESTVIN0000038'

# 登录开瑞新能源管理平台
print('------登录开瑞新能源管理平台--------')
url = "http://116.236.19.122:12702/api/signin"
data = {
    "password": "yundong123",
    "userName": "yundong"
}

r_login = requests.post(url=url, data=data)  # post请求

print("状态码：", r_login.status_code)  # 打印返回的状态码
print("打印正文", r_login.text)  # 打印返回的正文

cookies = requests.utils.dict_from_cookiejar(r_login.cookies)

# #远程控制-VIN搜索
# print('------登录开瑞新能源管理平台--------')
# url = 'http://116.236.19.122:12702/api/getJVehInfo'
#
# params={
#     'vin':VIN
# }
# r = requests.get(url=url,params=params,cookies=cookies)
# print("状态码：", r.status_code)  # 打印返回的状态码
# print("打印正文", r.text)  # 打印返回的正文

# 远程控制-远程寻车
print('------远程控制-远程寻车--------')
url = 'http://116.236.19.122:12702/api/sendCommandFuel'
data = {"deviceId": VIN, "cmdCode": "00122", "dataSources": "tsp", "webSocketNum": "", "operationMode": "FV",
        "operator": "yundong", "appId": "999",
        "params": "[{\"code\":\"encryptionModel\",\"value\":\"NONE\"},{\"code\":\"seekWay\",\"value\":0}]"}

r = requests.post(url=url, data=data, cookies=cookies)
print("状态码：", r.status_code)  # 打印返回的状态码
print("打印正文", r.text)  # 打印返回的正文
