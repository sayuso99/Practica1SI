import sqlite3;
import pandas as pd;

con = sqlite3.connect('SISTINF.db');

query = con.execute("SELECT * From users")
cols = [column[0] for column in query.description]
dUsers = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)

query = con.execute("SELECT * From fechas_user")
cols = [column[0] for column in query.description]
dFechas_User = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)

query = con.execute("SELECT count(ip) as numAccesos From ips_user group by rtb_user")
cols = [column[0] for column in query.description]
dIPS_User = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)

query = con.execute("select count(fecha) as numAccesos from fechas_user group by rtb_user;")
cols = [column[0] for column in query.description]
dFechas_User = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)

con.close()


print("La media de correos recibidos son:", dUsers['emailsPhising'].mean())
print("La desviacion estándar de correos recibidos son: ", dUsers['emailsPhising'].std())
print("El valor máximo de correos recibidos es:", dUsers['emailsTotal'].max())
print("La valor mínimo de correos recibidos es:", dUsers['emailsTotal'].min())


print("El valor máximo de las fechas que se ha iniciado sesión es:", dFechas_User['numAccesos'].max())
print("El valor mínimo de las fechas que se ha iniciado sesión es:", dFechas_User['numAccesos'].min())

print("La media de accesos por IP es de:", dIPS_User['numAccesos'].mean())
print("La desviación estándar de accesos por IP es de:", dIPS_User['numAccesos'].std())