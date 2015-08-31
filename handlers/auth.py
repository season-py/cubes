# coding=utf-8
from handlers.base import BaseHandler
from tornado import gen, web
from utils.urlmap import urlmap
from tasks import tasks


@urlmap(url=r'/auth')
class AuthHandler(BaseHandler):

    def get(self):
        if not self.current_user:
            return self.render('auth.html', **self.context)
        self.redirect('/foods')

    def post(self):
        email = self.get_argument('email', None)
        passwd = self.get_argument('password', None)
        redirect_to = self.get_body_argument('next', '/')
        with db_session:
            user = get(u for u in Customer if u.email == email)
            if not user:
                self.write({'code': -1, 'msg': '用户名不存在!'})
            elif user.password.password != passwd:
                self.write({'code': -1, 'msg': '用户名或密码错误!'})
            else:
                self.set_secure_cookie('user', user.email)
                self.write({'code': 0, 'url': redirect_to})

@urlmap(url="/logout")
class LogoutHandler(BaseHandler):

    def get(self):
        if self.current_user:
            self.clear_all_cookies()
        self.redirect('/foods')
