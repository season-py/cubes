import os
import decimal
from datetime import datetime
from pony.orm import *
from settings import SETTINGS

sqlite_file = os.path.join(SETTINGS['sqlite_path'], 'canteen.sqlite')
db = Database()
db.bind('sqlite', sqlite_file, create_db=True)


class Restaurant(db.Entity):
    name = Required(unicode)
    addr = Required(unicode)
    telephone = Required(int)
    foods = Set('Food')
    add_dt = Required(datetime, default=datetime.now())


class Food(db.Entity):
    name = Required(unicode)
    restaurant = Required('Restaurant')
    price = Required(decimal.Decimal, 10, 2, default=0)
    description = Required(unicode)
    pictures = Set('Picture')
    comments = Set('Comment')
    orders = Set('Order')
    likes = Required(int)
    dislikes = Required(int)
    like_customers = Set('Like')
    dislike_customers = Set('Dislike')
    add_dt = Required(datetime, default=datetime.now())


class Sex(db.Entity):
    name = Required(unicode)
    customer = Optional('Customer')
    add_dt = Required(datetime, default=datetime.now())


class Like(db.Entity):
    food = Required('Food')
    customer = Required('Customer')
    add_dt = Required(datetime, default=datetime.now())


class Dislike(db.Entity):
    food = Required('Food')
    customer = Required('Customer')
    add_dt = Required(datetime, default=datetime.now())


class Customer(db.Entity):
    name = Required(unicode)
    email = Required(unicode)
    telephone = Required(int)
    sex = Required('Sex')
    like_foods = Set('Like')
    dislike_foods = Set('Dislike')
    comments = Set('Comment')
    orders = Set('Order')
    add_dt = Required(datetime, default=datetime.now())


class Order(db.Entity):
    customer = Required('Customer')
    foods = Set('Food')
    add_dt = Required(datetime, default=datetime.now())


class Comment(db.Entity):
    score = Required(int)
    comment = Required(unicode)
    food = Required('Food')
    customer = Required('Customer')
    add_dt = Required(datetime, default=datetime.now())


class Picture(db.Entity):
    url = Required(unicode)
    food = Required('Food')
    add_dt = Required(datetime, default=datetime.now())

db.generate_mapping(create_tables=True)
