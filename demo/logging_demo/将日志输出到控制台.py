# -*- coding: utf-8 -*-
# @Time    : 2023/5/19 10:39
# @Author  : CXRui
# @File    : 将日志输出到控制台.py
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
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
sh.setFormatter(formatter)
# 加载控制台实例到logger对象中
logger.addHandler(sh)

if __name__ == '__main__':
    logging.debug("-----调试信息[debug]-----")
    logging.info("-----有用的信息[info]-----")
    logging.warning("-----有用的信息[info]-----")
    logging.error("-----有用的信息[info]-----")
    logging.critical("-----有用的信息[info]-----")


