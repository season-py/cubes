import os
import datetime
from pony.orm import *
from settings import SETTINGS

sqlite_file = os.path.join(SETTINGS['sqlite_path'], 'teambuilding.sqlite')
db = Database()
db.bind('sqlite', sqlite_file, create_db=True)

class Company(db.Entity):
    name = Required(unicode)
    addr = Required(unicode)
    add_dt = Required(datetime.datetime)
    departments = Set('Department')
    authors = Set('Author')

class Department(db.Entity):
    name = Required(unicode)
    num_of_employees = Required(int)
    add_dt = Required(datetime.datetime)
    company = Required(Company)
    authors = Set('Author')
 
class Sex(db.Entity):
    name = Required(unicode)
    add_dt = Required(datetime.datetime)
    author = Optional('Author')

class Author(db.Entity):
    name = Required(unicode)
    email = Required(unicode)
    telephone = Required(int)
    add_dt = Required(datetime.datetime)
    sex = Required(Sex)
    company = Required(Company)
    department = Required(Department)
    activities = Set('Activity')
    comments = Set('Comment')

class Organizer(db.Entity):
    name = Required(unicode)
    addr = Required(unicode)
    add_dt = Required(datetime.datetime)
    activities = Set('Activity')
    
class Activity(db.Entity):
    theme = Required(unicode)
    description = Required(unicode)
    members = Required(int)
    add_dt = Required(datetime.datetime)
    organizer = Required(Organizer)
    author = Required(Author)
    comments = Set('Comment')
    pictures = Set('Picture')

class Comment(db.Entity):
    score = Required(int)
    comment = Required(unicode)
    add_dt = Required(datetime.datetime)
    activity = Required('Activity')
    author = Required('Author')
 
class Picture(db.Entity):
    url = Required(unicode)
    add_dt = Required(datetime.datetime)
    activity = Required('Activity')

db.generate_mapping(create_tables=True)
