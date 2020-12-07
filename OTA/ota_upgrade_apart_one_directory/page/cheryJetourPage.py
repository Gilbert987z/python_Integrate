# coding = utf-8

import requests
import json

#
# 奇瑞捷途页面
#

chery_jetour_url = 'http://nev.mychery.com'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
}

proxy_addr = {
    # 'https': 'https://127.0.0.1:8888',  # 本地fiddler代理端口
    # 'http': 'http://127.0.0.1:8888'
}


class CheryJetourPage():

    # 登录开瑞新能源管理平台
    def login_chery(userName, password):
        '''
        接口：登录开瑞新能源管理平台
        '''
        print('------登录开瑞新能源管理平台--------')
        url = chery_jetour_url + "/api/signin"
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
    def upgrade_task_search_vin(cookies, VIN):
        '''
        接口：创建升级任务-查询vin
        '''
        print('------创建升级任务-查询vin--------')
        url = chery_jetour_url + '/api/queryOtaList'

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

    # 版本管理-查询版本
    def upgarede_task_get_version_parameterid(cookies, modelId, unitId, manufactureId, deviceTypeId):
        """
        接口：版本管理-查询版本
        """
        print('------版本管理-查询版本--------')
        url = chery_jetour_url + '/api/queryOtaVersion'

        params = {
            'modelId': modelId,
            'unitId': unitId,
            'manufactureId': manufactureId,
            'deviceTypeId': deviceTypeId,
            'hardwareVersion': '',
            'pageIndex': 1,
            'pageSize': 10
        }

        r = requests.get(url=url, params=params, cookies=cookies, headers=header, proxies=proxy_addr)

        print("状态码：", r.status_code)  # 打印返回的状态码
        print("打印正文：", r.text)  # 打印返回的正文

        jsonData = json.loads(r.text)
        otaParameters = jsonData.get('datas')[0].get('otaParameters')
        # parameterId = jsonData.get('datas')[0].get('otaParameters')[0].get('id')  # 接口返回的datas信息
        return otaParameters

    # 升级任务设置-保存提交
    def upgrade_task_setting_commit(cookies, taskName, parameterId, account, vins, currentVersion, tboxSn, modelName,
                                    unitName,
                                    manufacturerName, deviceName, modelCode, modelId, unitId, manufacturerId,
                                    deviceTypeId,
                                    lastVersion, hardWareVersion):
        """
        接口：升级任务设置-保存提交
        """
        print('------升级任务设置-保存提交--------')
        url = chery_jetour_url + '/api/otaUpgrade'

        header['Content-Type'] = 'application/json;charset=UTF-8'

        data = {
            "VehUpgrade": 1,  # 升级方式，1：立即升级；:0：预约升级
            "name": taskName,
            "parameterId": parameterId,  # 版本的Id
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
            "deviceTypeId": deviceTypeId,
            "otaType": 1,  # 升级方式，1：立即升级；:0：预约升级
            "now": False,
            "firmWareVersion": lastVersion,  # 目标版本
            "hardWareVersion": hardWareVersion
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
        url = chery_jetour_url + '/api/taskHistory'
        params = {
            'taskName': taskName,
            'pageIndex': 1,
            'pageSize': 10,
            'appPush': 0
        }
        r = requests.get(url=url, params=params, headers=header, cookies=cookies)

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

        url = chery_jetour_url + '/api/auditOtaTask'

        params = {
            'taskId': taskId,
            'account': account,
            'status': True
        }

        r = requests.get(url=url, params=params, cookies=cookies, headers=header, proxies=proxy_addr)
        print(r.status_code)  # 打印返回的状态码
        print(r.text)  # 打印返回的正文

    # 升级任务管理-下发升级
    def upgrade_task_commit(cookies, taskId, account):
        """
        接口：升级任务管理-下发升级
        """
        print('------升级任务管理-下发升级--------')

        url = chery_jetour_url + '/api/commitOtaTask'

        params = {
            'taskId': taskId,
            'acount': account
        }

        r = requests.get(url=url, params=params, cookies=cookies, headers=header, proxies=proxy_addr)
        print(r.status_code)  # 打印返回的状态码
        print(r.text)  # 打印返回的正文

    # 升级任务管理-升级结果
    def upgrade_task_result(cookies, taskId):
        """
        接口：升级任务管理-升级结果
        """
        print('\n------升级任务管理-查看升级结果--------')

        url = chery_jetour_url + '/api/otaTaskResult'
        params = {
            'taskId': taskId,
            'pageIndex': 1,
            'pageSize': 10
        }
        r = requests.get(url=url, params=params, cookies=cookies, headers=header, proxies=proxy_addr)
        print(r.status_code)  # 打印返回的状态码
        print(r.text)  # 打印返回的正文

        jsonData = json.loads(r.text)

        return jsonData.get('datas')


    #todo  由于log页面防抓包了，

    # 远程控制-查询VIN
    def remote_setting_search_vin(cookies, VIN):
        """
        接口：远程控制-查询VIN
        """
        print('\n------远程控制-查询VIN--------')

        url = chery_jetour_url + '/api/getJVehInfo'

        params = {
            'vin': VIN
        }

        r = requests.get(url=url, params=params, cookies=cookies, headers=header, proxies=proxy_addr)
        print(r.status_code)  # 打印返回的状态码
        print(r.text)  # 打印返回的正文

        jsonData = json.loads(r.text)
        search_vin_datas = jsonData.get('datas')[0]  # 接口返回的datas信息
        return search_vin_datas
