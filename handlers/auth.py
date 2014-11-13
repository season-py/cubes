from base import BaseHandler
from tornado import gen, web
from utils.urlmap import urlmap
from celery_tasks import tasks
from pony.orm import db_session


@urlmap(url=r'/auth')
class AuthHandler(BaseHandler):

    def get(self):
        if not self.current_user:
            self.redirect('/login')
            return
        self.write('hello, ' + self.current_user)


@urlmap(url=r'/login')
class LoginHandler(BaseHandler):

    def get(self):
        pass

    def post(self):
        pass
