CREATE TABLE `test_config` (
    # 配置信息序号
    `id` int(0) NOT NULL,
    # 项目名称
    `web` varchar(255) DEFAULT NULL,
    # 环境信息字段
    `key` varchar(255) DEFAULT NULL,
    # 环境信息的值
    `value` varchar(255) DEFAULT NULL,
    # 设置 id 为主键
    PRIMARY KEY (`id`) USING BTREE
    # 设置表的引擎为 InnoDB
) ENGINE = InnoDB ;