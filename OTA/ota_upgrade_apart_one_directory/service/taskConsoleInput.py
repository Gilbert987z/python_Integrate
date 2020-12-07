# coding = utf-8

import time
from ..process.taskCreate import *
from ..process.taskResult import *


# 手动输入导入任务信息
def task_console_input(account):
    # todo
    cookies = JETOUR.login_chery(userName=account, password='yundong123')  # 登录并保存cookies

    VIN = input('请输入VIN:')
    taskName = input('请输入任务名称:')
    watting_time = int(input('请输入等待时间：'))

    taskId = taskCreate(cookies, VIN, taskName, account)  # 登录后的总流程

    print('\n开始读秒（10秒输出一次，共%d秒）' % watting_time)

    for cycle_time in range(0, watting_time + 1, 10):
        print('%ds ' % cycle_time, end='', flush=True)
        time.sleep(10)  # 睡眠10秒

    # 睡眠结束后，校验是否升级成功
    task_result_datas = taskResult(cookies, taskId)

    task_status = task_result_datas.get('otaList')[0].get('status')
    print('\n升级结果：', task_status)
