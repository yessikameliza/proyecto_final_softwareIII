# coding: utf-8

class Admin(object):
    user: str
    password: str

    def __init__(self, user, password):
        self.user = user
        self.password = password
