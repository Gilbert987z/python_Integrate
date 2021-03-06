# coding = utf-8

import requests
import json
import xlrd
import time
import sys

'''
PC端-开瑞新能源管理平台-tbox升级
'''

proxy_addr = {
    # 'https': 'https://127.0.0.1:8888',  # 本地fiddler代理端口
    # 'http': 'http://127.0.0.1:8888'
}


#
# 数据模块
#

def get_excel_data(path, sheet_name):
    '''
    读取Excel
    '''
    bk = xlrd.open_workbook(path)  # 打开Excel文档
    sh = bk.sheet_by_name(sheet_name)  # 打开sheet
    row_num = sh.nrows  # 行数 11=10+1
    data_list = []  # 列表

    for i in range(1, row_num):  # 循环行数 从第2行开始，到11行结束
        row_data = sh.row_values(i)  # 行 ['X70TESTVIN0000038', 'YODOTEST_20200801_#38_30']
        # print(row_data)
        data = {}
        for index, key in enumerate(sh.row_values(0)):  # 枚举，创建出键值对 第一行 ['VIN', '任务名称']
            data[key] = row_data[index]

        data_list.append(data)
    return data_list


# 登录开瑞新能源管理平台
def login_chery(userName, password):
    '''
    接口：登录开瑞新能源管理平台
    '''
    print('------登录开瑞新能源管理平台--------')
    url = chery_url + "/api/signin"
    data = {
        "password": password,
        "userName": userName
    }

    r = requests.post(url=url, data=data, proxies=proxy_addr)  # post请求

    print("状态码：", r.status_code)  # 打印返回的状态码
    print("打印正文：", r.text)  # 打印返回的正文

    cookies = requests.utils.dict_from_cookiejar(r.cookies)
    return cookies


# 创建升级任务-查询vin
def upgrade_task_search_vin(cookies, VIN):
    '''
    接口：创建升级任务-查询vin
    '''
    print('------创建升级任务-查询vin--------')
    url = chery_url + '/api/queryOtaList'

    params = {
        'pageIndex': 1,
        'pageSize': 10,
        'vin': VIN,
        'unitId': 15,
        'unitName': 'TBOX',
        'flag': False
    }

    r = requests.get(url=url, params=params, cookies=cookies, proxies=proxy_addr)

    print("状态码：", r.status_code)  # 打印返回的状态码
    print("打印正文：", r.text)  # 打印返回的正文

    jsonData = json.loads(r.text)
    search_vin_datas = jsonData.get('datas')[0]  # 接口返回的datas信息
    return search_vin_datas


# 升级任务设置-保存提交
def upgrade_task_setting_commit(cookies, taskName, account, vins, currentVersion, tboxSn, modelName, unitName,
                                manufacturerName, deviceName, modelCode, modelId, unitId, manufacturerId, deviceTypeId,
                                lastVersion, hardWareVersion):
    """
    接口：升级任务设置-保存提交
    """
    print('------升级任务设置-保存提交--------')
    url = chery_url + '/api/otaUpgrade'

    header = {
        'Content-Type': 'application/json;charset=UTF-8'
    }
    data = {
        "VehUpgrade": "1",  # 升级方式，1：立即升级；:0：预约升级
        "name": taskName,  # 升级任务名称
        "parameterId": 795,  # 暂时没有发现这个parameterId有什么关联？？？  #TODO
        "remark": "",  # 备注
        "runtime": None,
        "otaUpgradByVehicleParam": 1,
        "saveType": 2,
        "account": account,
        "vins": vins,
        "currentVersion": currentVersion,
        "tboxSn": tboxSn,
        "forceUpdate": 1,  # 是否强制升级；1：强制升级，0：不强制升级
        "modelName": modelName,
        "unitName": unitName,
        "manufacturerName": manufacturerName,
        "deviceName": deviceName,
        "modelCode": modelCode,
        "modelId": modelId,
        "unitId": unitId,
        "manufacturerId": manufacturerId,
        "deviceTypeId": deviceTypeId,  #
        "otaType": 1,  # 升级方式，1：立即升级；:0：预约升级
        "now": False,
        "firmWareVersion": lastVersion,  # 目标版本
        "hardWareVersion": hardWareVersion,
        "appPush": 0
    }

    r = requests.post(url=url, data=json.dumps(data), headers=header, cookies=cookies,
                      proxies=proxy_addr)
    print(r.status_code)  # 打印返回的状态码
    print(r.text)  # 打印返回的正文


# 升级任务管理-任务名称搜索
def upgrade_task_search_name(cookies, taskName):
    """
    接口：升级任务管理-任务名称搜索
    """
    print('------升级任务管理-任务名称搜索--------')
    url = chery_url + '/api/taskHistory'
    params = {
        'taskName': taskName,
        'pageIndex': 1,
        'pageSize': 10,
        'appPush': 0
    }
    r = requests.get(url=url, params=params, cookies=cookies)

    print("状态码：", r.status_code)  # 打印返回的状态码
    print("打印正文", r.text)  # 打印返回的正文

    jsonData = json.loads(r.text)

    return jsonData.get('datas')


# 升级任务管理-审核
def upgrade_task_audit(cookies, taskId, account):
    """
    接口：升级任务管理-审核
    """
    print('------升级任务管理-审核--------')

    url = chery_url + '/api/auditOtaTask'

    params = {
        'taskId': taskId,
        'account': account,
        'status': True
    }

    r = requests.get(url=url, params=params, cookies=cookies, proxies=proxy_addr)
    print(r.status_code)  # 打印返回的状态码
    print(r.text)  # 打印返回的正文


# 升级任务管理-下发升级
def upgrade_task_commit(cookies, taskId, account):
    """
    接口：升级任务管理-下发升级
    """
    print('------升级任务管理-下发升级--------')

    url = chery_url + '/api/commitOtaTask'

    params = {
        'taskId': taskId,
        'acount': account
    }

    r = requests.get(url=url, params=params, cookies=cookies, proxies=proxy_addr)
    print(r.status_code)  # 打印返回的状态码
    print(r.text)  # 打印返回的正文


# 升级任务管理-升级结果
def upgrade_task_result(cookies, taskId):
    """
    接口：升级任务管理-升级结果
    """
    print('\n------升级任务管理-查看升级结果--------')

    url = chery_url + '/api/otaTaskResult'
    params = {
        'taskId': taskId,
        'pageIndex': 1,
        'pageSize': 10
    }
    r = requests.get(url=url, params=params, cookies=cookies, proxies=proxy_addr)
    print(r.status_code)  # 打印返回的状态码
    print(r.text)  # 打印返回的正文

    jsonData = json.loads(r.text)

    return jsonData.get('datas')


# 接口：升级任务管理-登录后的总流程
def tbox_process(VIN, taskName, account, inLastVersion):
    """
    接口：升级任务管理-登录后的总流程
    """
    # VIN码的校验
    try:
        search_vin_datas = upgrade_task_search_vin(cookies, VIN)  # 搜索VIN码，返回接口数据
    except BaseException:
        print('ERROR:没有找到对应的VIN码，请重新设置！')

    # 关联
    vins = search_vin_datas.get('vin')
    currentVersion = search_vin_datas.get('currentVersion')
    tboxSn = search_vin_datas.get('tboxSn')
    modelName = search_vin_datas.get('modelName')
    unitName = search_vin_datas.get('unitName')
    manufacturerName = search_vin_datas.get('manufactureName')
    deviceTypeName = search_vin_datas.get('deviceTypeName')
    modelCode = search_vin_datas.get('modelCode')
    modelId = search_vin_datas.get('modelId')
    unitId = search_vin_datas.get('unitId')
    manufactureId = search_vin_datas.get('manufactureId')
    deviceTypeId = search_vin_datas.get('deviceTypeId')
    lastVersion = search_vin_datas.get('lastVersion')  # 最新版本
    hardWareVersion = search_vin_datas.get('hardWareVersion')

    if (inLastVersion != None):  # 如果Excel有值，就替换
        lastVersion = inLastVersion

    # 升级任务管理-下发升级
    upgrade_task_setting_commit(cookies, taskName=taskName, account=account, vins=vins,
                                currentVersion=currentVersion, tboxSn=tboxSn,
                                modelName=modelName, unitName=unitName,
                                manufacturerName=manufacturerName, deviceName=deviceTypeName,
                                modelCode=modelCode, modelId=modelId, unitId=unitId, manufacturerId=manufactureId,
                                deviceTypeId=deviceTypeId,
                                lastVersion=lastVersion, hardWareVersion=hardWareVersion)

    # 升级任务管理-任务名称搜索
    search_taskName_datas = upgrade_task_search_name(cookies, taskName)
    taskId = search_taskName_datas[0].get('id')  # 获取taskId

    # 升级任务管理-审核
    upgrade_task_audit(cookies, taskId, account)

    # 升级任务管理-下发升级
    upgrade_task_commit(cookies, taskId, account)

    return taskId


# excel导入
def task_excel_input(account):
    while True:
        try:
            path = input('请输入Excel的路径(I:\data.xlsx)：')
            sheet = input('请输入Excel的工作表名（Sheet1）：')

            # path = 'I:/data.xls'
            # sheet = 'Sheet1'

            task_list = get_excel_data(path, sheet)  # excel读取的列表
            task_sum = len(task_list)  # excel的列表的数量

            print('\nTBOX升级任务：', task_list)
            print('共有 %d 个TBOX升级任务' % task_sum)
            # time.sleep(3)   #暂停三秒
            break
        except BaseException:
            print('\nERROR:输入错误，请重新输入！')

    # 输入循环等待时长的校验的校验
    while True:
        try:
            cycle_time = int(input('\n每次循环大概多少秒：'))
            if cycle_time >= 1:
                break
            else:
                print('ERROR:输入错误，要求输入数字为正整数，请重新输入！')
        except BaseException:
            print('\nERROR:输入错误，要求输入为正整数，请重新输入！')

    task_success = 0  # 统计成功的数量
    #
    # 开始Excel内的循环
    #
    for task_num in range(0, task_sum):
        task_count = task_num + 1  # 轮次的计数

        taskName = task_list[task_num].get('任务名称')  # 从Excel中读取的任务名称
        VIN = task_list[task_num]['VIN']  # 从Excel中读取的VIN

        lastVersion = ''
        if '目标版本' in task_list[task_num]:  # 如果有目标版本
            lastVersion = task_list[task_num]['目标版本']

        print('\n\n<<开始第 %d 轮的TBOX升级-%s>>' % (task_count, taskName))

        taskId = tbox_process(VIN, taskName, account, lastVersion)  # 登录后的总流程

        if task_num < len(task_list) - 1:
            print('\n开始读秒（10秒输出一次，共%d秒）' % cycle_time)
            for cycle_time in range(0, cycle_time + 1, 10):
                print('%ds ' % cycle_time, end='', flush=True)
                time.sleep(5)  # 睡眠1秒

        # 睡眠结束后，校验是否升级成功
        task_result_datas = upgrade_task_result(cookies, taskId)
        # task_status = task_result_datas.get('otaList')[0].get('upgradeStatus')[0].get('upgradesResult')
        task_status = task_result_datas.get('otaList')[0].get('status')
        print('\n第%d次升级结果：' % task_count, task_status)

        if task_status == 'UPGRADES_SUCCESS':
            task_success = task_success + 1

    task_success_rate = task_success / task_sum * 100
    print('\n*****TOBOX升级结果*****')
    print('升级任务总数-%d;升级成功数-%d；升级成功率-%f;' % (task_sum, task_success, task_success_rate))


# 手动输入导入任务信息
def task_console_input(account):
    VIN = input('请输入VIN(X70TESTVIN0000038):')
    taskName = input('请输入任务名称(YODOTEST_20200808_#38_01):')
    watting_time = int(input('请输入等待时间：'))

    taskId = tbox_process(VIN, taskName, account, inLastVersion='')  # 登录后的总流程

    print('\n开始读秒（10秒输出一次，共%d秒）' % watting_time)

    for cycle_time in range(0, watting_time + 1, 10):
        print('%ds ' % cycle_time, end='', flush=True)
        time.sleep(5)  # 睡眠1秒

    # 睡眠结束后，校验是否升级成功
    task_result_datas = upgrade_task_result(cookies, taskId)
    task_status = task_result_datas.get('otaList')[0].get('status')
    print('\n升级结果：', task_status)


# main执行总程序
if __name__ == '__main__':
    chery_url = "http://116.236.19.122:12702"

    flag = True
    while flag:

        print('#开瑞新能源管理平台-TBOX升级功能-V1.0#\n')
        # 用户名，密码
        account = 'yundong'
        password = 'yundong123'

        cookies = login_chery(userName=account, password=password)  # 登录并保存cookies

        print('\n（1-导入Excel文档，2-手动输入）')
        while True:
            task_choice = input("请输入你的选择:")  # str型的

            if task_choice == '1':
                task_excel_input(account)  # excel导入
                break
            elif task_choice == '2':
                task_console_input(account)  # 手动导入
                break

        print('\n<<<<运行结束>>>>')

        print('\n（exit-结束运行,并关闭当前窗口，1-重新运行程序）')
        while True:
            try:
                flag = input("请输入你的选择:")  # str型的

                if flag == 'exit':
                    print('\n<<<<正在关闭当前窗口>>>>')
                    break
                elif flag == '1':
                    print('\n<<<<重新执行程序>>>>')
                    break

            except BaseException:
                print('ERROR:输入错误，请重新输入！')

        if flag == 1:
            flag = True
        elif flag == 'exit':
            for times in range(1, 6):
                print('。', end='', flush=True)
                time.sleep(1)  # 睡眠1秒
            break
