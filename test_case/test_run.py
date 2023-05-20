# -*- coding: utf-8 -*-
# @Time    : 2023/5/20 18:40
# @Author  : CXRui
# @File    : test_run.py
# @Description : 定义获取测试用例类
import datetime
from config.settings import DynamicParam
from utils.logutil import logger
import common.base as Base
import json
import pytest
from utils.read_mysql import RdTestcase
from utils.requestsutil import RequestSend

# 初始化类
attribute = DynamicParam()
# 实例化测试用例对象
case_data = RdTestcase()
# 根据测试用例对象获取测试用例列表
case_list = case_data.is_run_data("zrlog")
# 获取当前时间
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# 测试用例执行类
class TestApi:
    # 类方法，运行开始前只执行1次
    def setup_class(self):
        # 打印日志
        logger.info(f"***** 开始执行测试用例，开始时间为：{current_time} *****")

    # 类方法，运行结束后只执行1次
    def teardown_class(self):
        # 打印日志
        logger.info(f"***** 执行用例完成，完成时间为：{current_time} *****")

    # 测试用例参数化
    @pytest.mark.parametrize('case', case_list)
    def test_run(self, case):
        # 定义变量
        res_data = None
        # 根据条件，从数据库获取url信息，并拼接完整url信息
        url = case_data.loadConfkey('zrlog', 'url_api')['value'] + case['url']
        # 获取method内容
        method = case['method']
        # 获取headers内容,格式化字符为字典
        headers = eval(case['headers'])
        # 获取cookies内容，格式化字符为字典
        cookies = eval(case['cookies'])
        # 获取请求内容，格式化字符为字典
        data = eval(case['request_body'])
        # 获取关联内容
        relation = str(case['relation'])
        # 获取测试用例名称
        case_name = case['title']

        # 根据关联，获取headers参数中是否有变量需要被替换，有则替换，无则默认
        headers = self.correlation(headers)
        # 根据关联，获取cookies参数中是否有变量需要被替换，有则替换，无则默认
        cookies = self.correlation(cookies)
        # 根据关联，获取data参数中是否有变量需要被替换，有则替换，无则默认
        data = self.correlation(data)

        # 异常处理
        try:
            # 打印日志
            logger.info("正在执行{}用例".format(case_name))
            # 执行测试用例，发送http请求
            res_data = RequestSend().send(url, method, data=data, headers=headers, cookies=cookies)
            # 打印日志
            logger.info("用例执行成功，请求的结果为{}".format(res_data))
        # 异常捕获
        except:
            # 打印日志
            logger.info("用例执行失败，请查看日志找原因。")
            # 断言结果为失败
            assert False
        # 判断res_data是否存在
        if res_data:
            # res_data存在后，判断relation不为None
            if relation != "None":
                # 根据响应结果，以及关联信息（token=cookies.admin-token），设置变量token的值为响应结果的信息
                self.set_relation(relation, res_data)
        # 结果进行验证
        self.assert_respoes(case, res_data)
        # 返回res_data信息
        return res_data

    # 响应结果关联设置函数
    def set_relation(self, relation, res_data):
        # 异常处理
        try:
            # 判断relation内容为True
            if relation:
                # 根据,进行分割，结果为List
                relation = relation.split(",")
                # 循环打印relation列表
                for i in relation:
                    # 根据=进行分割
                    var = i.split("=")
                    # 列表第1个值设置为var_name
                    var_name = var[0]
                    # 列表第2值内容按.进行分割，结果内容保存变量var_tmp
                    var_tmp = var[1].split(".")
                    # 在响应结果res_data中，根据条件var_tmp进行匹配
                    res = Base.parse_relation(var_tmp, res_data)
                    # 打印信息
                    print(f"{var_name}={res}")
                    # 把定义的变量名称以及值 以属性的方式设置到DynamicParam类中，实现动态存储
                    setattr(DynamicParam, var_name, res)

        # 捕获异常
        except Exception as e:
            # 打印异常信息
            print(e)

    # 根据关联，获取该变量内容
    def correlation(self, data):
        # 根据正则，获取数据
        res_data = Base.find(data)
        # 判断res_data为True
        if res_data:
            # 定义空的字典
            replace_dict = {}
            # 循环打印
            for i in res_data:
                # 根据名称，从DynamicParam动态获取属性值，并把结果内容赋值给变量data_tmp
                data_tmp = getattr(DynamicParam, str(i), "None")
                # 把结果更新到字典replace_dict中
                replace_dict.update({str(i): data_tmp})
            # 参数进行替换，并把str转换为python对象
            data = json.loads(Base.relace(data, replace_dict))
        # 返回结果
        return data

    # 结果验证方法
    def assert_respoes(self, case, res_data):
        # 变量初始化为False
        is_pass = False
        # 异常处理，捕获assert抛出的异常，不直接抛出
        try:
            # 根据结果进行断言验证
            assert int(res_data['body']['error']) == int(case['expected_code'])
            # 打印信息
            logger.info("用例断言成功")
            # 设置变量为True
            is_pass = True
        # 捕获异常
        except:
            # 设置变量为False
            is_pass = False
            # 打印日志
            logger.info("用例断言失败")
        # 无论是否出现异常，都执行下面内容代码
        finally:
            # 把结果更新到数据库
            case_data.updateResults(res_data, is_pass, str(case['id']))
            # 根据变量结果是True/False，进行断言验证，成功则通过，失败则未通过
            assert is_pass
        # 返回该变量结果
        return is_pass


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_run.py'])
