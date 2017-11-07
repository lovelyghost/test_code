#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')

severity = 'hello'
message = 'Hello World!'
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
print (" [x] Sent %r:%r" % (severity, message))
connection.close()