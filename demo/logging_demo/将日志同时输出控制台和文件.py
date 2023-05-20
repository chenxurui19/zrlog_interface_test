# -*- coding: utf-8 -*-
# @Time    : 2023/5/19 10:54
# @Author  : CXRui
# @File    : 将日志同时输出控制台和文件.py
# @Description :
# 导入logging库
import logging
# 创建logger对象
logger = logging.getLogger("test_logger")
# 设置日志输出等级总开关
logger.setLevel(logging.DEBUG)
# 创建控制台实例
sh = logging.StreamHandler()

fh = logging.FileHandler("api.log", mode="a", encoding="utf-8")
# 设置控制台输出的日志级别
sh.setLevel(logging.DEBUG)
# 设置向文件输出的日志级别
fh.setLevel(logging.DEBUG)
# 统一设置日志的输出格式
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# 设置向控制台实例到logger对象中
logger.addHandler(sh)
# 加载文件实例到logger对象中
logger.addHandler(fh)

if __name__ == '__main__':
    logging.debug("-----调试信息[debug]-----")
    logging.info("-----调试信息[debug]-----")
    logging.warning("-----调试信息[debug]-----")
    logging.error("-----调试信息[debug]-----")
    logging.critical("-----调试信息[debug]-----")