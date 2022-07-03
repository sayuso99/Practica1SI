import json;
import sqlite3;

con = sqlite3.connect('SISTINF.db')

def sql_insert_legal(url,cookie,aviso,proteccion,creacion):
    cursorObj = con.cursor()
    cursorObj.execute("INSERT INTO legal VALUES ('"+url+"','"+cookie+"','"+aviso+"','"+proteccion+"','"+creacion+"') ")
    con.commit()
    
def sql_insert_users(nombre,telefono,contrasena,provincia,permisos,emailsTot,emailsPhis,emailsCic):
    cursorObj = con.cursor()
    cursorObj.execute("INSERT INTO USERS VALUES ('"+nombre+"','"+telefono+"','"+contrasena+"','"+provincia+"','"+permisos+"','"+emailsTot+"','"+emailsPhis+"','"+emailsCic+"') ")
    con.commit()
    
def sql_insert_fec_users(user,fecha):
    cursorObj = con.cursor()
    cursorObj.execute("INSERT INTO FECHAS_USER VALUES ('"+user+"','"+ip+"') ")
    con.commit()
    
def sql_insert_ips_users(user,ip):
    cursorObj = con.cursor()
    cursorObj.execute("INSERT INTO IPS_USER VALUES ('"+user+"','"+ip+"') ")
    con.commit()
  
arch = open("legal.json","r");
lineas = json.load(arch);

i = 0;
while i < len(lineas["legal"]):
    clave  = lineas["legal"][i].keys();
    print(list(clave)[0]);
    print(lineas["legal"][i][list(clave)[0]]);
    sql_insert_legal(list(clave)[0],str(lineas["legal"][i][list(clave)[0]]["cookies"]),str(lineas["legal"][i][list(clave)[0]]["aviso"]),str(lineas["legal"][i][list(clave)[0]]["proteccion_de_datos"]),str(lineas["legal"][i][list(clave)[0]]["creacion"]));
    i = i+1;
con.close()