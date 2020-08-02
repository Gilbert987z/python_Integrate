import requests



'''
PC端-工友家-工地的管理员登录
'''

url = "http://gyj-dev-api.idougong.com/biz/login"
params = {
    "mobile": "17376597890",
    "smsCode": "idougong"
}

response = requests.post(url=url, params=params)  # post请求    r指的是response

print(response.text)  # 打印返回的正文
print(response.status_code)  # 打印返回的状态码
print(response.cookies)  # 打印返回的cookie
print(response.url)  # url值
