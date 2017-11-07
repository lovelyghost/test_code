# -*- coding: utf-8 -*-
from datetime import timedelta
from celery.schedules import crontab
from celery.utils.log import get_task_logger

from kombu import Queue, Exchange

BROKER_URL = 'redis://127.0.0.1:6379'               # 指定 Broker
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'  # 指定 Backend

logger = get_task_logger(__name__)

CELERY_TIMEZONE='Asia/Shanghai'                     # 指定时区，默认是 UTC
# CELERY_TIMEZONE='UTC'

CELERY_IMPORTS = (                                  # 指定导入的任务模块
    'celery_app.task1',
    'celery_app.task2',
    'celery_app.task3'
)


# rebbitmq 专用任务队列
# CELERY_QUEUES = ( # 定义任务队列
#
# Queue("default",Exchange("default"), routing_key="default"), # 路由键以“task.”开头的消息都进default队列
#
# Queue("web_tasks",Exchange("tasks"), routing_key="web"), # 路由键以“web.”开头的消息都进web_tasks队列
#
# )
#
# CELERY_ROUTES = {'task1.add': {"queue": "web_tasks", "routing_key": "web"},
#                 'task2.multiply':{"queue": "web_tasks", "routing_key": "web"},
#                  'task3.div':{"queue": "web_tasks", "routing_key": "web"},
#                  }

CELERY_DEFAULT_EXCHANGE = 'default' # 默认的交换机名字为tasks

CELERY_DEFAULT_EXCHANGE_TYPE = 'topic' # 默认的交换类型是topic

CELERY_DEFAULT_ROUTING_KEY = 'task.default' # 默认的路由键是task.default，这个路由键符合上面的default队列
# schedules
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
         'task': 'celery_app.task1.add',
         'schedule': timedelta(seconds=3),       # 每 30 秒执行一次
         'args': (5, 8)                           # 任务函数参数
    },
    'multiply-at-some-time': {
        'task': 'celery_app.task2.multiply',
        'schedule': crontab(hour=9, minute=50),   # 每天早上 9 点 50 分执行一次
        'args': (3, 7)                            # 任务函数参数
    },
    'div-at-some-time': {
        'task': 'celery_app.task3.div',
        'schedule': timedelta(seconds=3),   # 每 30 秒执行一次
        'args': (3, 0)  # 任务函数参数
    }
}