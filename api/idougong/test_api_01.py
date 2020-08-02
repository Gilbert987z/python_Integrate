import requests

'''
PC端-工地管理员登录
'''
'''
url = "http://gyj-dev-api.idougong.com/biz/login"
params = {
    "mobile": "17376597890",
    "smsCode": "idougong"
}

r = requests.post(url=url, params=params)  # post请求    r指的是response

print(r.text)  # 打印返回的正文
print(r.status_code)  # 打印返回的状态码
print(r.cookies)  # 打印返回的cookie
print(r.url)  # url值

'''


'''
PC端-菜买办-管理员登录
'''

url1 = "http://cdd-dev-api.idougong.com/admin/user/sms/login"
params1 = {
    "phone": "17376597890",
    "username": "17376597890",
    "password": "123456",
    "smsCode": "idougong"
}

r1 = requests.post(url=url1, params=params1)  # post请求
print()
session = requests.session()
print(session)
print(r1.text)  # 打印返回的正文
print(r1.status_code)  # 打印返回的状态码
print(r1.cookies)  # 打印返回的cookie
print(r1.url)  # url值

cookies = requests.utils.dict_from_cookiejar(r1.cookies)
print('cookies')
print(cookies)
print(cookies.keys())
for key in cookies.keys():
    print(key, cookies.get(key))
print(cookies.get(key))
print("SESSION="+cookies.get(key))
'''
PC端-菜买办-商家认证
'''

url2 = "http://cdd-dev-api.idougong.com/v2/admin/shop/getShopListAuditStateOrPhone?pageSize=20&pageNum=1"

headers = {
    "User_Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    ,"Cookie": "SESSION="+cookies.get(key)
}
r2 = requests.get(url=url2, headers=headers)  # get请求

print(r2.text)  # 打印返回的正文
print(r2.status_code)  # 打印返回的状态码
print(r2.cookies)  # 打印返回的cookie
print(r2.url)  # url值
