# # -*- coding:utf-8 -*-
# import time
# import calendar
# from sandglass.shortcut import tslice
# # print(calendar.monthrange(2017,9))
# dd = calendar.Calendar()
# # print(dd.monthdatescalendar(2017,9))
# # print(dd.yeardatescalendar(2017,9))
# # slice = tslice('day','2013-01-01','2013-01-04')
# slice = tslice('month','2013-01','2014-01')
#
# for i in slice:
#     print(i)
#
#
# def get_mon_seq(create_at_start, create_at_end):
#     start_time = time.time()
#     end_year, end_month = create_at_end.split('-')[:2]
#     start_year, start_month = create_at_start.split('-')[:2]
#     final = []
#     if int(end_year) > int(start_year):
#         s = [start_year + "-" + str('{:0>2}'.format(i))
#              for i in range(int(start_month), 13)]
#         # s = ["".join([start_year,str('-{:0>2}'.format(i))])
#         #      for i in range(int(start_month), 13)]
#         e = [end_year + "-" + str('{:0>2}'.format(i))
#              for i in range(1, int(end_month) + 1)]
#         # e = ["".join([end_year ,str('-{:0>2}'.format(i))])
#         #      for i in range(1, int(end_month) + 1)]
#         middle = [str(x) + "-" + str('{:0>2}'.format(j)) for x in range(int(start_year) + 1, int(end_year)) for j in
#                   range(1, 13)]
#         final = s + middle + e
#
#     if int(end_year) == int(start_year):
#         final = [start_year + "-" + str('{:0>2}'.format(i))
#                  for i in range(int(start_month), int(end_month) + 1)]
#     end_time = time.time()
#     print(end_time-start_time)
#
#     return final
#
# print(get_mon_seq("2012-03","2017-12"))
import datetime

def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime.datetime(int(year_s), int(mon_s), int(day_s))

def mch_append_start_end(details, query_date):
    detail = list()
    if int(query_date) == 2:
        for i in details:
            j = list(i)
            _year, _month = j[0].split('-')[:2]
            next_month = 1 if int(_month) == 12 else int(_month) + 1
            next_year = int(_year) + 1 if int(_month) == 12 else int(_year)
            days = (datetime.datetime(next_year, next_month, 1) - datetime.datetime(int(_year), int(_month), 1)).days
            end_date = datetime.datetime(int(_year), int(_month), days, 23, 59, 59).strftime('%Y-%m-%d %H:%M:%S')
            start_date = datetime.datetime(int(_year), int(_month), 1, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')
            j.pop()
            j.extend([start_date, end_date])
            detail.append(tuple(j))
    else:
        for i in details:
            j = list(i)
            kk = (parse_ymd(j[0])).strftime("%Y-%m-%d")
            _year, _month, _day = str(kk).split('-')
            end_date = datetime.datetime(int(_year), int(_month), int(_day), 23, 59, 59).strftime('%Y-%m-%d %H:%M:%S')
            start_date = datetime.datetime(int(_year), int(_month), int(_day), 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')
            j.pop()
            j.extend([start_date, end_date])
            detail.append(tuple(j))
    detail_keys = ('date', 'day_tx_count_total', 'day_tx_amount_total', 'day_refund_count_total',
                          'day_refund_amount_total', 'day_tx_net_amout_total', 'day_profit_amount_total','date_start','date_end')
    final_detail = [dict(zip(detail_keys,i) for i in detail)]
    return final_detail


detail_keys = (1,2,3,4)
print(dict(zip(detail_keys,(2,3,4,5))))