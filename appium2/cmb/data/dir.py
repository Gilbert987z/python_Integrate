import sys
import os

#print(sys.path)
print('##########')

os.getcwd()  # 获得当前工作目录

print(os.path.abspath('.'))  # 获得当前工作目录

print(os.path.abspath('..'))  # 获得当前工作目录的父目录

print(os.path.abspath(os.curdir))  # 获得当前工作目录

print('##########')
#print(readExcel('data',1,1))
project_name = "InterfaceTest_project"
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find(project_name+"\\")+len(project_name+"\\")]  #关键点！！

print(project_name)
print(curPath)
print(rootPath)




print(curPath+'\\data.xlsx')