import sys
import os

#print(sys.path)
print('##########')

os.getcwd()  # 获得当前工作目录

print(os.path.abspath('.'))  # 获得当前工作目录

print(os.path.abspath('..'))  # 获得当前工作目录的父目录

print(os.path.abspath(os.curdir))  # 获得当前工作目录

#获取当前脚本的路径（包含文件名称）-绝对路径
print(os.path.abspath(__file__))
print(os.path.realpath(__file__))

#获取当前脚本所在目录（不包含当前文件名）
print(os.path.split(os.path.abspath(__file__))[0])
print(os.path.dirname(os.path.abspath(__file__)))


print('##########')
#print(readExcel('data',1,1))
project_name = "InterfaceTest_project"
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find(project_name+"\\")+len(project_name+"\\")]  #关键点！！

print(project_name)
print(curPath)
print(rootPath)




print(curPath+'\\data.xlsx')