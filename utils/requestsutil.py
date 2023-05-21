# -*- coding: utf-8 -*-
# @Time    : 2023/5/19 22:19
# @Author  : CXRui
# @File    : requestsutil.py
# @Description : HTTP请求工具，提供发送HTTP请求等操作
import requests
from utils.logutil import logger


# 定义HTTP请求类
class RequestSend:
    # 封装requests请求函数
    def api_run(self, url, method, data=None, headers=None, cookies=None):
        # 定义变量，获取响应结果
        res = None
        # 打印日志
        logger.info("请求的url为{},类型为{}".format(url, type(url)))
        # 打印日志
        logger.info("请求的method为{},类型为{}".format(method, type(method)))
        # 打印日志
        logger.info("请求的data为{},类型为{}".format(data, type(data)))
        # 打印日志
        logger.info("请求的headers为{},类型为{}".format(headers, type(headers)))
        # 打印日志
        logger.info("请求的cookies为{},类型为{}".format(cookies, type(cookies)))
        # 判断请求方法
        if method == "get":
            # 如果是get方法，则执行下面命令，发送http请求，方法为get
            res = requests.get(url, data=data, headers=headers, cookies=cookies)
        # 如果是post方法，则执行下面命令
        elif method == "post":
            # 判断headers内容，如果是json格式
            if headers == {"Content-Type": "application/json"}:
                # 发送http请求，方法为post，参数使用json=data
                res = requests.post(url, json=data, headers=headers, cookies=cookies)
            # 判断headers内容，如果是application/x-www-form-urlencoded格式
            elif headers == {"Content-Type": "application/x-www-form-urlencoded"}:
                # 发送http请求，方法为post，参数使用data=data
                res = requests.post(url, data=data, headers=headers, cookies=cookies)
        # 获取请求响应的状态码
        code = res.status_code
        # 获取请求响应的cookies
        cookies = res.cookies.get_dict()
        # 定义字典
        dict1 = dict()
        # 异常处理
        try:
            # 获取响应结果json格式
            body = res.json()
        # 捕获异常
        except:
            # 获取响应结果text
            body = res.text
        # 自定义参数code写入字典
        dict1['code'] = code
        # 自定义参数body写入字典
        dict1['body'] = body
        # 自定义参数cookies写入字典
        dict1['cookies'] = cookies
        # 返回自定义字典
        return dict1

    # 对外调用方法，**kwargs 传入的参数是dict类型
    def send(self, url, method, **kwargs):
        # 调用自定义方法
        return self.api_run(url=url, method=method, **kwargs)


if __name__ == '__main__':
    url = "http://192.168.0.5/api/admin/login"
    data = {"userName": "admin", "password": "c1d6d359fb2e2d0cba3ef62af63ffd8c", "https": False, "key": 1684427952551}
    method = "post"
    headers = {"Content-Type": "application/json"}
    print(RequestSend().send(url=url, method=method, headers=headers, data=data))



