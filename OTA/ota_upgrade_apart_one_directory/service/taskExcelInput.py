# coding = utf-8

import time
from ..page.cheryJetourPage import CheryJetourPage as JETOUR
from ..util import excel as EXCEL
from ..util import timestamp
from ..process.taskCreate import *
from ..process.taskResult import *

# excel导入
def task_excel_input(account):
    #输入相关excel信息，获取任务
    while True:
        try:
            file_path = input('请输入Excel的路径：')
            print('NOTICE（需提前关闭该Excel文件！！！）')
            sheet = input('请输入Excel的工作表名：')

            # path = 'I:/data.xls'
            # sheet = 'Sheet1'

            excel_data = EXCEL.get_excel_data(file_path, sheet)  # excel读取的列表
            task_list = excel_data[0]  # excel读取的列表

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





    #todo
    cookies = JETOUR.login_chery(userName=account, password='yundong123')  # 登录并保存cookies


    task_result_success = 0  # 统计成功的数量

    #
    # 开始Excel内的循环
    #

    for task_num in range(0, task_sum):
        task_count = task_num + 1  # 轮次的计数

        taskName = task_list[task_num].get('任务名称')  # 从Excel中读取的任务名称
        VIN = task_list[task_num]['VIN']  # 从Excel中读取的VIN


        print('\n\n<<开始第 %d 轮的TBOX升级-%s>>' % (task_count, taskName))

        if '目标版本' in task_list[task_num]:  # 如果有目标版本
            versionNum = task_list[task_num]['目标版本']  #从Excel中读取的版本号

            try:
                taskId = taskCreate(cookies, VIN, taskName, account, versionNum)  # 登录后的创建任务流程
            except Exception:
                print('\n-------token过期，重新登录-------\n')
                cookies = JETOUR.login_chery(userName=account, password='yundong123')  # 登录并保存cookies
                taskId = taskCreate(cookies, VIN, taskName, account, versionNum)  # 登录后的创建任务流程
        else:
            try:
                taskId = taskCreate(cookies, VIN, taskName, account, versionNum='')  # 登录后的创建任务流程
            except Exception:
                print('\n-------token过期，重新登录-------\n')
                cookies = JETOUR.login_chery(userName=account, password='yundong123')  # 登录并保存cookies
                taskId = taskCreate(cookies, VIN, taskName, account, versionNum='')  # 登录后的创建任务流程





        # if task_num < len(task_list) - 1:
        print('\n开始读秒（10秒输出一次，共%d秒）' % cycle_time)
        for cycle_time in range(0, cycle_time + 1, 10):
            print('%ds ' % cycle_time, end='', flush=True)
            time.sleep(10)  # 睡眠10秒

        try:
            task_result_datas = taskResult(cookies,taskId)  #查看任务结果的流程
        except Exception:
            print('\n-------token过期，重新登录-------\n')
            cookies = JETOUR.login_chery(userName=account, password='yundong123')  # 登录并保存cookies
            task_result_datas = taskResult(cookies, taskId)  # 查看任务结果的流程




        task_result_status = task_result_datas.get('otaList')[0].get('status')  # 升级结果，成功失败准备

        task_create_timestamp = task_result_datas.get('otaList')[0].get('createtime')  # 创建任务的时间戳
        task_create_time = timestamp.timestamp13_to_time(task_create_timestamp)  # 时间戳转换为任务创建时间

        #TODO 可能找不到上传信息，会报错，需要改进
        if task_result_status == 'UPGRADES_FAILURE' or task_result_status == 'UPGRADES_SUCCESS':      #如果   升级状态 != 准备     =失败和成功
            task_update_timestamp = task_result_datas.get('otaList')[0].get('updatestatus')[0].get('updatetime')  # 上传的时间戳
            task_update_time = timestamp.timestamp13_to_time(task_update_timestamp)  # 时间戳转换为上传时间

        #TODO 可能找不到失败信息，会报错，需要改进
        if task_result_status == 'UPGRADES_FAILURE':   #如果   升级状态 = 失败
            task_failure_message = task_result_datas.get('otaList')[0].get('failureMessage')  # failureMessage=Tbox上报：启动信息失败



        try:
            print('\n将运行结果，创建时间，上传时间，失败信息写入EXCEL中')

            EXCEL.write_excel_xls(file_path, excel_data[1], task_count,
                            task_result_status)  # 写入升级结果的数据  excel_data[1]是返回的第二个数据
            # EXCEL.write_excel_xls(file_path, excel_data[2], task_count,
            #                 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 写入升级时间

            EXCEL.write_excel_xls(file_path, excel_data[2], task_count,
                              task_create_time)  # 写入创建时间
            EXCEL.write_excel_xls(file_path, excel_data[3], task_count,
                              task_update_time)  # 写入上传时间
            EXCEL.write_excel_xls(file_path, excel_data[4], task_count,
                              task_failure_message)  # 写入失败信息
        except BaseException:
            print('\nERROR:由于Excel文件处于打开状态或者未找到相关信息，无法写入Excel文件！')


        print('\n第%d次升级结果：' % task_count, task_result_status)

        if task_result_status == 'UPGRADES_SUCCESS':
            task_result_success = task_result_success + 1

        task_success_rate = task_result_success / (task_num + 1) * 100

        print('\n目前的升级任务总数-%d;升级成功数-%d；升级成功率-%f;' % (task_num + 1, task_result_success, task_success_rate))




    print('\n*****TOBOX升级结果*****')
    print('可在Excel表中查看升级的结果')
    print('升级任务总数-%d;升级成功数-%d；升级成功率-%f;' % (task_sum, task_result_success, task_success_rate))


    # print('\n（是否要下载查看日志？ 1-下载日志，2-不了）')
    # while True:
    #     task_choice = input("请输入你的选择:")  # str型的
    #
    #     if task_choice == '1':
    #         task_excel_input(account)  # 下载日志
    #         break
    #     elif task_choice == '2':
    #         break
