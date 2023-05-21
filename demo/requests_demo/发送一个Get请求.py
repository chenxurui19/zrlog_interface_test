# -*- coding: utf-8 -*-
# @Time    : 2023/5/18 23:36
# @Author  : CXRui
# @File    : 发送一个Get请求.py
# @Description :
import requests
url = "http://192.168.0.5/admin/login"
# 通过Requests库发送Get请求
r = requests.get(url=url)
# 以文本的方式返回响应内容
print(r.text)
# 返回HTTP协议返回
print(r.status_code)
