from tornado import web
from tornado import gen
from tornado import log
from utils.urlmap import urlmap
from models import activity
from pony.orm import db_session

@urlmap(appkey=[1, 2], url=r'/home')
class Home(web.RequestHandler):

    def get(self):
        self.write('Paty Go!!!')
        with db_session:
            activity.Activity()
