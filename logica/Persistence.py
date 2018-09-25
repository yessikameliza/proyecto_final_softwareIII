from logica.Matter import Matter
from logica.Docent import Docent
from DB.InsertarDatos import insertarMatter
matter = Matter()
docent = Docent()


def register_Matter(codigo, name, ubi_Semester, numCredit, codRequisite, numHoursSem):
    matter.codigo = codigo
    matter.name = name
    matter.ubi_Semester = ubi_Semester
    matter.numCredit = numCredit
    matter.codRequisite = codRequisite
    matter.numHoursSem = numHoursSem
    insertarMatter()


def register_Docent(name, limitHours, contract, phone, identification):
    docent.name = name
    docent.limitHours = limitHours
    docent.contract = contract
    docent.phone = phone
    docent.identification = identification
