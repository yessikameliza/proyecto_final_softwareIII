# enconding: utf-8
# IMPORTANTE convertir el script a la codificación UTF-8
import sqlite3

# Conectamos a la base de datos
conexion = sqlite3.connect("dataBase.sqlite3")

# Seleccionamos el cursor para realizar la consulta
consulta = conexion.cursor()

# String con la consulta para crear la tabla
sql = """CREATE TABLE IF NOT EXISTS docent( 
id_Docent INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
name VARCHAR(100) NOT NULL,
estate VARCHAR(50) NOT NULL,
limitHoras INTEGER NOT NULL,
contract VARCHAR(200) NOT NULL,
phone VARCHAR(100) NOT NULL,
identification VARCHAR(100),
city VARCHAR(200))"""

sql2 = """CREATE TABLE IF NOT EXISTS semester( 
id_Semester INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
num_semester INTEGER NOT NULL)"""
sql3 = """CREATE TABLE IF NOT EXISTS hour( 
id_Hour INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
hour_ini VARCHAR(10) NOT NULL,
hour_fin VARCHAR(10) NOT NULL)"""
sql4 = """CREATE TABLE IF NOT EXISTS block( 
id_block INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
TypeBlock VARCHAR(2) NOT NULL)"""
sql5 = """CREATE TABLE IF NOT EXISTS matter( 
id_Matter INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
codigo VARCHAR(50) NOT NULL,
name VARCHAR(500) NOT NULL,
ubi_Semester INTEGER NOT NULL,
numCredit VARCHAR(10) NOT NULL,
codRequisite VARCHAR(50) NOT NULL,
id_block INTEGER,
numHoursSem INTEGER,
FOREIGN KEY (id_block) REFERENCES block (id_block)
ON DELETE CASCADE ON UPDATE NO ACTION)"""
sql6 = """CREATE TABLE IF NOT EXISTS admin( 
id_Admin INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
user VARCHAR(200) NOT NULL,
password VARCHAR(100) NOT NULL)"""
sql7 = """CREATE TABLE IF NOT EXISTS city( 
id_city INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
name_City VARCHAR(200) NOT NULL)"""
sql8 = """CREATE TABLE IF NOT EXISTS date( 
id_Date INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
Date VARCHAR(50) NOT NULL,
origin VARCHAR(100) NOT NULL,
id_block INTEGER, idents VARCHAR(100),
FOREIGN KEY (id_block) REFERENCES block (id_block)
ON DELETE CASCADE ON UPDATE NO ACTION)"""
sql9 = """ CREATE TABLE IF NOT EXISTS matter_date(
 id_Matter integer,
 id_Date integer,
 PRIMARY KEY (id_Matter, id_Date),
 FOREIGN KEY (id_Matter) REFERENCES matter (id_Matter) 
 ON DELETE CASCADE ON UPDATE NO ACTION,
 FOREIGN KEY (id_Date) REFERENCES date (id_Date) 
 ON DELETE CASCADE ON UPDATE NO ACTION)"""
sql10 = """ CREATE TABLE IF NOT EXISTS matter_hour(
 id_Matter integer,
 id_Hour integer,
 PRIMARY KEY (id_Matter, id_Hour),
 FOREIGN KEY (id_Matter) REFERENCES matter (id_Matter) 
 ON DELETE CASCADE ON UPDATE NO ACTION,
 FOREIGN KEY (id_Hour) REFERENCES hour (id_Hour) 
 ON DELETE CASCADE ON UPDATE NO ACTION)"""
sql11 = """ CREATE TABLE IF NOT EXISTS date_hour(
 id_Date integer,
 id_Hour integer,
 PRIMARY KEY (id_Date, id_Hour),
 FOREIGN KEY (id_Date) REFERENCES date (id_Date) 
 ON DELETE CASCADE ON UPDATE NO ACTION,
 FOREIGN KEY (id_Hour) REFERENCES hour (id_Hour) 
 ON DELETE CASCADE ON UPDATE NO ACTION)"""
sql12 = """ CREATE TABLE IF NOT EXISTS docent_matter(
 id_Docent integer,
 id_Matter integer,
 PRIMARY KEY (id_Docent, id_Matter),
 FOREIGN KEY (id_Docent) REFERENCES docent (id_Docent) 
 ON DELETE CASCADE ON UPDATE NO ACTION,
 FOREIGN KEY (id_Matter) REFERENCES matter (id_Matter) 
 ON DELETE CASCADE ON UPDATE NO ACTION)"""
sql13 = """ CREATE TABLE IF NOT EXISTS docent_city(
 id_Docent integer,
 id_city integer,
 PRIMARY KEY (id_Docent, id_city),
 FOREIGN KEY (id_Docent) REFERENCES docent (id_Docent) 
 ON DELETE CASCADE ON UPDATE NO ACTION,
 FOREIGN KEY (id_city) REFERENCES city (id_city) 
 ON DELETE CASCADE ON UPDATE NO ACTION)"""
sql50 = """ALTER TABLE docent ADD COLUMN matter VARCHAR(200)"""
# Ejecutamos la consulta
if consulta.execute(sql50):
    print("Tabla creada con éxito")
else:
    print("Ha ocurrido un error al crear la tabla")

# Cerramos la consulta
consulta.close()

# Guardamos los cambios
conexion.commit()

# Cerramos la conexión
conexion.close()