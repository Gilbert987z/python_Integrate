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


'''
PC端-工友家-上传图片
'''
# Content-Disposition: form-data; name="file"; filename="zTest.jpg"
# Content-Type: image/jpeg
proxy_addr = {
    'https': 'https://127.0.0.1:8888',  # 本地shadowsocks代理端口
    'http': 'http://127.0.0.1:8888'
}

url = "http://gyj-dev-api.idougong.com/admin/upload/uploadImage"

files = {
    'file': ('test2.jpg', open(r'C:\Users\ASUS\Pictures\test2.jpg', 'rb'), 'image/jpeg')
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Cookie': 'SESSION=Y2E3ZDk0YWUtYTM1ZS00MjVhLTg3NDQtNTE4MjEyMTBjMzdh'
}

data = {
    'type': '2'
}


response = requests.post(url=url, files=files, headers=header, proxies=proxy_addr, data=data, timeout=2)  # post请求

print(response.text)  # 打印返回的正文
# print(response.status_code)  # 打印返回的状态码
# print(response.cookies)  # 打印返回的cookie
# print(response.url)  # url值
# print(response.json())
