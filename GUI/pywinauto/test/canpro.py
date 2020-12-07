from pywinauto import application
from pywinauto.keyboard import send_keys

app = application.Application(backend='uia').start('notepad.exe')
#选中该窗口
wind_calc = app['无标题 - 记事本']
#获取所有控件，打印结果
wind_calc.print_control_identifiers()
#选择编辑器窗口
edit = app['无标题 - 记事本']['Edit']
#内容输入
edit.type_keys('记事本测试\n开心每一天')
send_keys('{VK_RETURN}')
edit.type_keys('测试\ntest')

# 关闭弹窗
ftptool = app.window_(found_index=0).close()
app = application.Application(backend='uia').connect(handle=0x01B529BC)
ftptool = app.window_(found_index=0).close()

nokeep = app['记事本']['不保存(&N)']

send_keys('{VK_RETURN}')