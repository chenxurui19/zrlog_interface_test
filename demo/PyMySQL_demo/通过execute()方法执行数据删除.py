# -*- coding: utf-8 -*-
# @Time    : 2023/5/19 14:01
# @Author  : CXRui
# @File    : 通过execute()方法执行数据删除.py
# @Description :
import pymysql

# 导入PyMySQL库
db = pymysql.connect(
    # 设置数据库主机的地址
    host="192.168.0.3",
    # 设置数据库的用户名
    user="root",
    # 设置数据库的密码
    password="123456",
    # 设置数据库的名称
    database="zrlog",
    # 设置数据库的字符集
    charset="utf8",
    # 设置数据库的端口号
    port=33506
)

# 创建SQL游标对象，游标对象主要用来执行SQL语句
cursor = db.cursor()
# 要执行的SQL，并通过delete语句删除log表中的数据
sql = 'delete from log where alias="你好，希望"'
# 使用execute()方法执行SQL语句
cursor.execute(sql)
# 默认情况下MySQL的事物机制是开启的，需要使用commit()方法提交删除操作
db.commit()
