from base import BaseHandler
from utils.urlmap import urlmap
from models.canteen import Food
from pony.orm import db_session, select, desc


@urlmap(appkey=[1, 2], url=r'/home')
class Home(BaseHandler):

    def get(self):
        with db_session:
            foods = select(a for a in Food).order_by(
                desc(Food.likes), Food.dislikes)[:]
            self.context.foods = foods
            self.render('home.html', **self.context)

