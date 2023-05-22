-- 设置客户端字符集为UTF8mb4
SET NAMES 'utf8mb4';

-- 创建zrlog数据库
create DATABASE zrlog CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- 创建test数据库
create DATABASE test  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 切换test数据库
use test;

-- 创建 test_case_list 表
CREATE TABLE `test_case_list` (
    -- 测试用例的编号
    `id` int(0) NOT NULL AUTO_INCREMENT,
    -- 项目名称
    `web` varchar(255) DEFAULT NULL,
    -- 项目模块
    `module` varchar(255) DEFAULT NULL,
    -- 测试用例的标题
    `title` varchar(255) DEFAULT NULL,
    -- 接口地址的路径
    `url` varchar(255) DEFAULT NULL,
    -- 请求方法
    `method` varchar(255) DEFAULT NULL,
    -- 请求头
    `headers` varchar(255) DEFAULT NULL,
    -- cookies 秘钥
    `cookies` varchar(1000) DEFAULT NULL,
    -- 请求主体信息
    `request_body` varchar(1000) DEFAULT NULL,
    -- 请求主体的数据类型
    `request_type` varchar(255) DEFAULT NULL,
    -- 关联
    `relation` varchar(255) DEFAULT NULL,
    -- 预期业务状态码
    `expected_code` varchar(255) DEFAULT NULL COMMENT ' 作为
    断言标准 ',
    -- 测试用例是否可运行
    `isdel` int(0) NULL DEFAULT 1 COMMENT '0 为删除， 1 为正常',
    -- 设置 id 为主键
    PRIMARY KEY (`id`) USING BTREE
-- 设置表的引擎为 InnoDB
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4;

-- 向 test_case_list 表中插入测试用例的内容
-- 插入第一条测试用例
INSERT INTO `test_case_list` VALUES (1, 'zrlog', '登录模块', '密码错误', '/api/admin/login', 'post', '{\"Content-Type\": \"application/json\"}', '{}', '{\"userName\":\"admin\",\"password\":123456,\"https\":False,\"key\":1598188173501}', 'json', NULL, '1', 1);
-- 插入第二条测试用例
INSERT INTO `test_case_list` VALUES (2, 'zrlog', '登录模块', '不携带密码参数', '/api/admin/login', 'post', '{\"Content-Type\": \"application/json\"}', '{}', '{\"userName\":\"admin\",\"https\":False,\"key\":1598188173501}', 'json', NULL, '1', 1);
-- 插入第三条测试用例
INSERT INTO `test_case_list` VALUES (3, 'zrlog', '登录模块', '用户名错误', '/api/admin/login', 'post', '{\"Content-Type\": \"application/json\"}', '{}', '{\"userName\":\"adminadminadminadmin\",\"password\":\"ca72de92e7e1767aefe5853a282836e7\",\"https\":False,\"key\":1598188173501}', 'json', NULL, '1', 1);
-- 插入第四条测试用例
INSERT INTO `test_case_list` VALUES (4, 'zrlog', '登录模块', '用户名为非字符串类型', '/api/admin/login', 'post', '{\"Content-Type\": \"application/json\"}', '{}', '{\"userName\":123456,\"password\":\"ca72de92e7e1767aefe5853a282836e7\",\"https\":False,\"key\":1598188173501}', 'json', NULL, '1', 1);
-- 插入第五条测试用例
INSERT INTO `test_case_list` VALUES (5, 'zrlog', '登录模块', '不携带用户名参数', '/api/admin/login', 'post', '{\"Content-Type\": \"application/json\"}', '{}', '{\"password\":\"ca72de92e7e1767aefe5853a282836e7\",\"https\":False,\"key\":1598188173501}', 'json', NULL, '1', 1);
-- 插入第六条测试用例
INSERT INTO `test_case_list` VALUES (6, 'zrlog', '登录模块', '用户名为空字符串', '/api/admin/login', 'post', '{\"Content-Type\": \"application/json\"}', '{}', '{\"userName\":\"\",\"password\":\"ca72de92e7e1767aefe5853a282836e7\",\"https\":False,\"key\":1598188173501}', 'json', NULL, '1', 1);
-- 插入第七条测试用例
INSERT INTO `test_case_list` VALUES (7, 'zrlog', '登录模块', '用户名和密码正确', '/api/admin/login', 'post', '{\"Content-Type\": \"application/json\"}', '{}', '{\"userName\":\"admin\",\"password\":\"ca72de92e7e1767aefe5853a282836e7\",\"https\":False,\"key\":1598188173501}', 'json', 'token=cookies.admin-token', '0', 1);
-- 插入第八条测试用例
INSERT INTO `test_case_list` VALUES (8, 'zrlog', '文章管理模块', '发布文章', '/api/admin/article/create', 'post', '{\"Content-Type\": \"application/json\"}', '{\"admin-token\":\"${token}\"}', '{\"id\":None,\"editorType\":\"markdown\",\"title\":\"付出\",\"alias\":\"付出\",\"thumbnail\":None,\"typeId\":\"1\",\"keywords\":None,\"digest\":None,\"canComment\":False,\"recommended\":False,\"privacy\":False,\"content\":\"<p>付出</p>\\n\",\"markdown\":\"付出\",\"rubbish\":False}', 'json', 'id_name=body.id,alias_name=body.alias', '0', 1);
-- 插入第九条测试用例
INSERT INTO `test_case_list` VALUES (9, 'zrlog', '文章管理模块', '修改文章', '/api/admin/article/update', 'post', '{\"Content-Type\": \"application/json\"}', '{\"admin-token\":\"${token}\"}', '{\"id\":\"${id_name}\",\"editorType\":\"markdown\",\"title\":\"付出才能杰出\",\"alias\":\"${alias_name}\",\"thumbnail\":None,\"typeId\":\"1\",\"keywords\":None,\"digest\":\"<p>付出</p>\",\"canComment\":False,\"recommended\":False,\"privacy\":False,\"content\":\"<p>付出</p>\\n\",\"markdown\":\"付出\",\"rubbish\":False}', 'json', NULL, '0', 1);
-- 插入第十条测试用例
INSERT INTO `test_case_list` VALUES (10, 'zrlog', '文章管理模块', '删除文章', '/api/admin/article/delete', 'post', '{\"Content-Type\": \"application/x-www-form-urlencoded\"}', '{\"admin-token\":\"${token}\"}', '{\"oper\":\"del\",\"id\":\"${id_name}\"}', 'data', NULL, '0', 1);
-- 插入第十一条测试用例
INSERT INTO `test_case_list` VALUES (11, 'zrlog', '文章管理模块', '查询文章', '/api/admin/article?keywords=付出才能杰出&_search=false&nd=1598429806679&rows=10&page=1&sidx=&sord=asc', 'get', '{\"Content-Type\": \"application/x-www-form-urlencoded\"}', '{\"admin-token\":\"${token}\"}', '{}', 'data', NULL, '0', 1);


-- 创建 test_config 表
CREATE TABLE `test_config` (
    -- 配置信息序号
    `id` int(0) NOT NULL,
    -- 项目名称
    `web` varchar(255) DEFAULT NULL,
    -- 环境信息字段
    `key` varchar(255) DEFAULT NULL,
    -- 环境信息的值
    `value` varchar(255) DEFAULT NULL,
    -- 设置 id 为主键
    PRIMARY KEY (`id`) USING BTREE
    -- 设置表的引擎为 InnoDB
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4;


-- 向 test_config 表中插入测试用例
-- 插入的配置信息为测试环境的 IP 地址
INSERT INTO `test_config` VALUES (1, 'zrlog', 'url_api','http://192.168.47.128');

-- 创建 test_result_record 表
CREATE TABLE `test_result_record` (
    -- 执行结果记录的序号
    `id` int(0) UNSIGNED NOT NULL AUTO_INCREMENT,
    -- 被执行测试用例的 id
    `case_id` varchar(255) DEFAULT NULL,
    -- 执行结果更新的时间
    `times` varchar(255) DEFAULT NULL,
    -- 程序运行的实际结果
    `response` varchar(1000) DEFAULT NULL COMMENT '实际结果',
    -- 用例执行是否通过
    `result` varchar(255) DEFAULT NULL,
    -- 设置 id 为主键
    PRIMARY KEY (`id`) USING BTREE
    -- 设置表的引擎为 InnoDB
) ENGINE = InnoDB  DEFAULT CHARSET=utf8mb4;