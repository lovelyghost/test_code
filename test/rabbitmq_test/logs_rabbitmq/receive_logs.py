#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')

result = channel.queue_declare(exclusive=True) #当Consumer关闭连接时，这个queue要被deleted。可以加个exclusive的参数。
queue_name = result.method.queue #生成队列的名字,随机的,临时队列

#现在我们已经创建了fanout类型的exchange和没有名字的queue（实际上是RabbitMQ帮我们取了名字）。那exchange怎么样知道它的Message发送到哪个queue呢？答案就是通过bindings：绑定。
channel.queue_bind(exchange='logs',
                   queue=queue_name)

print (' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print (" [x] %r" % (body,))
    print (queue_name)


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()