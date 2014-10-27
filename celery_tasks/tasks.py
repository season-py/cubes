import sys
import time
from pony.orm import db_session, select, desc
from models.canteen import Food
sys.path.append('/home/season/works')
from celery_test.celery import celery


@celery.task(name='tasks.foods')
@db_session
def foods(*args, **kwargs):
    foods = select(f for f in Food).order_by(
        desc(Food.likes), Food.dislikes)[:]
    return foods
