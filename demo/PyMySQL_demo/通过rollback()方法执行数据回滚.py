# -*- coding: utf-8 -*-
# @Time    : 2023/5/19 12:25
# @Author  : CXRui
# @File    : 通过rollback()方法执行数据回滚.py
# @Description :

# 导入PyMySQL库
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

sql_001 = "insert into log set logId=6, title='你好，帅哥', alias='你好，帅哥', content='你好，帅哥！'"
sql_002 = "insert into log set logId=2, title='你好，美女', alias='你好，美女', content='你好，美女！'"

try:
    # 使用execute()方法执行sql_001语句
    cursor.execute(sql_001)
    # 使用execute()方法执行sql_002语句，此语句执行将回你产生异常
    cursor.execute(sql_002)
    # 默认情况下MySQL的事物机制是开启的，需要使用commit()方法进行数据提交
    db.commit()
except:
    # 关闭游标对象
    db.rollback()
    # 关闭database对象
    db.commit()

