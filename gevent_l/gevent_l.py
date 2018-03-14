# -*- coding: utf-8 -*-

import gevent
 

# ”gevent.spawn()”方法会创建一个新的greenlet协程对象，并运行它。
# ”gevent.joinall()”方法会等待所有传入的greenlet协程运行结束后再退出，
# 这个方法可以接受一个”timeout”参数来设置超时时间，单位是秒。运行上面的程序，

def test1():
    print 12
    gevent.sleep(0)
    print 34
 
def test2():
    print 56
    gevent.sleep(0)
    print 78
 
gevent.joinall([
    gevent.spawn(test1),
    gevent.spawn(test2),
])

from gevent import monkey; monkey.patch_all()
import socket
#  我们通过协程分别获取三个网站的IP地址，
# 由于打开远程地址会引起IO阻塞，所以gevent会自动调度不同的协程。
# 另外，我们可以通过协程对象的”value”属性，来获取协程函数的返回值。
urls = ['www.google.com', 'www.gevent.org', 'www.python.org']
jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
gevent.joinall(jobs, timeout=5)
 
print [job.value for job in jobs]





#  协程状态有已启动和已停止，
# 分别可以用协程对象的”started”属性和”ready()”方法来判断。
# 对于已停止的协程，可以用”successful()”方法来判断其是否成功运行且没抛异常。
# 如果协程执行完有返回值，可以通过”value”属性来获取。
# 另外，greenlet协程运行过程中发生的异常是不会被抛出到协程外的，
# 因此需要用协程对象的”exception”属性来获取协程中的异常。下面的例子很好的演示了各种方法和属性的使用。



def win():
    return 'You win!'
 
def fail():
    raise Exception('You failed!')
 
winner = gevent.spawn(win)
loser = gevent.spawn(fail)
 
print winner.started # True
print loser.started  # True
 
# 在Greenlet中发生的异常，不会被抛到Greenlet外面。
# 控制台会打出Stacktrace，但程序不会停止
try:
    gevent.joinall([winner, loser])
except Exception as e:
    # 这段永远不会被执行
    print 'This will never be reached'
 
print winner.ready() # True
print loser.ready()  # True
 
print winner.value # 'You win!'
print loser.value  # None
 
print winner.successful() # True
print loser.successful()  # False
 
# 这里可以通过raise loser.exception 或 loser.get()
# 来将协程中的异常抛出
print loser.exception




from gevent.event import Event
 
evt = Event()
#  协程间通讯
# greenlet协程间的异步通讯可以使用事件（Event）对象。
# 该对象的”wait()”方法可以阻塞当前协程，
# 而”set()”方法可以唤醒之前阻塞的协程。
# 在下面的例子中，5个waiter协程都会等待事件evt，
# 当setter协程在3秒后设置evt事件，所有的waiter协程即被唤醒。
def setter():
    print 'Wait for me'
    gevent.sleep(3)  # 3秒后唤醒所有在evt上等待的协程
    print "Ok, I'm done"
    evt.set()  # 唤醒
 
def waiter():
    print "I'll wait for you"
    evt.wait()  # 等待
    print 'Finish waiting'
 
gevent.joinall([
    gevent.spawn(setter),
    gevent.spawn(waiter),
    gevent.spawn(waiter),
    gevent.spawn(waiter),
    gevent.spawn(waiter),
    gevent.spawn(waiter)
])


print("我是美丽的分割线")
print("________________________________")

# 除了Event事件外，
# gevent还提供了AsyncResult事件，它可以在唤醒时传递消息。
# 让我们将上例中的setter和waiter作如下改动:

from gevent.event import AsyncResult
aevt = AsyncResult()
 
def hsetter():
    print 'Wait for me'
    gevent.sleep(3)  # 3秒后唤醒所有在evt上等待的协程
    print "Ok, I'm done"
    aevt.set('Hello!')  # 唤醒，并传递消息
 
def hwaiter():
    print("I'll wait for you")
    message = aevt.get()  # 等待，并在唤醒时获取消息
    print 'Got wake up message: %s' % message

gevent.joinall([
    gevent.spawn(hsetter),
    gevent.spawn(hwaiter),
    gevent.spawn(hwaiter)
])

print("我是美丽的分割线")
print("________________________________")


# 队列 Queue
# 队列Queue的概念相信大家都知道，
# 我们可以用它的put和get方法来存取队列中的元素。
# gevent的队列对象可以让greenlet协程之间安全的访问。
# 运行下面的程序，你会看到3个消费者会分别消费队列中的产品，且消费过的产品不会被另一个消费者再取到：

import gevent
from gevent.queue import Queue
 
products = Queue()
 
def consumer(name):
    while not products.empty():
        print '%s got product %s' % (name, products.get())
        gevent.sleep(0)
 
    print '%s Quit'
 
def producer():
    for i in xrange(1, 10):
        products.put(i)
 
gevent.joinall([
    gevent.spawn(producer),
    gevent.spawn(consumer, 'steve'),
    gevent.spawn(consumer, 'john'),
    gevent.spawn(consumer, 'nancy'),
])