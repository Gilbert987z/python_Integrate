import xlwt

'''
利用xlwt能写成功
'''

# 创建一个工作表对象
workbook = xlwt.Workbook(encoding='utf-8')
# 设置excel表名
sheet = workbook.add_sheet('工作表')
# 往表格中填充数据
# 第一个参数表示行号，第二个参数表示列号
sheet.write(0,0,'姓名')
sheet.write(0,1,'年龄')
sheet.write(0,2,'身高')
sheet.write(0,3,'体重')

sheet.write(1,0,'李青')
sheet.write(1,1,20)
sheet.write(1,2,170)
sheet.write(1,3,'65KG')
workbook.save('I:\data.xls')