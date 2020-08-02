# 导入pymysql模块
import pymysql


# 连接database
db = pymysql.connect(host='121.196.36.116', user='root',password='123456',database='movie',charset='utf8')

#db = pymysql.connect(host='101.37.65.134', user='dbmanager',password='fafe1a2c82ecb5187eea^&$%QWEF',database='DOUGONG-JYJ-DEV',charset='utf8')
#db = pymysql.connect("101.37.65.134","dbmanager","fafe1a2c82ecb5187eea^&$%QWEF","DOUGONG-JYJ-DEV" )
