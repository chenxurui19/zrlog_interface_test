# -*- coding: utf-8 -*-
# @Time    : 2023/5/19 10:29
# @Author  : CXRui
# @File    : basicConfig()方法的使用.py
# @Description :
import logging
"""
通过basicConfig()方法控制日志输出
level参数用来设置日志输出级别，此例日志为INFO
低于INFO级别的日志都不会打印，而format参数用设置日志输出格式
"""

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"
)

if __name__ == '__main__':
    logging.debug("-----调试信息[debug]-----")
    logging.info("-----有用信息[info]-----")
    logging.warning("-----调试信息[warning]-----")
    logging.error("-----错误信息[error]-----")
    logging.critical("-----严重错误信息[critical]-----")
