# -*- coding: utf-8 -*-
# @Time    : 2023/5/19 09:51
# @Author  : CXRui
# @File    : 携带cookies发送请求.py
# @Description :
# 导入Request库
import requests
# 此处使用的接口地址为Zrlog系统文章发布的接口地址
url = "http://192.168.0.3/api/admin/article/create"
# 请求的数据类型为JSON格式的字符串，并存放在字典当中
data = {
    "id": None,
    "editorType": "markdown",
    "title": "您好",
    "alias": "您好",
    "thumbnail": None,
    "typeId": "1",
    "keywords": None,
    "digest": None,
    "canComment": False,
    "recommended": False,
    "privacy": False,
    "content": "<p>您好</p>",
    "markdown": "您好",
    "rubbish": False
}

"""
新增文章时需要携带服务端返回的cookies，以验证用户的身份
此cookies已过期，请读者重新抓去cookies
"""
cookies = {"admin-token": "1#4C7A71556C4555562B31706A385A7761385468366166344539465A652B6451567A444F5A4A426C38554C4D61482F36794F572B697168617A6F70753742726F726D6A63416B7154664D7332713756573879787A6E5559737271456D7177494666534E37377630416A784E633D"}

# 此POST方法里面携带了cookies这个字段
r = requests.post(url=url, json=data, cookies=cookies)
# 以文本的方式返回客户端响应的内容
print(r.text)
# 以JSON格式返回服务端响应的内容
print(r.json())
