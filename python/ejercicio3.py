import sqlite3;
import pandas as pd;

con = sqlite3.connect('SISTINF.db');

query = con.execute("SELECT * From users where permisos  = 0")
cols = [column[0] for column in query.description]
dUsersUser = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)

query = con.execute("SELECT * From users where permisos  = 1")
cols = [column[0] for column in query.description]
dUsersAdmin = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)

query = con.execute("SELECT * From users where permisos  = 0 and emailsPhising = -1")
cols = [column[0] for column in query.description]
dUsersUserMiss = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)

query = con.execute("SELECT * From users where permisos  = 1 and emailsPhising = -1")
cols = [column[0] for column in query.description]
dUsersAdminMiss = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)

query = con.execute("SELECT * From users where emailsPhising >= 200")
cols = [column[0] for column in query.description]
dUsersMas200 = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)

query = con.execute("SELECT * From users where emailsPhising < 200")
cols = [column[0] for column in query.description]
dUsersMenos200 = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)


con.close()

print("USUARIOS")

print("El número de observaciones es:", dUsersUser['emailsPhising'].count())
print("El número de valores ausentes es:", dUsersUserMiss['emailsPhising'].count())
print("La mediana es:", dUsersUser['emailsPhising'].median())
print("La media es:",dUsersUser['emailsPhising'].mean())
print("La varianza es:", dUsersUser['emailsPhising'].var())
print("El valor mínimo y máximos es:", dUsersUser['emailsPhising'].min(),
      "y el valor máximo es", dUsersUser['emailsPhising'].max())

print("\nADMIN")
print("El número de observaciones es:", dUsersAdmin['emailsPhising'].count())
print("El número de valores ausentes es:", dUsersAdminMiss['emailsPhising'].count())
print("La mediana es:", dUsersAdmin['emailsPhising'].median())
print("La media es:",dUsersAdmin['emailsPhising'].mean())
print("La varianza es:", dUsersAdmin['emailsPhising'].var())
print("El valor mínimo y máximos es:", dUsersAdmin['emailsPhising'].min(),
      "y el valor máximo es", dUsersAdmin['emailsPhising'].max())


print("\nMENOS DE 200 CORREOS")
print("El número de observaciones es:", dUsersMenos200['emailsPhising'].count())
print("La mediana es:", dUsersMenos200['emailsPhising'].median())
print("La media es:",dUsersMenos200['emailsPhising'].mean())
print("La varianza es:", dUsersMenos200['emailsPhising'].var())
print("El valor mínimo y máximos es:", dUsersMenos200['emailsPhising'].min(),
      "y el valor máximo es", dUsersMenos200['emailsPhising'].max())


print("\nMAS DE 200 CORREOS")
print("El número de observaciones es:", dUsersMas200['emailsPhising'].count())
print("La mediana es:", dUsersMas200['emailsPhising'].median())
print("La media es:",dUsersMas200['emailsPhising'].mean())
print("La varianza es:", dUsersMas200['emailsPhising'].var())
print("El valor mínimo y máximos es:", dUsersMas200['emailsPhising'].min(),
      "y el valor máximo es", dUsersMas200['emailsPhising'].max())
