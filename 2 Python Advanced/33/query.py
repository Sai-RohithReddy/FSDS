import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()

mycursor.execute("select * from ineuron.fsds")

for i in mycursor:
    print(i)

mycursor.execute('select studentid , firstname, class from ineuron.fsds')

for i in mycursor:
    print(i)

mycursor.execute('select * from ineuron.fsds where studentid = 130 ')

for i in mycursor:
    print(i)

mycursor.execute('select * from ineuron.fsds where studentid > 130 ')

for i in mycursor:
    print(i)

mycursor.execute("select * from ineuron.fsds where firstname = 'shubham' and class = 'sql'")

for i in mycursor:
    print(i)

mycursor.execute("update ineuron.fsds set firstname = 'roshan' where studentid = 125 ")

mydb.commit()

mycursor.execute("update ineuron.fsds set class = 'mysql'")
mydb.commit()

mycursor.execute("delete from ineuron.fsds where lastname = 'gupta'")
mydb.commit()


mycursor.execute("select min(studentid) from ineuron.fsds")

for i in mycursor:
    print(i)

mycursor.execute("select max(studentid) from ineuron.fsds")

for i in mycursor:
    print(i)

mycursor.execute("select count(*) from ineuron.fsds")

for i in mycursor:
    print(i)


mycursor.execute("update ineuron.fsds set class = 'sql' where studentid between 125 and 128 ")
mydb.commit()


mycursor.execute("update ineuron.fsds set class = 'mongodb' where studentid between 129 and 133 ")
mydb.commit()

mycursor.execute("select count(*) ,class from ineuron.fsds group by class")
for i in mycursor:
    print(i)

#mycursor.execute("drop table ineuron.fsds")
mydb.commit()

mycursor.execute("drop database ineuron")
