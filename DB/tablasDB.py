#enconding: utf-8
#IMPORTANTE convertir el script a la codificación UTF-8
import sqlite3

#Conectamos a la base de datos
conexion = sqlite3.connect("BaseDatosPF.sqlite3")

#Seleccionamos el cursor para realizar la consulta
consulta = conexion.cursor()

#String con la consulta para crear la tabla
sql = """CREATE TABLE IF NOT EXISTS docent( 
id_Docent INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
name VARCHAR(100) NOT NULL,
estate VARCHAR(50) NOT NULL,
limitHoras INTEGER NOT NULL,
contract VARCHAR(200) NOT NULL,
phone VARCHAR(100) NOT NULL)"""
sql2 = """CREATE TABLE IF NOT EXISTS matter( 
id_Matter INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
codigo VARCHAR(50) NOT NULL,
name VARCHAR(5) NOT NULL,
numCredit VARCHAR(10) NOT NULL,
codRequisite VARCHAR(50) NOT NULL)"""
#Ejecutamos la consulta
if (consulta.execute(sql)):
 print("Tabla creada con éxito")
 if (consulta.execute(sql2)):
  print("Tabla creada con éxito")
else: print("Ha ocurrido un error al crear la tabla")

#Cerramos la consulta
consulta.close()

#Guardamos los cambios
conexion.commit()

#Cerramos la conexión
conexion.close()