from handlers.base import BaseHandler
from tornado import gen, web, template
from utils.urlmap import urlmap
from concurrent.futures import ThreadPoolExecutor
from tornado.concurrent import run_on_executor


@urlmap(url=r'/cube/(?P<cube_name>[^\/]+)/aggregates')
class FoodsHandler(BaseHandler):

    executor = ThreadPoolExecutor(100)

    @web.asynchronous
    @gen.coroutine
    def get(self, cube_name):
        html = yield self.foods()
        self.write(html)
        self.finish()

