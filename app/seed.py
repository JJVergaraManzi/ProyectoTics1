from config import *
import psycopg2

conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))
cur = conn.cursor()

sql = """
insert into usuario (rut, apellido, nombre , contrasena)
values ('178665463','Perez','Juan', '123456')
returning
rut, apellido , nombre ,contrasena;
"""

cur.execute(sql)
conn.commit()
usuario = cur.fetchone()
print ("en el usuario :" )
print(usuario)
