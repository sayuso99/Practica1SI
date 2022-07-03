import json;
import sqlite3;

con = sqlite3.connect('SISTINF.db')


def sql_insert_legal(url, cookie, aviso, proteccion, creacion):
    cursorObj = con.cursor()
    cursorObj.execute(
        "INSERT INTO legal VALUES ('" + url + "','" + cookie + "','" + aviso + "','" + proteccion + "','" + creacion + "') ")
    con.commit()


arch = open("legal.json", "r");
lineas = json.load(arch);

i = 0;
while i < len(lineas["legal"]):
    clave = lineas["legal"][i].keys();
    sql_insert_legal(list(clave)[0], str(lineas["legal"][i][list(clave)[0]]["cookies"]),
                     str(lineas["legal"][i][list(clave)[0]]["aviso"]),
                     str(lineas["legal"][i][list(clave)[0]]["proteccion_de_datos"]),
                     str(lineas["legal"][i][list(clave)[0]]["creacion"]));
    i = i + 1;


def sql_insert_users(nombre, telefono, contrasena, provincia, permisos, emailsTot, emailsPhis, emailsCic):
    cursorObj = con.cursor()
    cursorObj.execute(
        "INSERT INTO USERS VALUES ('" + nombre + "','" + telefono + "','" + contrasena + "','" + provincia + "','" + permisos + "','" + emailsTot + "','" + emailsPhis + "','" + emailsCic + "') ")
    con.commit()


def sql_insert_fec_users(user, fecha):
    cursorObj = con.cursor()
    cursorObj.execute("INSERT INTO FECHAS_USER VALUES ('" + user + "','" + fecha + "') ")
    con.commit()


def sql_insert_ips_users(user, ip):
    cursorObj = con.cursor()
    cursorObj.execute("INSERT INTO IPS_USER VALUES ('" + user + "','" + ip + "') ")
    con.commit()


arch = open("users.json", "r");
lineas = json.load(arch);

i = 0;
while i < len(lineas["usuarios"]):
    clave = lineas["usuarios"][i].keys();
    sql_insert_users(list(clave)[0], str(lineas["usuarios"][i][list(clave)[0]]["telefono"]),
                     str(lineas["usuarios"][i][list(clave)[0]]["contrasena"]),
                     str(lineas["usuarios"][i][list(clave)[0]]["provincia"]),
                     str(lineas["usuarios"][i][list(clave)[0]]["permisos"]),
                     str(lineas["usuarios"][i][list(clave)[0]]["emails"]["total"]),
                     str(lineas["usuarios"][i][list(clave)[0]]["emails"]["phishing"]),
                     str(lineas["usuarios"][i][list(clave)[0]]["emails"]["cliclados"]));
    x = 0;
    while x < len(lineas["usuarios"][i][list(clave)[0]]["fechas"]):
        sql_insert_fec_users(list(clave)[0], str(lineas["usuarios"][i][list(clave)[0]]["fechas"][x]));
        x = x + 1;
    x = 0;
    while x < len(lineas["usuarios"][i][list(clave)[0]]["ips"]):
        sql_insert_ips_users(list(clave)[0], str(lineas["usuarios"][i][list(clave)[0]]["ips"][x]));
        x = x + 1;
    i = i + 1;


con.close()

