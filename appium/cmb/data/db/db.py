# 导入pymysql模块
import pymysql



# 连接database
db = pymysql.connect(host='121.196.36.116', user='root',password='123456',database='movie',charset='utf8')
#db = pymysql.connect(host='101.37.65.134', user='dbmanager',password='fafe1a2c82ecb5187eea^&$%QWEF',database='DOUGONG-JYJ-DEV',charset='utf8')
#db = pymysql.connect("101.37.65.134","dbmanager","fafe1a2c82ecb5187eea^&$%QWEF","DOUGONG-JYJ-DEV" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql =  'select * from favor'


# 使用 fetchone() 方法获取单条数据.
#data = cursor.fetchone()


# 执行SQL语句
cursor.execute(sql)
# 获取多条查询数据
ret = cursor.fetchall()
cursor.close()
db.close()
# 打印下查询结果
print(ret)