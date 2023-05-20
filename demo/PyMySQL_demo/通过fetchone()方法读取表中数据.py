# -*- coding: utf-8 -*-
# @Time    : 2023/5/19 12:01
# @Author  : CXRui
# @File    : 通过fetchone()方法读取表中数据.py
# @Description :
# 导入PyMySQL库
import pymysql
# 创建数据库对象

db = pymysql.connect(
    # 设置数据库主机的地址
    host="192.168.0.3",
    # 设置数据库的用户名
    user="root",
    # 设置数据库的密码
    password="123456",
    # 设置数据库的名称
    database="zrlog",
    # 设置数据库的端口号
    port=33506
)

# 创建SQL游标对象，游标对象主要用来执行SQL语句
cursor = db.cursor()
# 要执行的SQL语句
sql = "select * from log"
# 使用execute()方法执行SQL语句
cursor.execute(sql)
# 使用fetchone()方法一次性获取一条数据
res = cursor.fetchone()
# 打印获取的数据
print(res)
# 关闭游标对象
cursor.close()
# 关闭database对象
db.close()
