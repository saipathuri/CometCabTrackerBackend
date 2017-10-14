from peewee import *
import os

username = os.environ.get('DBUSERNAME', None)
password = os.environ.get('DBPASSWORD', None)
DB_endpoint = os.environ.get('DBENDPOINT', None)

if username is None or password is None or DB_endpoint is None:
    raise Exception('Could not find DB credentials')

db = MySQLDatabase("cometcabDB", host=DB_endpoint, port=3306,
                   user=username, passwd=password)


class Cab(Model):
    name = CharField(max_length=40)
    id = CharField(max_length=8, primary_key=True)
    heading = SmallIntegerField()
    ignition = BooleanField()
    latitude = CharField(max_length=15)
    longitude = CharField(max_length=15)
    moved = TimeField()
    updated = TimeField()
    velocity = SmallIntegerField()

    class Meta:
        database = db


# used to initially create the DB
def create_db():
    db.connect()
    db.create_table(Cab)
    db.close()


# returns an array of all cabs in the DB
def get_all_cabs():
    db.connect()
    cabs = []
    for cab in Cab.select():
        cabs.append(cab)

    db.close()

    return cabs


# updates all cabs in the DB
def update_all_cabs(cabs):
    db.connect()
    for cab in cabs:
        print 'Inserted Cab: %s' % cab.name
        cab.save()
    db.close()
