# coding: utf-8
from logica.Matter import Matter
from DB.InsertarDatos import insertMatter
from DB.InsertarDatos import insertDocent
from logica.Date import Date


def register_Matter(codigo, name, ubi_Semester, numCredit, codRequisite, numHoursSem):
    matter = Matter()
    matter.codigo = codigo
    matter.name = name
    matter.ubi_Semester = ubi_Semester
    matter.numCredit = numCredit
    matter.codRequisite = codRequisite
    matter.numHoursSem = numHoursSem
    insertMatter(matter)


def register_Docent(name: str, state: str, limitHours: int, contract: str, phone: str, identification: str):

    nom: str = name
    stat: str = state
    limitHour: int = limitHours
    contra: str = contract
    phonen: str = phone
    identi: str = identification
    print(stat)
    print(limitHour)
    print(contra)
    print(phonen)
    print(nom)
    print(identi)
    insertDocent(nom, stat, limitHour, contra, phonen, identi)


def register_Date(date, origin):
    dateInst = Date()
    dateInst.date = date
    dateInst.origin = origin
