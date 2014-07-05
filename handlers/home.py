from base import BaseHandler
from utils.urlmap import urlmap
from models.activity import Activity
from pony.orm import db_session, select


@urlmap(appkey=[1, 2], url=r'/home')
class Home(BaseHandler):

    def get(self):
        with db_session:
            select(a for a in Activity).order_by(Activity.add_dt)[:]
        self.context.news = "hello world"
        self.render('home.html', **self.context)
