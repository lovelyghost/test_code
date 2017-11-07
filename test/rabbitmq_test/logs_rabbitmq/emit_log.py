#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import pika
# logs_rabbitmq 广播形式,信息分发给所有有绑定exchange的消费者
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()
#Producer发送的Message实际上是发到了Exchange中。它的功能也很简单：从Producer接收Message，然后投递到queue中。Exchange需要知道如何处理Message，是把它放到那个queue中，还是放到多个queue中？这个rule是通过Exchange 的类型定义的

channel.exchange_declare(exchange='logs',
                         type='fanout')#fanout就是广播模式，会将所有的Message都放到它所知道的queue中。创建一个名字为logs，类型为fanout的Exchange：

message = '.'*random.randint(2,200) or "info: Hello World!"
#使用exchange发布信息,广播形式的routing_key可以被忽略,广播形式的message发给所有的queue
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print (" [x] Sent %r" % (message,))
connection.close()