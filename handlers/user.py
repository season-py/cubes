from tornado import web
from tornado import gen
from utils.urlmap import urlmap

@urlmap(appkey=1, url=r'/user/\d+')
class User(web.RequestHandler):

    @gen.coroutine
    def get(self):
        self.write('Hello World')

