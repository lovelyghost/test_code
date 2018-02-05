
# # -*- coding:utf-8 -*-

#tasks.py
from celery import Celery, Task
from celery.utils.log import get_task_logger
import time
app = Celery('tasks',  backend='redis://localhost:6379/0', broker='redis://localhost:6379/0') #配置好celery的backend和broker
app.config_from_object('celery_config')
logger = get_task_logger(__name__)

class MyTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print 'task done: {0}'.format(retval)
        return super(MyTask, self).on_success(retval, task_id, args, kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print 'task fail, reason: {0}'.format(exc)
        return super(MyTask, self).on_failure(exc, task_id, args, kwargs, einfo)

@app.task(base=MyTask,bind=True)  #普通函数装饰为 celery task
def add(self,x, y):
    logger.info(self.request.args)
    return x + y

@app.task(bind=True)
def test_mes(self):
    for i in range(1, 11):
        time.sleep(0.1)
        self.update_state(state="PROGRESS", meta={'p': i*10})
    return 'finish'

@app.task(bind=True)
def period_task(self):
    print ('period task done,fuck you there: {0}'.format(self.request.id))