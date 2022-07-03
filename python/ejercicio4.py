import sqlite3;
import pandas as pd;

con = sqlite3.connect('SISTINF.db');

query = con.execute("SELECT nombre, emailsPhising, emailsClicados From users")
cols = [column[0] for column in query.description]
dUsersCrit = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)
dUsersCrit['critico'] = dUsersCrit['emailsClicados']/dUsersCrit['emailsPhising']
dUsersCrit = dUsersCrit.sort_values(by=['critico'], ascending=False, ignore_index=True).loc[:9]
dUsersCrit.plot(kind='bar', x='nombre', y='critico')

query = con.execute("SELECT * From legal")
cols = [column[0] for column in query.description]
dWebPol = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)
dWebPol = dWebPol.sort_values(by=['cookie','aviso','proteccion'], ascending=False, ignore_index=True).loc[:4]
dWebPol.plot(kind='bar', x='url')

plt.show();

con.close()
