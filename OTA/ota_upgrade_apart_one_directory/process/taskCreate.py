# coding = utf-8

from ..page.cheryJetourPage import CheryJetourPage as JETOUR


# 接口：升级任务管理-登录后的创建任务流程
def taskCreate(cookies,VIN, taskName, account, versionNum):
    """
    接口：升级任务管理-登录后的总流程
    """



    # VIN码的校验
    try:
        search_vin_datas = JETOUR.upgrade_task_search_vin(cookies, VIN)  # 搜索VIN码，返回接口数据
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
    print('最新版本', lastVersion)
    hardWareVersion = search_vin_datas.get('hardWareVersion')


    # 版本管理-查询版本
    otaParameters = JETOUR.upgarede_task_get_version_parameterid(cookies, modelId=modelId, unitId=unitId,
                                                          manufactureId=manufactureId, deviceTypeId=deviceTypeId)
    parameterId = otaParameters[0].get('id')  # 获取parameterId


    print('versionum:',versionNum)
    if len(versionNum) != 0:   # 如果Excel有值，就替换
        lastVersion = versionNum

        print(otaParameters)
        for parametersNum in range(0, len(otaParameters)):
            if otaParameters[parametersNum].get('firmWareVersion') == versionNum:
                parameterId = otaParameters[parametersNum].get('id')  # 获取parameterId

    print('将要升级的版本', lastVersion)
    print('parameterId',parameterId)
    # 升级任务管理-任务提交
    JETOUR.upgrade_task_setting_commit(cookies, taskName=taskName, account=account, parameterId=parameterId, vins=vins,
                                currentVersion=currentVersion, tboxSn=tboxSn,
                                modelName=modelName, unitName=unitName,
                                manufacturerName=manufacturerName, deviceName=deviceTypeName,
                                modelCode=modelCode, modelId=modelId, unitId=unitId, manufacturerId=manufactureId,
                                deviceTypeId=deviceTypeId,
                                lastVersion=lastVersion, hardWareVersion=hardWareVersion)

    # 升级任务管理-任务名称搜索
    search_taskName_datas = JETOUR.upgrade_task_search_name(cookies, taskName)
    taskId = search_taskName_datas[0].get('id')  # 获取taskId

    # 升级任务管理-审核
    JETOUR.upgrade_task_audit(cookies, taskId, account)

    # # 升级任务管理-下发升级
    JETOUR.upgrade_task_commit(cookies, taskId, account)

    return taskId