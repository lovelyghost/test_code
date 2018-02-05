 # -*- coding:utf-8 -*-

# 1. "from __future__ import absolute_import"是拒绝隐式引入，因为celery.py的名字和celery的包名冲突，需要使用这条语句让程序正确地运行。
#
# 2. app是Celery类的实例，创建的时候添加了proj.tasks这个模块，也就是包含了proj/tasks.py这个文件。
#
# 3. 把Celery配置存放进proj/celeryconfig.py文件，使用app.config_from_object加载配置。

from __future__ import absolute_import

from celery import Celery

app = Celery('proj', include=['tasks'])

app.config_from_object('celeryconfig')


if __name__ == '__main__':

    app.start()