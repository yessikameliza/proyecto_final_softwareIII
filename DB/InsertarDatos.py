# enconding: utf-8
# IMPORTANTE convertir el script a la codificación UTF-8
import sqlite3
from logica.Persistence import Persistence
# Establecer la conexión
conexion = sqlite3.connect("DateBases.sqlite3")

# Seleccionar el cursor para iniciar una consulta
consulta = conexion.cursor()
persistence = Persistence()

print("**** Programa para insertar datos en bases de datos sqlite3 ****")
# TypeBlock = input("tipo de bloque: ")
codigo = input("Introduzca el codigo: ")
name = input("Introduzca el nombre: ")
ubi_Semester = input("Introduzca un número ubicacion semestral: ")
numCredit = input("Introduzca un número creditos: ")
codRequisite = input("Introduzca codigo requisito : ")
numHoursSem = input("Introduzca el numero de horas por semestre :")
# Capturar excepciones para los números enteros y decimal
# Sólo números enteros
try:
    ubi_Semester = int(ubi_Semester)
except ValueError:
    print(ubi_Semester, "no es un número entero")
    exit()

# Valor de los argumentos
argumentos = (codigo, name, ubi_Semester, numCredit, codRequisite, numHoursSem)
# argumentos2 = TypeBlock
# consulta SQL con argumentos ?, ?, ?, ?, ?
# sql2 = """INSERT INTO block (TypeBlock)
# VALUES (?)"""
sql = """INSERT INTO matter (codigo, name, ubi_Semester, numCredit, codRequisite, numHoursSem)
VALUES (?, ?, ?, ?, ?, ?)"""



# Realizar la consulta
if consulta.execute(sql, argumentos):
        print("Tabla creada con éxito")
else:
    print("Ha ocurrido un error al crear la tabla")

# Cerrar la consulta
consulta.close()

# Guardar los cambios en la base de datos
conexion.commit()

# Cerrar la conexión
conexion.close()
