# -*- coding: utf-8 -*-
# import shutil
# import os.path
# i = "/Users/lx/test/100001053122.csv"
# temp_path = "/Users/lx/test/temp"
# shutil.copy(i,temp_path)
# k = os.path.join(temp_path,os.path.split(i)[1])
# with open(k, 'r') as rf:
#     data = rf.read()
#     data = data.decode('utf-8').encode('GB2312')
# with open(k, 'w') as wf:
#     #     rf.truncate()
#     wf.write(data)

# m = 2
# f = 3
# g = True
# ss = [{"w":3,"e":m if g else f},{"w":4,"e":"tt"}]
# print(ss)

def kk(d,f,**g):
    print(d)
kk(1,2,ii=3)