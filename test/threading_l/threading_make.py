#coding=utf-8

import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    print 'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')

t1.start()
hah = threading.local()
print(hah)


# 判断线程是否是激活的（alive）。从调用start()方法启动线程，到run()方法执行完毕或遇到未处理异常而中断 这段时间内，线程是激活的。
print(t1.is_alive())
print(t1.isAlive())

# 获取当前活动的(alive)线程的个数。
print(threading.active_count())
print(threading.activeCount())


# 获取当前的线程对象（Thread object）
print(threading.currentThread())
print(threading.current_thread())

# 调用Thread.join将会使主调线程堵塞，直到被调用线程运行结束或超时。
# 参数timeout是一个数值类型，表示超时时间，如果未提供该参数，那么主调线程将一直堵塞到被调线程结束。
t1.join()

# 获取线程的名称
print(t1.getName())
# 改变线程的名称
t1.setName("ghost")
# 获取线程的名称
print(t1.name)
# 获取线程的标识符。线程标识符是一个非零整数，只有在调用了start()方法之后该属性才有效，否则它只返回None。
print(t1.ident)

# 获取线程对象的列表
print(threading.enumerate())

# threading.Timer是threading.Thread的子类，可以在指定时间间隔后执行某个操作。
def hello():
    print "hello, world"
t = threading.Timer(3, hello)
t.start()