from base import BaseHandler
from tornado import gen, web, template
from utils.urlmap import urlmap
from pony.orm import db_session
from models.canteen import Food
from futures import ThreadPoolExecutor
from tornado.concurrent import run_on_executor


@urlmap(appkey=[1, 2], url=r'/foods')
class Foods(BaseHandler):

    executor = ThreadPoolExecutor(100)

    @web.asynchronous
    @gen.coroutine
    def get(self):
        html = yield self.foods()
        self.write(html)
        self.finish()

    @run_on_executor
    def foods(self, *args, **kwargs):
        import time
        time.sleep(5)
        with db_session:
            foods = select(f for f in Food).order_by(
                desc(Food.likes), Food.dislikes)[:]
            self.context.foods = foods
            return self.render_string("home.html", **self.context)
