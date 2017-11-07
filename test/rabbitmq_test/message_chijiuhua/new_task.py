#!/usr/bin/env python
# -*- coding: utf-8 -*-

#new_task 和 worker 持久化
import sys
import random
import pika
#程序的第一句话就是建立连接，第二句话就是创建channel：
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

# channel.exchange_declare(exchange='logs',
#                          type='fanout')#fanout就是广播模式，会将所有的Message都放到它所知道的queue中。创建一个名字为logs，类型为fanout的Exchange：


#创建名字为hello的queue 发送者和接收者都需要声明队列
#queue的持久化需要在声明时指定durable=True：
# channel.queue_declare(durable=True,queue='hello')
channel.queue_declare(durable=True,queue='task_queue')
#Producer只能发送到exchange，它是不能直接发送到queue的。现在我们使用默认的exchange（名字是空字符）。这个默认的exchange允许我们发送给指定的queue。routing_key就是指定的queue名字。

#自定义message
message = '.'*random.randint(2,200) or "Hello World!"

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent  使message持久化
                      )
                      )
print (" [x] Sent %r" % (message,) )
#退出前别忘了关闭connection。
connection.close()


#最开始定义了hello队列,后来才加上持久化并不起作用,原因就是RabbitMQ Server已经维护了一个叫hello的queue，那么上述执行不会有任何的作用，也就是hello的任何属性都不会被影响。
#    为了数据不丢失，我们采用了：

# 在数据处理结束后发送ack，这样RabbitMQ Server会认为Message Deliver 成功。
# 持久化queue，可以防止RabbitMQ Server 重启或者crash引起的数据丢失。
# 持久化Message，理由同上。
#     但是这样能保证数据100%不丢失吗？