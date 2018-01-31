# # -*- coding:utf-8 -*-

from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import time
import os


def tick():
    print('Tick! The time is: %s' % datetime.now())

scheduler = BackgroundScheduler()
scheduler.add_job(tick, 'interval', seconds=3)
# 间隔3秒钟执行一次
scheduler.start()