# coding = utf-8

import requests
import json

#
# 奇瑞捷途日志页面
#

log_url = 'http://120.77.62.245:50016'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
}

proxy_addr = {
    # 'https': 'https://127.0.0.1:8888',  # 本地fiddler代理端口
    # 'http': 'http://127.0.0.1:8888'
}

#todo  由于log页面防抓包了，

class LogPage():

    # 登录开瑞新能源管理平台
    def login_log(userName, password):
        '''
        接口：登录开瑞新能源管理平台
        '''
        print('------登录开瑞新能源管理平台--------')
        url = log_url + "/api/signin"
        data = {
            "password": password,
            "userName": userName
        }
        header['Content-Type'] = 'application/json;charset=UTF-8'  #

        r = requests.post(url=url, data=json.dumps(data), headers=header, proxies=proxy_addr)  # post请求

        print("状态码：", r.status_code)  # 打印返回的状态码
        print("打印正文：", r.text)  # 打印返回的正文

        cookies = requests.utils.dict_from_cookiejar(r.cookies)
        return cookies

    # 创建升级任务-查询vin
    def log_download(cookies, VIN):
        '''
        接口：创建升级任务-查询vin
        '''
        print('------创建升级任务-查询vin--------')
        url = log_url + '/api/queryOtaList'

        params = {
            'pageIndex': 1,
            'pageSize': 10,
            'vin': VIN,
            'unitId': 15,
            'unitName': 'TBOX',
            'flag': False
        }

        r = requests.get(url=url, params=params, cookies=cookies, headers=header, proxies=proxy_addr)

        print("状态码：", r.status_code)  # 打印返回的状态码
        print("打印正文：", r.text)  # 打印返回的正文

        jsonData = json.loads(r.text)
        search_vin_datas = jsonData.get('datas')[0]  # 接口返回的datas信息
        return search_vin_datas
