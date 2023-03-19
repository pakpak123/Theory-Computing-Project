import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Pondps123",
  database="test"
)

#-----data Chachoengsao Temple-----
table_name1 = "Chachoengsao_Temple"
mycursor = db.cursor()
mycursor.execute("SELECT name FROM " + table_name1)
myresult = mycursor.fetchall()
list1 = []
for x in myresult:
  list1.append(x[0])
#print(list1)

#-----data Chainat Temple-----
table_name2 = "Chainat_Temple"
mycursor.execute("SELECT name FROM " + table_name2)
myresult = mycursor.fetchall()
list2 = []
for x in myresult:
  list2.append(x[0])
#print(list2)

#-----data Chaiyaphum Temple-----
table_name3 = "Chaiyaphum_Temple"
mycursor.execute("SELECT name FROM " + table_name3)
myresult = mycursor.fetchall()
list3 = []
for x in myresult:
  list3.append(x[0])
#print(list3)

#-----data Chonburi Temple-----
table_name4 = "Chonburi_Temple"
mycursor.execute("SELECT name FROM " + table_name4)
myresult = mycursor.fetchall()
list4 = []
for x in myresult:
  list4.append(x[0])
#print(list4)

mycursor.close()
db.close()