import sys
import time
from celery import app
from pony.orm import db_session, select, desc
from models.canteen import Food


@app.task(name='tasks.foods')
@db_session
def foods(*args, **kwargs):
    foods = select(f for f in Food).order_by(
        desc(Food.likes), Food.dislikes)[:]
    return foods
