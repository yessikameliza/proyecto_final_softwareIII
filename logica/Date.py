# coding: utf-8
from sqlite3.dbapi2 import Date


class Date(object):
    date: Date
    origin: str

    def __init__(self, date, origin):
        self.date = date
        self.origin = origin
