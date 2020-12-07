import time
from pywinauto import application

app = application.Application().start('notepad.exe')
app.Notepad.MenuSelect('帮助->关于记事本')
time.sleep(1)
OK = '确定'
app['关于“记事本”']['确定'].Click()  # 或者app['关于“记事本”'][OK].Click()
time.sleep(1)
app.notepad.TypeKeys("输入测试文本")
time.sleep(2)
dig = app.Notepad.MenuSelect("编辑(E)->替换(R)")
time.sleep(1)
Replace = '替换'
Cancel = '取消'
app[Replace][Cancel].Click()  # 要不然就写成app['替换']['取消'].Click()
time.sleep(1)
dialogs = app.windows_()
