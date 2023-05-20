CREATE TABLE `test_result_record` (
    # 执行结果记录的序号，不为空，自增长
    `id` int(0) UNSIGNED NOT NULL AUTO_INCREMENT,
    # 被执行测试用例的 id
    `case_id` varchar(255) DEFAULT NULL,
    # 执行结果更新的时间
    `times` varchar(255) DEFAULT NULL,
    # 程序运行的实际结果
    `response` varchar(1000) DEFAULT NULL COMMENT '实际结果',
    # 用例执行是否通过
    `result` varchar(255) DEFAULT NULL,
    # 设置 id 为主键
    PRIMARY KEY (`id`) USING BTREE
    # 设置表的引擎为 InnoDB
) ENGINE = InnoDB;