#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pika
#程序的第一句话就是建立连接，第二句话就是创建channel：
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()
#创建名字为hello的queue 发送者和接收者都需要声明队列
channel.queue_declare(queue='hello')
#Producer只能发送到exchange，它是不能直接发送到queue的。现在我们使用默认的exchange（名字是空字符）。这个默认的exchange允许我们发送给指定的queue。routing_key就是指定的queue名字。
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!i am a newcomer')
print (" [x] Sent 'Hello World!'")
#退出前别忘了关闭connection。
connection.close()
