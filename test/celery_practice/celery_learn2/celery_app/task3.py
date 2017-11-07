
from celery_app import app
from celeryconfig import logger

@app.task(bind=True)
def div(self, x, y):
    logger.info(('Executing task id {0.id}, args: {0.args!r} '
                 'kwargs: {0.kwargs!r}').format(self.request))
    try:
        result = x / y
    except ZeroDivisionError as e:
        raise self.retry(exc=e, countdown=5, max_retries=3)
    return result