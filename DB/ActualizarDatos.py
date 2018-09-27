# enconding: utf-8
# IMPORTANTE codificar el script en UTF-8
import sqlite3

def upDate_Matter(codigo: str, name: str, ubi_Semester: int, numCredit: str, codRequisite: str, numHoursSem: int):
    conexion = sqlite3.connect("dataBases.sqlite3")

    consulta = conexion.cursor()
    sql2 = """UPDATE matter
     SET name = %s,
     SET ubi_Semester
     SET num
     
     where codigo = %s""" % codigo

    consulta.execute(sql2)
    consulta.close()
    conexion.commit()
    conexion.close()

