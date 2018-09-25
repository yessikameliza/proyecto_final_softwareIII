from logica.Matter import Matter


def register_Matter(name, ubi_Semester, numCredit, codRequisite, numHoursSem):
    matter.name = name
    matter.ubi_Semester = ubi_Semester
    matter.numCredit = numCredit
    matter.codRequisite = codRequisite
    matter.numHoursSem = numHoursSem


class Persistence(object):
    pass
