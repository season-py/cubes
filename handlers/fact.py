from base import BaseHandler
from tornado import gen, web
from utils.urlmap import urlmap
from celery_tasks import tasks
from pony.orm import db_session


@urlmap(url=r'/home')
class HomeHandler(BaseHandler):

    @web.authenticated
    @web.asynchronous
    @gen.coroutine
    def get(self):
        with db_session:
            response = yield gen.Task(tasks.foods.apply_async, args=[])
            self.context.foods = response.result
            self.render('home.html', **self.context)
