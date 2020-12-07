import requests

def download_pic_by_url(url):
    requests.packages.urllib3.disable_warnings()
    r = requests.get(url, verify = False)

    # 将获取到的图片二进制流写入本地文件
    with open('./validateCode/pictures3.png', 'wb') as f:
        # 对于图片类型的通过r.content方式访问响应内容，将响应内容写入baidu.png中
        f.write(r.content)