from datetime import datetime

from pony.orm import *

db = Database()


class App_AdsForEmployee(db.Entity):
    name = Required(str)
    type = Required(int)
    description = Required(str)
    date_of_publication = Required(datetime)


class App_BirthdaysEmployee(db.Entity):
    first_name = Required(str)
    middle_name = Optional(str)
    last_name = Required(str)
    birth_date = Required(datetime)
    email = Required(str)
    phone = Required(str)


class App_Channel(db.Entity):
    channel_id = Required(str)
    type = Required(int)


class App_TemplatesForBirthday(db.Entity):
    name = Required(str)
    template = Required(str)


db.bind(
    'postgres', 
    user='wmyjeiknukknuf', 
    password='0db1f11ac2c658b482e7c76ff3fd35d9f029be14fca26b8fc0123e44cbd25eea', 
    host='ec2-54-209-221-231.compute-1.amazonaws.com', 
    port=5432,
    database='d5dkte8bsacqeg'
)
db.generate_mapping(create_tables=False)
