# coding: utf-8
class Matter(object):
    codigo: str
    name: str
    ubi_Semester: int
    numCredit: str
    codRequisite: str
    numHoursSem: int

    def __init__(self, codigo, name, ubi_Semester, numCredit, codRequisite, numHoursSem):
        self.codigo = codigo
        self.name = name
        self.ubi_Semester = ubi_Semester
        self.numCredit = numCredit
        self.codRequisite = codRequisite
        self.numHoursSem = numHoursSem
