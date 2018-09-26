from logica.Matter import Matter
from logica.Docent import Docent
from DB.InsertarDatos import insertMatter
from DB.InsertarDatos import insertDocent




def register_Matter(codigo, name, ubi_Semester, numCredit, codRequisite, numHoursSem):
    matter = Matter()
    matter.codigo = codigo
    matter.name = name
    matter.ubi_Semester = ubi_Semester
    matter.numCredit = numCredit
    matter.codRequisite = codRequisite
    matter.numHoursSem = numHoursSem
    insertMatter(matter)


def register_Docent(name, state, limitHours, contract, phone, identification):
    docent = Docent()
    docent.name = name
    docent.state = state
    docent.limitHours = limitHours
    docent.contract = contract
    docent.phone = phone
    docent.identification = identification
    insertDocent(docent)