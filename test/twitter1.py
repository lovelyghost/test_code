# -*- coding:utf-8 -*-
import re
#多线程学习
import urllib
import logging
import string
import datetime
import requests
import os
import random
import threading
import time
from multiprocessing import Pool, Process
#多进程学习
# class MyThread(threading.Thread):
#
#     def __init__(self, number, logger):
#         threading.Thread.__init__(self)
#         self.number = number
#         self.logger = logger
#
#     def run(self):
#         """
#         运行线程
#         """
#         logger.debug('Calling doubler')
#         get_beauty(self.number, self.logger)
#
#
#
#
# def get_logger():
#     logger = logging.getLogger("threading_example")
#     logger.setLevel(logging.DEBUG)
#
#     fh = logging.FileHandler("threading.log")
#     fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
#     formatter = logging.Formatter(fmt)
#     fh.setFormatter(formatter)
#
#     logger.addHandler(fh)
#     return logger
#
# def get_beauty(num, logger):
#     for j in range(num,2005):
#         dir = r'/Users/lx/Desktop/image/{}/'.format(j)
#         logger.debug('the {}th file'.format(j))
#         if not os.path.exists(dir):
#             os.makedirs(dir)
#         for i in range(10):
#             url='http://img1.mm131.com/pic/{}/{}.jpg'.format(j,i)
#             local_filename = str(j) + url.split('/')[-1]
#             print "Download Image File=", local_filename
#             r = requests.get(url, stream=True) # here we need to set stream = True parameter
#             if r and not os.path.exists(dir + local_filename):
#                 with open(dir + local_filename, 'wb') as f:
#                     for chunk in r.iter_content(chunk_size=1024):
#                         if chunk: # filter out keep-alive new chunks
#                             f.write(chunk)
#                             f.flush()
#                     f.close()
#             else:
#                 break
#
#
# if __name__=="__main__":
#     logger = get_logger()
#     thread_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
#     lasttime = time.time()
#     for i in range(6):
#         my_thread = MyThread(2000, logger)
#         my_thread.setName(thread_names[i])
#         my_thread.start()
#         my_thread.join()
#     print(time.time()-lasttime)


# from multiprocessing import Pool


def get_logger():
    logger = logging.getLogger("threading_example")
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler("threading.log")
    fmt = '%(asctime)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    return logger


def id_generator(size=32, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def get_beauty(num, logger, pro,starttime):
    for j in range(num,num+200):
        if round(j-num)%10==0:
            print(("{}~"+str(num+200)).format(num) + "区间已完成  " + str((j-num)/2) + "%")
        dir = r'/Users/lx/Desktop/image/{}/'.format(j)
        logger.debug('{} id downloading the {}th file'.format(pro, j))


        for i in range(70):
            url='http://img1.mm131.com/pic/{}/{}.jpg'.format(j,i)
            local_filename = str(j) + url.split('/')[-1]
            r = requests.get(url, stream=True) # here we need to set stream = True parameter
            if r and not os.path.exists(dir + local_filename):
                if not os.path.exists(dir):
                    os.makedirs(dir)
                # urllib.urlretrieve(url,dir+local_filename)
                with open(dir + local_filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk: # filter out keep-alive new chunks
                            f.write(chunk)
                            f.flush()
                    f.close()
            else:
                break

if __name__ == '__main__':

    starttime = time.time()
    logger = get_logger()
    name = ['a', 'b', 'c', 'd', 'e']
    start = [3100, 3200, 3300, 3400, 3500]
    data = zip(name, start)
    for j, i in data:
        p = Process(target=get_beauty,args=(i,logger,j,starttime))
        p.start()