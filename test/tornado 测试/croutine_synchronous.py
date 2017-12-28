
import urllib2 as urllib
import time

def http_blockway(url1, url2):

    begin = time.time()
    data1 = urllib.urlopen(url1).read()
    data2 = urllib.urlopen(url2).read()
    print len(data1), len(data2)
    print'http_blockway cost', time.time() - begin
    
if __name__ == '__main__':
    url_list = [ 'http://www.baidu.com/','https://www.bing.com']    
    http_blockway(*url_list)
    