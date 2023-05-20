# -*- coding: utf-8 -*-
# @Time    : 2023/5/19 10:13
# @Author  : CXRui
# @File    : 调用request()方法发送请求.py
# @Description :

# 导入Request库
import requests
# 此处使用的接口地址为zrlog系统后台登录的接口地址
url_login = "http://192.168.0.3/api/admin/login"

# 请求的数据为JSON格式的字符串
data = {
    "userName": "admin",
    "password": "c1d6d359fb2e2d0cba3ef62af63ffd8c",
    "https": False,
    "key": 1684427952551
}

# 定义method参数的值为post
method = "post"
# 调用request()方法来发送POST请求，而request()方法中加入了method参数
r_res = requests.request(url=url_login,
                         method=method,
                         json=data,
                         verify=False)
# 以文本的方式返回响应内容
print(r_res.text)
# 以JSON格式返回响应内容
print(r_res.json())
