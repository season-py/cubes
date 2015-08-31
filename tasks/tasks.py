import sys
import time
from tasks.celery import app

@app.task(name='tasks.foods')
def foods(*args, **kwargs):
    return 'hello world' 
