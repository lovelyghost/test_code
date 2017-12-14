# -*- coding:utf-8 -*-

from concurrent.futures import ProcessPoolExecutor
import requests
import time
URLS = ['http://www.163.com', 'https://www.baidu.com/', 'https://github.com/', 'https://www.youtube.com/']

def load_url(url):
    time.sleep(5)
    print(url)
    print(requests.get(url).status_code)

executor = ProcessPoolExecutor(max_workers=3)

if __name__ == '__main__': # 要加main

    for url in URLS:
        future = executor.submit(load_url,url)
        print(future.done())
    print('主线程')



# (test_code_env) lxdeMacBook-Pro% python test/futures_l/futures_process.py
# False
# False
# False
# False
# 主线程
# http://www.163.com
# https://www.baidu.com/
# https://github.com/
# 200
# 200
# 200
# https://www.youtube.com/