from base import BaseHandler
from utils.urlmap import urlmap
from models.canteen import Food
from pony.orm import db_session, select, desc


@urlmap(appkey=[1, 2], url=r'/food/(like|dislike)')
class FoodLike(BaseHandler):

    def post(self, api):
        food_id = int(self.get_argument('food_id', 0))
        with db_session:
            food = Food[food_id]
            if api == 'like':
                food.likes += 1
                self.write(str(food.likes))
            elif api == 'dislike':
                food.dislikes += 1
                self.write(str(food.dislikes))


@urlmap(appkey=[1, 2], url=r'/food/detail/(\d+)')
class FoodDetail(BaseHandler):

    def get(self, food_id):
        food_id = int(food_id)
        with db_session:
            self.context.food = Food[food_id]
            self.render('food.html', **self.context)
