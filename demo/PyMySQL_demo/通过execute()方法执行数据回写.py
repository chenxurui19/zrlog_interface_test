# -*- coding: utf-8 -*-
# @Time    : 2023/5/19 12:12
# @Author  : CXRui
# @File    : 通过execute()方法执行数据回写.py
# @Description :
import pymysql

# 创建数据库对象
db = pymysql.connect(
    # 设置数据库主机的地址
    host="192.168.0.5",
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
sql = "insert into log set logId=5, title='您好，希望', alias='你好，希望', content='你好，希望'"
# 使用execute()方法执行SQL语句
cursor.execute(sql)

# 默认情况下MySQL的事物机制是开启的，需要使用commit()方法进行数据提交
db.commit()
# 关闭游标对象
cursor.close()
# 关闭database对象
db.close()