import requests

proxy_addr = {
    'https': 'https://127.0.0.1:8888',  # 本地jmeter代理端口
    'http': 'http://127.0.0.1:8888'
}

'''
PC端-菜买办-管理员登录
'''

url1 = "https://cdd-dev-api.idougong.com/admin/user/sms/login"
params1 = {
    "phone": "17376597890",
    "username": "17376597890",
    "password": "123456",
    "smsCode": "idougong"
}

r1 = requests.post(url=url1, params=params1, proxies=proxy_addr, verify=False)  # post请求
print()
session = requests.session()
print(session)
print(r1.text)  # 打印返回的正文
print(r1.status_code)  # 打印返回的状态码
print(r1.cookies)  # 打印返回的cookie
print(r1.url)  # url值
print(r1.encoding)  # 编码
