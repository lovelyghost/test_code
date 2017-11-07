import datetime
create_at_start = "2015-05"
create_at_end = "2017-08"
query_date = 2

end_year, end_month = create_at_end.split('-')[:2]
start_year, start_month = create_at_start.split('-')[:2]
print(end_year)
print(start_year)
final =[]
if int(end_year) > int(start_year):
    s = [start_year + "-" + str('{:0>2}'.format(i))  for i in range(int(start_month),13)]
    e = [end_year + "-" + str('{:0>2}'.format(i))  for i in range(1,int(end_month)+1)]
    middle=[str(x)+"-"+str('{:0>2}'.format(j)) for x in range(int(start_year)+1,int(end_year)) for j in range(1,13)]
    final = s + middle + e

if int(end_year) == int(start_year):
    final = [start_year + "-" + str('{:0>2}'.format(i))  for i in range(int(start_month),int(end_month)+1)]
print(final)
# print(sorted(final))

print((datetime.datetime(int(end_year),int(end_month)+1,1) - datetime.datetime(int(end_year),int(end_month),1)).days)





# count1 = (datetime.datetime.strptime(str(create_at_end), "%Y-%m") -
#          datetime.datetime.strptime(str(create_at_start), "%Y-%m")).days/30
#
#
# for i in xrange(count1 + 1):
#     create_start = datetime.datetime(int(end_year), int(
#         end_month)-i,2).strftime('%Y-%m')
#     print(create_start)

# create_end = create_at_end
# create_start = create_at_start
#
# # count = (datetime.datetime.strptime(str(create_end), "%Y-%m-%d") -
# #          datetime.datetime.strptime(str(create_start), "%Y-%m-%d")).days/30
# count1 = (datetime.datetime.strptime(str(create_end), "%Y-%m") -
#          datetime.datetime.strptime(str(create_start), "%Y-%m")).days/30
# # print(count)
# print(count1)
# for i in xrange(count + 1):
#     jj = (datetime.datetime.strptime(create_end, "%Y-%m-%d") - datetime.timedelta(i*30)).strftime("%Y-%m-%d")
#     print('jj:'+ jj)