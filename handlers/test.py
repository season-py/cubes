from tornado import web
from tornado import gen
from utils.urlmap import urlmap

@urlmap(url=r'/test')
class User(web.RequestHandler):

    @gen.coroutine
    def get(self):
        self.render('test.html')
