# -*- coding: utf-8 -*-
# from celery import
from celery_app import task1
from celery_app import task3

# task1.add.apply_async(args=[2, 8])        # 也可用 task1.add.delay(2, 8)
# task2.multiply.apply_async(args=[3, 7])   # 也可用 task2.multiply.delay(3, 7)
task1.add.delay(2,3)
# print ('hello world')

#countdown：指定多少秒后执行任务
#eta (estimated time of arrival)：指定任务被调度的具体时间，参数类型是 datetime
#expires：任务过期时间，参数类型可以是 int，也可以是 datetime
# task1.add.apply_async(args=(2, 3), countdown=5)    # 5 秒后执行任务
# task2.multiply.apply_async(args=[3, 7], eta=datetime.utcnow() + timedelta(seconds=10))
# task2.multiply.apply_async(args=[3, 7], expires=10)
task3.div.apply_async((2, 0), )