from tornado import web
from tornado import gen
from tornado import log
from utils.urlmap import urlmap

@urlmap(appkey=[1, 2], url=r'/')
class Map(web.RequestHandler):

    @web.authenticated
    def get(self):
        self.write('Welcome To HousingMap')
        print self.get_current_user()

