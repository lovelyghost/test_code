# -*- coding: utf-8 -*-
import pika,sys
from pika import spec
# 建立连接
credentials = pika.PlainCredentials("guest","guest")
conna_params = pika.ConnectionParameters("localhost",credentials=credentials)
conn_broker = pika.BlockingConnection(conna_params)

# 获取信道
channel = conn_broker.channel()

def confirm_handler(frame):
    if type(frame.method) == spec.Confirm.SelectOk: # 通知信道已经准备好接收消息
        print("channel in confirm mode")
    elif type(frame.method) == spec.Basic.Nack: # 由于 rabbitmq 内部错误导致数据丢失
        if frame.method.delevery_tag in msg_ids:
            print("message lost")
    elif type(frame.method) == spec.Basic.Ack: # 消息确认
        if frame.method.delevery_tag in msg_ids:
            print("message received ")
            msg_ids.remove(frame.method.delevery_tag)

channel.comfirm_delivery(callback=confirm_handler)

# 声明交换器
# channel.exchange_declare(exchange="hello-exchange",
#                          exchange_type="direct",
#                          passive = False,
#                          durable = True,
#                          auto_delete=False)

# 创建文本消息
msg = sys.argv[1]
msg_props = pika.BasicProperties()
msg_props.content_type="text/plain"
msg_ids = []
# 发布消息
channel.basic_publish(body=msg,
                      exchange="hello-exchange",
                      properties=msg_props,
                      routing_key="hola")
msg_ids.append(len(msg_ids) + 1)
channel.close()