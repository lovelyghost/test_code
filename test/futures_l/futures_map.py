# -*- coding:utf-8 -*-

from concurrent.futures import ThreadPoolExecutor
import requests
import time
URLS = ['http://www.163.com', 'https://www.baidu.com/', 'https://github.com/', 'https://www.youtube.com/']


def load_url(url):
    time.sleep(5)
    print(url)
    print(requests.get(url).status_code)


executor = ThreadPoolExecutor(max_workers=3)

# for url in URLS:
#     future = executor.submit(load_url, url)
#     print(future.done())

executor.map(load_url,URLS)

print('😝😝😝😝😝😝😝😝😝😝😝😝')


# (test_code_env) lxdeMacBook-Pro% python test/futures_l/futures_map.py
# 😝😝😝😝😝😝😝😝😝😝😝😝
# http://www.163.com
# https://www.baidu.com/
#  https://github.com/
# 200
# 200
# 200
# https://www.youtube.com/

# map是按照URLS列表元素的顺序返回的，

# 我们使用submit方法来往线程池中加入一个task，
# submit返回一个Future对象，对于Future对象可以简单地理解为一个在未来完成的操作。
# 由于线程池异步提交了任务，主线程并不会等待线程池里创建的线程执行完毕，
# 所以执行了print('主线程')，相应的线程池中创建的线程并没有执行完毕，故future.done()返回结果为False。