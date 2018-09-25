from logica.Matter import Matter

matter = Matter()


def register_Matter(codigo, name, ubi_Semester, numCredit, codRequisite, numHoursSem):
    matter.codigo = codigo
    matter.name = name
    matter.ubi_Semester = ubi_Semester
    matter.numCredit = numCredit
    matter.codRequisite = codRequisite
    matter.numHoursSem = numHoursSem
