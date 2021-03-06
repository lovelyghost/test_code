# # -*- coding:utf-8 -*-


# 3 Demonstrates how to use the background scheduler to schedule a job that executes on 3 second
from datetime import datetime
import time
import os
from apscheduler.schedulers.background import BackgroundScheduler


def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
     scheduler = BackgroundScheduler()
     # scheduler.add_job(tick, 'interval', seconds=3)
     scheduler.add_job(tick, 'date', run_date='2016-02-14 15:01:05') # 在指定的时间，只执行一次
     #间隔3秒钟执行一次
     scheduler.start()    #这里的调度任务是独立的一个线程
     print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
     print("what the fuck")
     try:
        # This is here to simulate application activity (which keeps the main thread alive).
         while True:
             time.sleep(2)
             #其他任务是独立的线程执行
             print('sleep!')
     except (KeyboardInterrupt, SystemExit):
         # Not strictly necessary if daemonic mode is enabled but should be done if possible
         scheduler.shutdown()
         print('Exit The Job!')
