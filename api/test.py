import requests

class HttpRequests:
    def __init__(self,url, params=None,headers=None,json=None):
        self.url = url
        self.params = params
        self.headers = headers
        self.json = json
    def http_requests(self,method,cookies = None):
        if method.upper() == "GET":
            try:
                res = requests.get(self.url, verify=False,params=self.params,headers=self.headers, cookies=cookies)
                print("url:{}的get请求执行成功".format(self.url))
            except Exception as e:
                res = e
        elif method.upper() == "POST":
            try:
                res = requests.post(self.url, verify=False,data=self.params, headers=self.headers, json=self.json, cookies=cookies)
            except Exception as e:
                res =e
        else:
            res = "请求方式不正确"
        return res
if __name__ == "__main__":
    url = "http://v.juhe.cn/weather/index"
    params = {"cityname":"%E8%8B%8F%E5%B7%9E","key":"d04661ce6f125719ef23c193deedd840"}
    res = HttpRequests(url,params).http_requests("get").json()
    print(res)
    if res["reason"]=="查询成功":
        print("请求正确")
    else:
        print("请求错误")
