# -*- coding: utf-8 -*-
# @Time    : 2023/5/19 23:02
# @Author  : CXRui
# @File    : base.py
# @Description :
# 导入json库
import json
# 导入Template类
from string import Template
# 导入re库
import re


def find(data):
    """
    根据参数匹配内容
    查询是否是否有关联参数进行关联操作。如果有则进行关联，如果无则不进行关联
    :param data:
    :return:
    """
    # 判断data类型是否为字典
    if isinstance(data, dict):
        data = json.dumps(data)
        # 定义正则匹配规则
        pattern = "\\${(.*?)}"
        # 按匹配进行查询，把查询的结果返回
        return re.findall(pattern, data)


def relace(ori_data, replace_data):
    """
    根据定义的变量及获取规则，把具体的响应结果赋值给该变量
    :param ori_data:
    :param replace_data:
    :return:
    """
    # 对象格式化为str
    ori_data = json.dumps(ori_data)
    # 处理字符串的类，实例化并初始化原始字符
    s = Template(ori_data)
    # 使用新的字符，替换
    return s.safe_substitute(replace_data)


def parse_relation(var, resdata):
    """
    根据var，逐层获取json格式的值
    如果条件是token=cookies.admin-token，则响应结果的值为{"admin-token": "admin-token=1#4C7A71556C4555562B31706A385A776138546836616571503178336D6A6E6F30317A367972594A474F66316A5548413362334130384A73384968574B55717A7372466754626352553371557A3374594B527563757463693242364633626C706A626C47704242792B726D453D
"}
    :param var:
    :param resdata:
    :return:
    """
    if not var:
        # 如果变量var不存在，则直接返回resdata内容
        return resdata
    else:
        # 如果变量存在，则获取数组第1个内容
        resdata = resdata.get(var[0])
        # 从数组中删除第1个内容
        del var[0]
        # 递归
        return parse_relation(var, resdata)


# 测试代码
if __name__ == '__main__':
    ori_data = {"admin-token": "${token}"}
    replace_data = {"token": "x015k878"}
    print(relace(ori_data, replace_data))
