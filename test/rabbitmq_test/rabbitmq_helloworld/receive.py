#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pika
#第一步还是创建connection。第二步创建channel。第三步创建queue，name = hello
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()
#创建名字为hello的queue
channel.queue_declare(queue='hello')

print (' [*] Waiting for messages. To exit press CTRL+C')

#接下来要subscribe了。在这之前，需要声明一个回调函数来处理接收到的数据。
def callback(ch, method, properties, body):
    print (" [x] Received %r" % (body,))

#subscribe 订阅
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)
#无限循环监听
channel.start_consuming()
