# coding=utf-8
import xlrd  #导入xlrd模块，需要先安装xlrd

#
# 数据模块
#

def readExcel(sheet, row, col):  #封装一个普通方法，用于读取excel表数据，readExcel是自定义的方法名
    #sheet/row/col作为形参，分别代表：工作表、行、列
    #通过xlrd中定义好的open_workbook()方法来打开Excel文件并赋给变量l_file
    #'C:\Users\Administrator\Desktop\data.xls'是excel文件以及其所在路径
    l_file = xlrd.open_workbook('C:\Users\Administrator.USER-20190920MY\Desktop\login.xlsx')
    #通过打开的excel文件l_file获取工作表，并赋给变量l_table
    # sheet_by_name()是通过工作表的名字获取，
    # sheet_by_index()是通过工作表的序列号获取
    l_table = l_file.sheet_by_name(sheet)
    #通过获取到的工作表l_table获取单元格中的数据，并赋给变量l_value
    # cell_value()是xlrd中定义的用于返回单元格数据的方法,通过行和列获取
    l_value = l_table.cell_value(row, col)
    #以下是对获取到的l_value进行数据类型的转换，并返回其值
    if type(l_value) == float:  #如果l_value的类型是float时，返回int型
        return int(l_value)  #return是返回值函数，用于返回变量的值
    else:
        return l_value