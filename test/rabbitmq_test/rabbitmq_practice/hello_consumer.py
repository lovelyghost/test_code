# -*- coding: utf-8 -*-

import pika,sys
# 建立连接
credentials = pika.PlainCredentials("guest","guest")
conna_params = pika.ConnectionParameters("localhost",credentials=credentials)
conn_broker = pika.BlockingConnection(conna_params)

# 获取信道
channel = conn_broker.channel()

# 声明交换器
channel.exchange_declare(exchange="hello-exchange",
                         exchange_type="direct",
                         passive = False,
                         durable = True,
                         auto_delete=False
                         )

# 声明队列
channel.queue_declare(queue="hello-queue")

# 通过键 hola将队列和交换器绑定起来
channel.queue_bind(queue="hello-queue",
             exchange="hello-exchange",
             routing_key="hola")

# 用于处理消息的函数
def msg_consumer(channel,method,header,body):
    # 消息确认
    channel.basic_ack(delivery_tag=method.delivery_tag)
    if body == "quit":
        channel.basic_cancel(consumer_tag="hello-consumer")  # 停止消费并退出
        channel.stop_consuming()
    else:
        print body
    return

# 订阅消息并处理消息
channel.basic_consume(msg_consumer,
                      queue="hello-queue",
                      consumer_tag="hello-consumer"
                      )
# 开始消费
channel.start_consuming()