#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import pika
#第一步还是创建connection。第二步创建channel。第三步创建queue，name = hello
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()
#创建名字为hello的queue
# channel.queue_declare(durable=True,queue='hello')
channel.queue_declare(durable=True,queue='task_queue')

print (' [*] Waiting for messages. To exit press CTRL+C')

#接下来要subscribe了。在这之前，basic_ack需要声明一个回调函数来处理接收到的数据。
def callback(ch, method, properties, body):
    print (" [x] Received %r" % (body,))
    print (body.count('.'))
    ch.basic_ack(delivery_tag = method.delivery_tag)
#subscribe 订阅 no_ack表示不确认消息是否接收或者处理完
channel.basic_consume(callback,
                      queue='hello')
#通过 basic.qos 方法设置prefetch_count=1 。这样RabbitMQ就会使得每个Consumer在同一个时间点最多处理一个Message。换句话说，在接收到该Consumer的ack前，他它不会将新的Message分发给它。
channel.basic_qos(prefetch_count=1)
#无限循环监听
channel.start_consuming()
