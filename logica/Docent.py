# coding: utf-8

class Docent (object):
    state: str
    name: str
    limitHours: int
    contract: str
    phone: str
    identification: str

    def __init__(self, name, state, limitHours, contract, phone, identification):
        self.state = state
        self.name = name
        self.limitHours = limitHours
        self.contract = contract
        self.phone = phone
        self.identification = identification
