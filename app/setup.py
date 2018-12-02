from config import *
import psycopg2
conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))

cur = conn.cursor()

sql ="""DROP SCHEMA public CASCADE;
CREATE SCHEMA public;"""

cur.execute(sql)

sql= """
CREATE TABLE usuario(rut varchar(255) primary key, apellido varchar(255), nombre varchar(255), contrasena varchar(255));
CREATE TABLE registros(id serial PRIMARY KEY , fecha timestamp , humedad float , temperatura float);
"""
cur.execute(sql)

conn.commit()
cur.close()
conn.close()
