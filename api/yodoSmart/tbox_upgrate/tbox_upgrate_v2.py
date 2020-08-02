import requests
import json

'''
PC端-开瑞新能源管理平台-tbox升级
'''

# 全局变量
VIN = input('请输入VIN:')
taskName = input('请输入任务名称:')

#VIN = 'X70TESTVIN0000038'  # VIN
#taskName = 'YODOTEST_20200801_#38_18'  # 任务名称



deviceTypeId=''
taskId=''
proxy_addr = {
    # 'https': 'https://127.0.0.1:8888',  # 本地fiddler代理端口
    # 'http': 'http://127.0.0.1:8888'
}
#


#登录开瑞新能源管理平台
print('------登录开瑞新能源管理平台--------')
url = "http://116.236.19.122:12702/api/signin"
data = {
    "password": "yundong123",
    "userName": "yundong"
}

r_login = requests.post(url=url, data=data)  # post请求

print("状态码：", r_login.status_code)  # 打印返回的状态码
print("打印正文", r_login.text)  # 打印返回的正文

_cookies = requests.utils.dict_from_cookiejar(r_login.cookies)

# print('------查询创建升级任务--------')
# url_upgradeList = 'http://116.236.19.122:12702/api/getQueryParameList'
# r_upgradeList = requests.get(url=url_upgradeList)

#创建升级任务-查询vin
print('------创建升级任务-查询vin--------')
url_queryOtaList = 'http://116.236.19.122:12702/api/queryOtaList'

params_queryOtaList = {
    'pageIndex': 1,
    'pageSize': 10,
    'vin': VIN,
    'unitId': 15,
    'unitName': 'TBOX',
    'flag': False
}

r_otaList = requests.get(url=url_queryOtaList, params=params_queryOtaList, cookies=_cookies)

print("状态码：", r_otaList.status_code)  # 打印返回的状态码
print("打印正文：", r_otaList.text)  # 打印返回的正文

jsonData = json.loads(r_otaList.text)
deviceTypeId = jsonData.get('datas')[0].get('deviceTypeId') #获取得到deviceTypeId
print("deviceTypeId：", deviceTypeId)


#升级任务设置
print('------升级任务设置--------')
url_upgrate_button = 'http://116.236.19.122:12702/api/getHardwareByDevice'
params_upgate_button = {
    'deviceTypeId': deviceTypeId
}
r_setUpgrateTask = requests.get(url=url_upgrate_button, params=params_upgate_button, cookies=_cookies)
print(r_otaList.status_code)  # 打印返回的状态码
print(r_setUpgrateTask.text)  # 打印返回的正文



#升级任务设置-保存提交
print('------升级任务设置-保存提交--------')
url_upgrateTaskSubmit = 'http://116.236.19.122:12702/api/otaUpgrade'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8'
}
data = {
    "VehUpgrade": "1",  # 升级方式，1：立即升级；:0：预约升级
    "name": taskName,  # 升级任务名称
    "parameterId": 795,  # id
    "remark": "",  # 备注
    "runtime": None,
    "otaUpgradByVehicleParam": 1,
    "saveType": 2,
    "account": "yundong",
    "vins": VIN,
    "currentVersion": "00.00.02",
    "tboxSn": "X70TESTSN000038",
    "forceUpdate": 1,  # 是否强制升级；1：强制升级，0：不强制升级
    "modelName": "捷途X70",
    "unitName": "TBOX",
    "manufacturerName": "云动",
    "deviceName": "TBOX-7DL",
    "modelCode": "X70",
    "modelId": 97,
    "unitId": 15,
    "manufacturerId": 73,
    "deviceTypeId": deviceTypeId,  #
    "otaType": 1,  # 升级方式，1：立即升级；:0：预约升级
    "now": False,
    "firmWareVersion": "00.00.05",
    "hardWareVersion": "0.0.1",
    "appPush": 0
}

r = requests.post(url=url_upgrateTaskSubmit, data=json.dumps(data), headers=header, cookies=_cookies,
                  proxies=proxy_addr)
print(r.status_code)  # 打印返回的状态码
print(r.text)  # 打印返回的正文



#升级任务管理-任务名称搜索
print('------升级任务管理-任务名称搜索--------')
url = 'http://116.236.19.122:12702/api/taskHistory'
params = {
    'taskName': taskName,
    'pageIndex': 1,
    'pageSize': 10,
    'appPush': 0
}
r = requests.get(url=url, params=params, cookies=_cookies)

print("状态码：", r.status_code)  # 打印返回的状态码
print("打印正文", r.text)  # 打印返回的正文

jsonData = json.loads(r.text)
taskId = jsonData.get('datas')[0].get('id') #获取得到taskId
print("id：", taskId)



#升级任务管理-审核
print('------升级任务管理-审核--------')

url = 'http://116.236.19.122:12702/api/auditOtaTask'

params = {
    'taskId': taskId,
    'account': 'yundong',
    'status': True
}

r = requests.get(url=url, params=params, cookies=_cookies, proxies=proxy_addr)
print(r.status_code)  # 打印返回的状态码
print(r.text)  # 打印返回的正文


#升级任务管理-下发升级
print('------升级任务管理-下发升级--------')

url = 'http://116.236.19.122:12702/api/commitOtaTask'

params = {
    'taskId': taskId,
    'acount': 'yundong'
}

r = requests.get(url=url, params=params, cookies=_cookies, proxies=proxy_addr)
print(r.status_code)  # 打印返回的状态码
print(r.text)  # 打印返回的正文
