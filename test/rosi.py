# # -*- coding:utf-8 -*-
# import re
# # 多线程学习
# import logging
# import string
#
# import requests
# import os
# import random
# import threading
# import time
# from multiprocessing import Pool, Process
#
#
# def get_logger():
#     logger = logging.getLogger("threading_example")
#     logger.setLevel(logging.DEBUG)
#
#     fh = logging.FileHandler("threading.log")
#     fmt = '%(asctime)s - %(levelname)s - %(message)s'
#     formatter = logging.Formatter(fmt)
#     fh.setFormatter(formatter)
#
#     logger.addHandler(fh)
#     return logger
#
#
# def id_generator(size=32, chars=string.ascii_lowercase + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))
#
#
# def get_beauty(logger):
#     for k in range(1000):
#         id = id_generator(32)
#         filedir=r'/Users/lx/Desktop/image'
#         dir = r'/Users/lx/Desktop/image/{}/'.format(id)
#         logger.debug('downloading the {}th file'.format(id))
#
#         if not os.path.exists(filedir):
#             os.makedirs(dir)
#         else:
#             url = 'http://img.youguoquan.com/uploads/magazine/content/{}_magazine_web_m.jpg'.format(
#                 id)
#             r = requests.get(url, stream=True)  # here we need to set stream = True parameter
#             if r:
#                 with open(dir, 'wb') as f:
#                     for chunk in r.iter_content(chunk_size=1024):
#                         if chunk:  # filter out keep-alive new chunks
#                             f.write(chunk)
#                             f.flush()
#                     f.close()
#
#
#
#
# if __name__ == '__main__':
#     s = time.time()
#     logger = get_logger()
#     for i in range(10):
#         p = Process(target=get_beauty, args=(logger,))
#         p.start()
#     e = time.time()
#     print(e - s)
