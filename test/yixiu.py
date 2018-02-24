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

def get_beauty(logger):
    dir = r'/Users/lx/Desktop/image/'

    # for j in range(1,999):
    #     # if round(j-num)%10==0:
    #         # print(("{}~"+str(num+200)).format(num) + "区间已完成  " + str((j-num)/2) + "%")
    logger.debug('downloading the file')
    #
    #
    #     for i in range(1,200):
    #         for k in range(1,200):
                # url='http://img15.yixiu8.com:8080/picture/170{}/pic{}/{}.jpg'.format(j,i,k)
    url="http://img15.yixiu8.com:8080/picture/171120/pic24/114.jpg"

    print(url)
    local_filename = "yixiu" + str(time.time()) + ".jpg"
    # try:
    r = requests.get(url, stream=True) # here we need to set stream = True parameter
    print(r)
    if r and not os.path.exists(dir + local_filename):
        if not os.path.exists(dir):
            os.makedirs(dir)
        urllib.urlretrieve(url,dir+local_filename)
            # with open(dir + local_filename, 'wb') as f:
            #     for chunk in r.iter_content(chunk_size=1024):
            #         if chunk:  # filter out keep-alive new chunks
            #             f.write(chunk)
            #             f.flush()
            #     f.close()
    # except Exception as e:
    #     print(e)


if __name__ == '__main__':

    starttime = time.time()
    logger = get_logger()
    # name = ['a', 'b', 'c', 'd', 'e']
    # start = [1, 250, 500, 750]
    # data = zip(name, start)
    # for j, i in data:
    p = Process(target=get_beauty,args=(logger,))
    p.start()