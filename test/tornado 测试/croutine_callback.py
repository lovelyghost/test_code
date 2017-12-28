import tornado
from tornado.httpclient import AsyncHTTPClient
import time, sys

def http_callback_way(url1, url2):
    http_client = AsyncHTTPClient()
    http_client.fetch(url1,lambda res, u = url1:handle_result(res, u))
    print('%s here between to request' % time.time())
    http_client.fetch(url2,lambda res, u = url2:handle_result(res, u))
    

def handle_result(response, url):
    begin = time.time()
    count = 0
    print('%s : handle_result with url %s' % (time.time(), url))
    count += 1
    if count == 2:
        print'http_callback_way cost', time.time() - begin
        sys.exit(0)
   


if __name__ == '__main__':

    url_list = [ 'http://www.baidu.com/','https://www.bing.com']
    http_callback_way(*url_list)
    tornado.ioloop.IOLoop.instance().start()