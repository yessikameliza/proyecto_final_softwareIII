# enconding: utf-8
# IMPORTANTE codificar el script en UTF-8
import sqlite3

def upDate_Matter(codigo: str, name: str, ubi_Semester: int, numCredit: str, codRequisite: str, numHoursSem: int):
    conexion = sqlite3.connect("dataBases.sqlite3")

    consulta = conexion.cursor()
    sql2 = """UPDATE matter
     SET codigo = %s
     SET name = %s,
     SET ubi_Semester = %i
     SET numCredit = %s
     SET codRequisite = &s
     SET numHoursSem = %i
     where codigo = %s""" % codigo, name, ubi_Semester, numCredit, codRequisite, numHoursSem

    consulta.execute(sql2)
    consulta.close()
    conexion.commit()
    conexion.close()

