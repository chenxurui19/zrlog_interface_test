# -*- coding: utf-8 -*-
# @Time    : 2023/5/18 23:41
# @Author  : CXRui
# @File    : 发送一个POST请求.py
# @Description :
# 导入Requests库
import requests
# 此处使用的接口地址为Zrlog系统后台登录的接口地址
url_login = "http://192.168.0.5/api/admin/login"
# 请求的数据为JSON格式的字符串，并将请求的数据保存在data字典中
data = {
    "userName": "admin",
    "password": "c1d6d359fb2e2d0cba3ef62af63ffd8c",
    "https": False,
    "key": 1684427952551
}

# 通过Requests库发送POST请求，其中verify=False代表绕过HTTPS证书验证
r_res = requests.post(url=url_login, json=data, verify=False)
# 以文本的方式返回响应内容
print(r_res.text)
# 以JSON格式返回响应内容
print(r_res.json())
