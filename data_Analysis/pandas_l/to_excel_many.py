# -*- coding: utf-8 -*-

from pandas import DataFrame,ExcelWriter,read_table,concat,read_csv
import time
import os

writer = ExcelWriter('/Users/lx/test_code/data_Analysis/pandas_l/out.xlsx')
print(dir(writer))
# detail_data_columns = [u'交易时间', u'APPID', u'商户号',u'子商户号',u'设备编号',u'Uline订单号',
#              u'第三方订单号',u'商户订单号',u'用户标识',u'交易类型',u'业务类型',u'付款银行',
#              u'货币种类',u'总金额',u'企业红包金额',u'Uline退款单号',u'商户退款单号',u'退款金额',u'企业红包退款金额',
#              u'退款状态',u'商品名称',u'商户数据包',u'手续费',u'费率',
#                     u'扩展字段一',u'扩展字段二',u'扩展字段三',u'扩展字段四',u'扩展字段五',u'扩展字段六'
#              ]
#
# detail_dataframe = DataFrame([],columns=detail_data_columns)
#
# detail_concat_list = [detail_dataframe,]
# statistics_concat_list = [detail_dataframe,]
#
# file_url = ['/Users/lx/test_code/data_Analysis/pandas_l/3月/1日/100053451814.csv',
#             '/Users/lx/test_code/data_Analysis/pandas_l/3月/1日/100053451799.csv',
#             '/Users/lx/test_code/data_Analysis/pandas_l/3月/1日/100053451950.csv',
#             '/Users/lx/test_code/data_Analysis/pandas_l/3月/1日/100053452055.csv'
#             ]
# file_url = os.listdir('/Users/lx/Desktop/bills_bills/')
# t1 = time.time()
#
# for i in file_url:
#     # data_all = read_csv(i, encoding='GB18030')
#     data_all = read_csv('/Users/lx/Desktop/bills_bills/' + i, encoding='UTF-8')
#     data_all.iat[-1,5] = data_all[u'商户号'][0]
#     data_all.iat[-1,6] = str(data_all[u'交易时间'][0])[:10]
#
#     data_detail = data_all[0:-2]
#     data_statistics = data_all.tail(1)
#
#     detail_concat_list.append(data_detail)
#     statistics_concat_list.append(data_statistics)
#
# detail_dataframe = concat(detail_concat_list,axis=0)
# statistics_dataframe = concat(statistics_concat_list,axis=0)
# change_columns = {u'交易时间':u'总交易单数', u'APPID':u'总交易额',
#                   u'商户号':u'总退款额',u'子商户号':u'交易总净额',
#                   u'设备编号':u'手续费总额',u'Uline订单号':u'商户 ID',
#                    u'第三方订单号':u'交易日期'}
# statistics_dataframe.rename(columns=change_columns,inplace=True)
# statistics_dataframe.drop(statistics_dataframe.columns[7:], axis=1,inplace=True)
# detail_dataframe.to_excel(writer, sheet_name = u'账单交易详情',index=False)
# statistics_dataframe.to_excel(writer, sheet_name = u'账单汇总数据',index=False,columns=[u'商户 ID',u'交易日期',u'总交易单数',u'总交易额',u'总退款额',u'交易总净额',u'手续费总额'])
# writer.save()
print(time.time()-t1)