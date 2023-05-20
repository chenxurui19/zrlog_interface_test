# 插入第一条测试用例
INSERT INTO `test_case_list` VALUES (1, 'zrlog', '登录模块', '密码错误', '/api/admin/login', 'post', '{\"Content-Type\": \"application/json\"}', '{}', '{\"userName\":\"admin\",\"password\":123456,\"https\":False,\"key\":1598188173501}', 'json', NULL, '1', 1);
# 插入第二条测试用例
INSERT INTO `test_case_list` VALUES (2, 'zrlog', '登录模块', '不携带密码参数', '/api/admin/login', 'post', '{\"Content-Type\": \"application/json\"}', '{}', '{\"userName\":\"admin\",\"https\":False,\"key\":1598188173501}', 'json', NULL, '1', 1);
# 插入第三条测试用例
INSERT INTO `test_case_list` VALUES (3, 'zrlog', '登录模块', '用户名错误', '/api/admin/login', 'post', '{\"Content-Type\": \"application/json\"}', '{}', '{\"userName\":\"adminadminadminadmin\",\"password\":\"ca72de92e7e1767aefe5853a282836e7\",\"https\":False,\"key\":1598188173501}', 'json', NULL, '1', 1);
# 插入第四条测试用例
INSERT INTO `test_case_list` VALUES (4, 'zrlog', '登录模块', '用户名为非字符串类型', '/api/admin/login', 'post', '{\"Content-Type\": \"application/json\"}', '{}', '{\"userName\":123456,\"password\":\"ca72de92e7e1767aefe5853a282836e7\",\"https\":False,\"key\":1598188173501}', 'json', NULL, '1', 1);
# 插入第五条测试用例
INSERT INTO `test_case_list` VALUES (5, 'zrlog', '登录模块', '不携带用户名参数', '/api/admin/login', 'post', '{\"Content-Type\": \"application/json\"}', '{}', '{\"password\":\"ca72de92e7e1767aefe5853a282836e7\",\"https\":False,\"key\":1598188173501}', 'json', NULL, '1', 1);
# 插入第六条测试用例
INSERT INTO `test_case_list` VALUES (6, 'zrlog', '登录模块', '用户名为空字符串', '/api/admin/login', 'post', '{\"Content-Type\": \"application/json\"}', '{}', '{\"userName\":\"\",\"password\":\"ca72de92e7e1767aefe5853a282836e7\",\"https\":False,\"key\":1598188173501}', 'json', NULL, '1', 1);
# 插入第七条测试用例
INSERT INTO `test_case_list` VALUES (7, 'zrlog', '登录模块', '用户名和密码正确', '/api/admin/login', 'post', '{\"Content-Type\": \"application/json\"}', '{}', '{\"userName\":\"admin\",\"password\":\"ca72de92e7e1767aefe5853a282836e7\",\"https\":False,\"key\":1598188173501}', 'json', 'token=cookies.admin-token', '0', 1);
# 插入第八条测试用例
INSERT INTO `test_case_list` VALUES (8, 'zrlog', '文章管理模块', '发布文章', '/api/admin/article/create', 'post', '{\"Content-Type\": \"application/json\"}', '{\"admin-token\":\"${token}\"}', '{\"id\":None,\"editorType\":\"markdown\",\"title\":\"付出\",\"alias\":\"付出\",\"thumbnail\":None,\"typeId\":\"1\",\"keywords\":None,\"digest\":None,\"canComment\":False,\"recommended\":False,\"privacy\":False,\"content\":\"<p>付出</p>\\n\",\"markdown\":\"付出\",\"rubbish\":False}', 'json', 'id_name=body.id,alias_name=body.alias', '0', 1);
# 插入第九条测试用例
INSERT INTO `test_case_list` VALUES (9, 'zrlog', '文章管理模块', '修改文章', '/api/admin/article/update', 'post', '{\"Content-Type\": \"application/json\"}', '{\"admin-token\":\"${token}\"}', '{\"id\":\"${id_name}\",\"editorType\":\"markdown\",\"title\":\"付出才能杰出\",\"alias\":\"${alias_name}\",\"thumbnail\":None,\"typeId\":\"1\",\"keywords\":None,\"digest\":\"<p>付出</p>\",\"canComment\":False,\"recommended\":False,\"privacy\":False,\"content\":\"<p>付出</p>\\n\",\"markdown\":\"付出\",\"rubbish\":False}', 'json', NULL, '0', 1);
# 插入第十条测试用例
INSERT INTO `test_case_list` VALUES (10, 'zrlog', '文章管理模块', '删除文章', '/api/admin/article/delete', 'post', '{\"Content-Type\": \"application/x-www-form-urlencoded\"}', '{\"admin-token\":\"${token}\"}', '{\"oper\":\"del\",\"id\":\"${id_name}\"}', 'data', NULL, '0', 1);
# 插入第十一条测试用例
INSERT INTO `test_case_list` VALUES (11, 'zrlog', '文章管理模块', '查询文章', '/api/admin/article?keywords=付出才能杰出&_search=false&nd=1598429806679&rows=10&page=1&sidx=&sord=asc', 'get', '{\"Content-Type\": \"application/x-www-form-urlencoded\"}', '{\"admin-token\":\"${token}\"}', '{}', 'data', NULL, '0', 1);
