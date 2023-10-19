import mysql.connector

db = mysql.connector.connect(host="localhost",database = "burgernica", user="root",password="1234")
print(db)

#metode .cursor()

cursor = db.cursor()

#.execute()
#.execute(sql,dati)

#sql kods datu ievietošanai
sql = ("""
insert into burgeri (idburgeri,nosaukums,gala,zalumi)
values (%s,%s,%s,%s);
""")
#Ievietojamie dati
dati = (785,"Bekona burgers",60,40)

cursor.execute(sql,dati)

#Apstiprināšana
db.commit()