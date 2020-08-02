# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql =  'select moviename from movies'


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

print(ret[0][0])