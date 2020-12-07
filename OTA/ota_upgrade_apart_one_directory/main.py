# coding = utf-8

import time
from .service.taskExcelInput import *
from .service.taskConsoleInput import *

# main执行总程序
if __name__ == '__main__':
    chery_url = 'http://nev.mychery.com'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    }

    try:
        flag = True
        while flag:

            print('#捷途车联网管理平台-TBOX_OTA升级-可指定版本升级-V4.0#\n')
            # 用户名，密码
            account = 'yundong'
            password = 'yundong123'



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

            if flag == '1':
                flag = True
            elif flag == 'exit' or 'EXIT':
                for times in range(1, 6):
                    print('。', end='', flush=True)
                    time.sleep(1)  # 睡眠1秒
                break

    except Exception as e:   #抓取所有的报错信息
        print(e)
        time.sleep(999999)