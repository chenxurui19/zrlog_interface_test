# -*- coding: utf-8 -*-
# @Time    : 2023/5/19 15:27
# @Author  : CXRui
# @File    : settings.py
# @Description : 负责存储配置信息
import os

# 获取文件的绝对路径
abs_path = os.path.abspath(__file__)
# 获取文件所在目录的上一级目录，也就是根目录
project_path = os.path.dirname(os.path.dirname(abs_path))
# 通过os.sep的方法来获取config目录的全路径
_config_path = project_path + os.sep + "config"
# 通过os.sep的方法来获取log目录的全路径
_log_path = project_path + os.sep + "log"
# 通过os.sep的方法来获取report报告目录的全路径
_report_path = project_path + os.sep + "report"
# 数据库信息配置
DB_CONFIG = {
    "host": "192.168.0.3",
    "user": "root",
    "password": "123456",
    "database": "test",
    "port": 33506,
    "charset": "utf8"
}


# 返回日志目录
def get_log_path():
    return _log_path


# 返回报告目录
def get_report_path():
    return _report_path


# 返回config目录
def get_config_path():
    return _config_path


# 占位用，勿删除
class DynamicParam:
    pass


if __name__ == '__main__':
    print(get_log_path())
