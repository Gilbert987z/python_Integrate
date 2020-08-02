import xlrd


def getExcelData(path, sheet_name):
    bk = xlrd.open_workbook(path)   #打开Excel文档
    sh = bk.sheet_by_name(sheet_name)   #打开sheet
    row_num = sh.nrows  #行数
    data_list = []      #列表
    for i in range(1, row_num):     #循环行数
        row_data = sh.row_values(i)     #列
        data = {}
        for index, key in enumerate(sh.row_values(0)):
            data[key] = row_data[index]
            data_list.append(data)
    return data_list



path = r'E:\data.xls'
Sheetname = 'Sheet1'
#print('12')
getExcelData(path, Sheetname)
print(getExcelData(path, Sheetname))
#print('12')
