# # -*- coding:utf-8 -*-

STATUS_CODE={
    (1,2):{"code":10001,"msg":"系统错误"},
    10008:{"code":10008,"msg":"参数错误，请参考API文档"},
    10009:{"code":10009,"msg":"无效的数据格式"},
}
STATUS_CODE[(1,2)].update({"data":"ss"})
print(STATUS_CODE[(1,2)])