# coding = utf-8

import time
from ..page.cheryJetourPage import CheryJetourPage as JETOUR


# 接口：升级任务管理-查看结果流程
def taskResult(cookies, taskId):
    """
    接口：升级任务管理-查看结果流程
    """

    # 睡眠结束后，校验是否升级成功
    task_result_datas = JETOUR.upgrade_task_result(cookies, taskId)

    return task_result_datas
