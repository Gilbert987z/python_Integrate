import requests
import json
import xlrd

'''
PC端-开瑞新能源管理平台-tbox升级
'''

# 全局变量
VIN = input('请输入VIN:')
taskName = input('请输入任务名称:')

#VIN = 'X70TESTVIN0000038'  # VIN
#taskName = 'YODOTEST_20200801_#38_18'  # 任务名称



proxy_addr = {
    # 'https': 'https://127.0.0.1:8888',  # 本地fiddler代理端口
    # 'http': 'http://127.0.0.1:8888'
}
#






#
# 数据模块
#

def readExcel(sheet, row, col):  #封装一个普通方法，用于读取excel表数据，readExcel是自定义的方法名
    #sheet/row/col作为形参，分别代表：工作表、行、列
    #通过xlrd中定义好的open_workbook()方法来打开Excel文件并赋给变量l_file
    #'C:\Users\Administrator\Desktop\data.xls'是excel文件以及其所在路径
    l_file = xlrd.open_workbook('C:\Users\Administrator.USER-20190920MY\Desktop\login.xlsx')
    #通过打开的excel文件l_file获取工作表，并赋给变量l_table
    # sheet_by_name()是通过工作表的名字获取，
    # sheet_by_index()是通过工作表的序列号获取
    l_table = l_file.sheet_by_name(sheet)
    #通过获取到的工作表l_table获取单元格中的数据，并赋给变量l_value
    # cell_value()是xlrd中定义的用于返回单元格数据的方法,通过行和列获取
    l_value = l_table.cell_value(row, col)
    #以下是对获取到的l_value进行数据类型的转换，并返回其值
    if type(l_value) == float:  #如果l_value的类型是float时，返回int型
        return int(l_value)  #return是返回值函数，用于返回变量的值
    else:
        return l_value
print(readExcel())





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
lastVersion = jsonData.get('datas')[0].get('lastVersion')   #获取得到最新版本
tboxSn = jsonData.get('datas')[0].get('tboxSn') #获取得到tboxSn
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
    "tboxSn": tboxSn,
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
    "firmWareVersion": lastVersion,  #目标版本
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
