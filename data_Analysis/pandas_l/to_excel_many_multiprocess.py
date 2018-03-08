# -*- coding: utf-8 -*-

from pandas import DataFrame,ExcelWriter,read_table,concat,read_csv
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import threading
import os
import time
executor = ThreadPoolExecutor(4)



def generate_csv(i):

    if i.endswith("csv"):
        data_all = read_csv('/Users/lx/Desktop/bills_bills/'+ i, encoding='GB18030')
        data_all.iat[-1,5] = '\t' + data_all[u'商户号'][0]
        data_all.iat[-1,6] = data_all[u'交易时间'][0][:10]

        data_detail = data_all[0:-2]
        data_detail[[u'交易时间',u'APPID',u'商户号',u'子商户号',u'Uline订单号',u'第三方订单号',u'商户订单号']] = data_detail[
            [u'交易时间',u'APPID',u'商户号',u'子商户号',u'Uline订单号',u'第三方订单号',u'商户订单号']].apply(lambda x: '\t' + x)

        data_statistics = data_all.tail(1)

        # data_statistics.rename(columns=change_columns,inplace=True)
        # data_statistics = data_statistics.reindex(columns=statistics_data_columns)
        data_detail.to_csv('/Users/lx/test_code/data_Analysis/pandas_l/交易详情.csv',mode='a', index=False,encoding='GB18030',header=False)
        data_statistics.to_csv('/Users/lx/test_code/data_Analysis/pandas_l/交易汇总.csv',mode='a', index=False,encoding='GB18030',header=False)


if __name__ == '__main__':

    detail_data_columns = [u'交易时间', u'APPID', u'商户号',u'子商户号',u'设备编号',u'Uline订单号',
                 u'第三方订单号',u'商户订单号',u'用户标识',u'交易类型',u'业务类型',u'付款银行',
                 u'货币种类',u'总金额',u'企业红包金额',u'Uline退款单号',u'商户退款单号',u'退款金额',u'企业红包退款金额',
                 u'退款状态',u'商品名称',u'商户数据包',u'手续费',u'费率',
                        u'扩展字段一',u'扩展字段二',u'扩展字段三',u'扩展字段四',u'扩展字段五',u'扩展字段六'
                 ]
    statistics_data_columns = [u'总交易单数', u'总交易额', u'总退款额',u'交易总净额',u'手续费总额',u'商户 ID',u'交易日期']

    detail_dataframe = DataFrame([],columns=detail_data_columns)
    detail_dataframe.to_csv('/Users/lx/test_code/data_Analysis/pandas_l/交易详情.csv', index=False, encoding='GB18030')

    statistics_dataframe = DataFrame([],columns=statistics_data_columns)
    statistics_dataframe.to_csv('/Users/lx/test_code/data_Analysis/pandas_l/交易汇总.csv', index=False, encoding='GB18030')

    file_url = os.listdir('/Users/lx/Desktop/bills_bills/')
    change_columns = {u'交易时间':u'总交易单数', u'APPID':u'总交易额',
                          u'商户号':u'总退款额',u'子商户号':u'交易总净额',
                          u'设备编号':u'手续费总额',u'Uline订单号':u'商户 ID',
                           u'第三方订单号':u'交易日期'}

    dd = time.time()
    for i in file_url:

        executor.submit(generate_csv, i)
    print(time.time()-dd)



