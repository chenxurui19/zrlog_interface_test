# -*- coding: utf-8 -*-
# @Time    : 2023/5/19 11:21
# @Author  : CXRui
# @File    : 日志实例应用.py
# @Description :
import logging
# 创建logger对象
logger = logging.getLogger("test_logger")
# 设置日志输出等级总开关
logger.setLevel(logging.DEBUG)
# 创建控制台实例
sh = logging.StreamHandler()
# 设置控制台输出的日志级别
sh.setLevel(logging.DEBUG)
# 设置控制台输出的日志格式
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
sh.setFormatter(formatter)
# 加载控制台实例到logger对象中
logger.addHandler(sh)

# 加入异常处理机制
try:
    # 本例设置了一个并不存在的文件路径，通过open()函数打开它
    open('/path/to/does/not/exist', 'rb')
    # 当文件存在时程序不会产生异常，以下日志信息将输出到控制台
    logger.info("文件正常打开啦")
except Exception as e:
    # 当文件不存在时将产生异常，以下错误日志信息将输出到控制台
    logger.error("很抱歉，文件打开失败了")
