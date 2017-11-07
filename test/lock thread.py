#!/usr/bin/env python
#coding=utf-8
# import threading
#
# total = 0
# num = 0
# lock = threading.RLock()
#
# def do_something(h):
#     global total
#     # with lock:
#     total += 1
#     print("total=" +h+ str(total))
#     print('~~~~~~~~~~~~~~~~~~~~')
#
#     return "do something"
#
# def do_something_else(h):
#     global num
#     # with lock:
#     num +=2
#     print("mum=" +h+ str(num))
#     print('___________________')
#
#     return "something else"
#
#
# def main(h):
#     # with lock:
#     result_one = do_something(h)
#     result_two = do_something_else(h)
#
#     print (result_one)
#     print (result_two)
#
# if __name__ == '__main__':
#     thread_names = ['Mike', 'George', 'Wanda', 'Dingbat', 'Nina']
#     for i in range(5):
#         my_thread = threading.Thread(target=main, args=(thread_names[i],))
#         my_thread.start()


import threading
from queue import Queue
def creator(data, q):
    """
    生成用于消费的数据，等待消费者完成处理
    """
    print('Creating data and putting it on the queue')
    for item in data:
        evt = threading.Event()
        q.put((item, evt))

        print('Waiting for data to be doubled')
        evt.wait()


def my_consumer(q):
    """
    消费部分数据，并做处理

    这里所做的只是将输入翻一倍

    """
    while True:
        data, evt = q.get()
        print('data found to be processed: {}'.format(data))
        processed = data * 2
        print(processed)
        evt.set()
        q.task_done()


if __name__ == '__main__':
    q = Queue()
    data = [5, 10, 13, -1]
    thread_one = threading.Thread(target=creator, args=(data, q))
    thread_two = threading.Thread(target=my_consumer, args=(q,))
    thread_one.start()
    thread_two.start()

    q.join()