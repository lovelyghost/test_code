#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         type='topic') #主题信息发送

routing_key = 'anonymous.warning'
message = 'Hello World!'
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)
print (" [x] Sent %r:%r" % (routing_key, message))
connection.close()


# Producer发送消息时需要设置routing_key，routing_key包含三个单词和两个点号。第一个key是描述了celerity（灵巧，敏捷），第二个是colour（色彩），第三个是species（物种）："<celerity>.<colour>.<species>"。