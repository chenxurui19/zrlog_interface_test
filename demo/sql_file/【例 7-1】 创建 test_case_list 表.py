CREATE TABLE `test_case_list` (
    # 测试用例的编号，不为空，自增长
    `id` int(0) NOT NULL AUTO_INCREMENT,
    # 项目名称
    `web` varchar(255) DEFAULT NULL,
    # 项目模块
    `module` varchar(255) DEFAULT NULL,
    # 测试用例的标题
    `title` varchar(255) DEFAULT NULL,
    # 接口地址的路径
    `url` varchar(255) DEFAULT NULL,
    # 请求方法
    `method` varchar(255) DEFAULT NULL,
    # 请求头
    `headers` varchar(255) DEFAULT NULL,
    # cookies 秘钥
    `cookies` varchar(1000) DEFAULT NULL,
    # 请求主体信息
    `request_body` varchar(1000) DEFAULT NULL,
    # 请求主体的数据类型
    `request_type` varchar(255) DEFAULT NULL,
    # 关联
    `relation` varchar(255) DEFAULT NULL,
    # 预期业务状态码
    `expected_code` varchar(255) DEFAULT NULL COMMENT ' 作为
    断言标准 ',
    # 测试用例是否可运行
    `isdel` int(0) NULL DEFAULT 1 COMMENT '0 为删除， 1 为正常',
    # 设置 id 为主键
    PRIMARY KEY (`id`) USING BTREE
# 设置表的引擎为 InnoDB
) ENGINE = InnoDB ;