# -*- coding: utf-8 -*-
# @Time    : 2023/5/19 09:42
# @Author  : CXRui
# @File    : 携带Headers发送请求.py
# @Description :
# 导入Request库
import requests
url_login = "http://192.168.0.3/api/admin/login"
# 请求的数据为JSON格式的字符串，并将请求的数据保存在data字典中
data = {
    "userName": "admin",
    "password": "c1d6d359fb2e2d0cba3ef62af63ffd8c",
    "https": False,
    "key": 1684427952551
}

# 请求的参数将携带Headers，并将字典的格式存放
headers = {"Content-Type": "application/json"}

# 通过Requests库发送POST请求，并携带Headers
r_res = requests.post(url=url_login, json=data, headers=headers)

# 以文本的方式返回响应内容
print(r_res.text)

# 以JSON格式返回响应的内容
print(r_res.json())