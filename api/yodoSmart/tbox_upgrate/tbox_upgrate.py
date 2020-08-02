import requests
import json


proxy_addr = {
    'https': 'https://127.0.0.1:8888',  # 本地fiddler代理端口
    'http': 'http://127.0.0.1:8888'
}

'''
PC端-开瑞新能源管理平台-管理员登录
'''
print('------登录‘开瑞新能源管理平台’--------')
url1 = "http://116.236.19.122:12702/api/signin"
data = {
    "password": "yundong123",
    "userName": "yundong"
}

r_login = requests.post(url=url1, data=data)  # post请求

print()
session = requests.session()
print(session)
print(r_login.text)  # 打印返回的正文
print(r_login.status_code)  # 打印返回的状态码
print(r_login.cookies)  # 打印返回的cookie   jar格式
print(r_login.url)  # url值
print(r_login.encoding)  # 编码
_cookies = r_login.cookies
print(_cookies)

_cookies = requests.utils.dict_from_cookiejar(r_login.cookies)
print(_cookies)

# print('------查询创建升级任务--------')
# url_upgradeList = 'http://116.236.19.122:12702/api/getQueryParameList'
# r_upgradeList = requests.get(url=url_upgradeList)

print('------查询vin--------')
url_queryOtaList = 'http://116.236.19.122:12702/api/queryOtaList'


params_queryOtaList = {
    'pageIndex': 1,
    'pageSize': 10,
    'vin': 'X70TESTVIN0000038',
    'unitId': 15,
    'unitName': 'TBOX',
    'flag': False
}

r_otaList = requests.get(url=url_queryOtaList, params=params_queryOtaList, cookies=_cookies)
print(r_otaList.text)  # 打印返回的正文
print(r_otaList.status_code)  # 打印返回的状态码
print(r_otaList.cookies)  # 打印返回的cookie
print(r_otaList.url)  # url值
print(r_otaList.encoding)  # 编码

print('------升级任务设置--------')
url_upgrate_button = 'http://116.236.19.122:12702/api/getHardwareByDevice'
params_upgate_button = {
    'deviceTypeId': 160
}
r_setUpgrateTask = requests.get(url=url_upgrate_button, params=params_upgate_button, cookies=_cookies)
print(r_setUpgrateTask.text)  # 打印返回的正文


print('------升级任务设置-保存提交--------')
url_upgrateTaskSubmit = 'http://116.236.19.122:12702/api/otaUpgrade'

'''
正常
{"VehUpgrade":"1","name":"YODOTEST_20200801_#38_06","parameterId":795,"remark":"","runtime":null,"otaUpgradByVehicleParam":1,"saveType":2,"account":"yundong","vins":"X70TESTVIN0000038","currentVersion":"00.00.02","tboxSn":"X70TESTSN000038","forceUpdate":1,"modelName":"捷途X70","unitName":"TBOX","manufacturerName":"云动","deviceName":"TBOX-7DL","modelCode":"X70","modelId":97,"unitId":15,"manufacturerId":73,"deviceTypeId":160,"otaType":1,"now":false,"firmWareVersion":"00.00.05","hardWareVersion":"0.0.1","appPush":0}
不强制  预约
{"VehUpgrade":"2","name":"远程升级任务1596251587329","parameterId":795,"remark":"","runtime":"2020-08-27T16:00:00.000Z","otaUpgradByVehicleParam":1,"saveType":2,"account":"yundong","vins":"X70TESTVIN0000038","currentVersion":"00.00.02","tboxSn":"X70TESTSN000038","forceUpdate":0,"modelName":"捷途X70","unitName":"TBOX","manufacturerName":"云动","deviceName":"TBOX-7DL","modelCode":"X70","modelId":97,"unitId":15,"manufacturerId":73,"deviceTypeId":160,"otaType":2,"now":false,"firmWareVersion":"00.00.05","hardWareVersion":"0.0.1","appPush":0}
不强制  不预约
{"VehUpgrade":"1","name":"远程升级任务1596251692468","parameterId":795,"remark":"","runtime":null,"otaUpgradByVehicleParam":1,"saveType":2,"account":"yundong","vins":"X70TESTVIN0000038","currentVersion":"00.00.02","tboxSn":"X70TESTSN000038","forceUpdate":0,"modelName":"捷途X70","unitName":"TBOX","manufacturerName":"云动","deviceName":"TBOX-7DL","modelCode":"X70","modelId":97,"unitId":15,"manufacturerId":73,"deviceTypeId":160,"otaType":1,"now":true,"firmWareVersion":"00.00.05","hardWareVersion":"0.0.1","appPush":0}
正常
{"VehUpgrade":"1","name":"远程升级任务1596251777670","parameterId":795,"remark":"","runtime":null,"otaUpgradByVehicleParam":1,"saveType":2,"account":"yundong","vins":"X70TESTVIN0000038","currentVersion":"00.00.02","tboxSn":"X70TESTSN000038","forceUpdate":1,"modelName":"捷途X70","unitName":"TBOX","manufacturerName":"云动","deviceName":"TBOX-7DL","modelCode":"X70","modelId":97,"unitId":15,"manufacturerId":73,"deviceTypeId":160,"otaType":1,"now":false,"firmWareVersion":"00.00.05","hardWareVersion":"0.0.1","appPush":0}
预约
{"VehUpgrade":"2","name":"远程升级任务1596252009912","parameterId":795,"remark":"","runtime":"2020-08-28T16:00:00.000Z","otaUpgradByVehicleParam":1,"saveType":2,"account":"yundong","vins":"X70TESTVIN0000038","currentVersion":"00.00.02","tboxSn":"X70TESTSN000038","forceUpdate":0,"modelName":"捷途X70","unitName":"TBOX","manufacturerName":"云动","deviceName":"TBOX-7DL","modelCode":"X70","modelId":97,"unitId":15,"manufacturerId":73,"deviceTypeId":160,"otaType":2,"now":false,"firmWareVersion":"00.00.05","hardWareVersion":"0.0.1","appPush":0}
'''

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8'
}
data={
    "VehUpgrade":"1",                   #升级方式，1：立即升级；:0：预约升级
    "name":"YODOTEST_20200801_#38_14",  #升级任务名称
    "parameterId":795,                  #id
    "remark":"",                        #备注
    "runtime":None,
    "otaUpgradByVehicleParam":1,
    "saveType":2,
    "account":"yundong",
    "vins":"X70TESTVIN0000038",
    "currentVersion":"00.00.02",
    "tboxSn":"X70TESTSN000038",
    "forceUpdate":1,                    #是否强制升级；1：强制升级，0：不强制升级
    "modelName":"捷途X70",
    "unitName":"TBOX",
    "manufacturerName":"云动",
    "deviceName":"TBOX-7DL",
    "modelCode":"X70",
    "modelId":97,
    "unitId":15,
    "manufacturerId":73,
    "deviceTypeId":160,                 #
    "otaType":1,                         #升级方式，1：立即升级；:0：预约升级
    "now":False,
    "firmWareVersion":"00.00.05",
    "hardWareVersion":"0.0.1",
    "appPush":0
}

r = requests.post(url=url_upgrateTaskSubmit,data=json.dumps(data),headers=header,cookies=_cookies,proxies=proxy_addr)
print(r.status_code)  # 打印返回的状态码
print(r.text)  # 打印返回的正文



print('------升级任务管理-审核--------')

url = 'http://116.236.19.122:12702/api/auditOtaTask'

params = {
    'taskId': 7289,
    'account': 'yundong',
    'status': True
}

r = requests.get(url=url, params=params, cookies=_cookies, proxies=proxy_addr)
print(r.status_code)  # 打印返回的状态码
print(r.text)  # 打印返回的正文




print('------升级任务管理-下发升级--------')

url = 'http://116.236.19.122:12702/api/commitOtaTask'

params = {
    'taskId':7289,
    'acount':'yundong'
}

r = requests.get(url=url, params=params, cookies=_cookies, proxies=proxy_addr)
print(r.status_code)  # 打印返回的状态码
print(r.text)  # 打印返回的正文