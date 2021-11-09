import sqlalchemy
from db import db
import sqlite3
class ItemModel(db.Model):
    def __init__(self, name, price):
        self.name = name
        self.price = price


    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return ItemModel.query.filter_by(name=name).first() # select * from items WHERE name=name LIMIT 1

    @classmethod
    def insert(cls, item):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_from_db(cls, item):
        db.session.delete(self)
        db.session.commit()