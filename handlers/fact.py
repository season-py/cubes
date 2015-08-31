from handlers.base import BaseHandler
from tornado import gen, web
from utils.urlmap import urlmap
from tasks import tasks

@urlmap(url=r'/cube/(?P<cube_name>[^\/]+)/fact')
class HomeHandler(base.BaseHandler):

    @web.asynchronous
    @gen.coroutine
    def get(self, cube_name):
        response = yield gen.Task(tasks.foods.apply_async, args=[])
        self.finish(response.result)

