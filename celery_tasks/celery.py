from __future__ import absolute_import
import celery
from datetime import timedelta
from kombu import Exchange, Queue
from kombu.common import Broadcast

celery = celery
app = celery.Celery('tasks')

app.conf.update(
    BROKER_URL='amqp://guest@localhost:5672/celery',
    CELERY_IMPORTS=('celery_tasks.tasks', ),
    CELERY_TASK_RESULT_EXPIRES=18000,
    CELERY_RESULT_BACKEND='amqp',
    # CELERY_RESULT_DBURI='mysql://root@localhost:3306/celery',
    # CELERY_RESULT_SERIALIZER='json',
    # CELERYD_CONCURRENCY=4,
    CELERYD_PREFETCH_MULTIPLIER = 100,
    CELERY_ANNOTATIONS = {'*': {'rate_limit': '1000/s'}},

    # CELERY_ROUTES={
    # 	'tasks.add': {'queue': 'default'}
    # },
    CELERYBEAT_SCHEDULE={
        'tasks.add': {
            'task': 'tasks.add',
            'schedule': timedelta(seconds=60),
            'args': (0, 0)
        }
    },
    # CELERY_DEFAULT_QUEUE = 'celery',
    # CELERY_QUEUES=(
    # 	Queue('celery', Exchange('direct'), routing_key='celery'),
    # )
    # CELERY_QUEUES = (Broadcast('broadcast_tasks'), )
)
