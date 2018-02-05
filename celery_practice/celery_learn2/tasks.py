# -*- coding: utf-8 -*-
# celery worker -A tasks --loglevel=info 启动celery --loglevel=info 日志级别
import time
from celery import Celery
broker = 'redis://127.0.0.1:6379'
backend =  'redis://127.0.0.1:6379/0'
app = Celery('tasks',broker=broker,backend=backend)
@app.task
def add(x, y):
    time.sleep(5)     # 模拟耗时操作
    return x + y


