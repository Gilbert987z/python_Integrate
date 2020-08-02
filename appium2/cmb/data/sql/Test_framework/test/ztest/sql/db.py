
import os
import yaml
import pymysql      # 导入pymysql模块
import pymysql.cursors


def connectDatabase():
    current_path = os.path.abspath("../../../config")
    yaml_path = os.path.join(current_path, "database.yaml")
    # print(current_path)
    # print(yaml_path)
    dbdata = get_yaml_data(yaml_path)

    # 连接database
    db = pymysql.connect(host=dbdata['host'], user=dbdata['user'],password=dbdata['password'],database=dbdata['database'],charset=dbdata['charset'])
    return db;
    # # 使用 cursor() 方法创建一个游标对象 cursor
    # cursor = db.cursor()
    #
    # sql =  'select user_id from vote_user'
    #
    #
    # # 使用 fetchone() 方法获取单条数据.
    # #data = cursor.fetchone()
    #
    #
    # # 执行SQL语句
    # cursor.execute(sql)
    # # 获取多条查询数据
    # ret = cursor.fetchall()
    # cursor.close()
    # db.close()
    # # 打印下查询结果
    # print(ret)
    #
    # print(ret[0][0])


#获取yaml文件里的database数据
def get_yaml_data(yaml_file):
    # 打开yaml文件
    print("***获取yaml文件数据***")
    file = open(yaml_file, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()

    print(file_data)
    print("类型：", type(file_data))

    # 将字符串转化为字典或列表
    print("***转化yaml数据为字典或列表***")
    data = yaml.load(file_data, Loader = yaml.FullLoader)
    print(data)
    print("类型：", type(data))
    return data




connectDatabase()