import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    database="testdb"
)

# -----------------------------Create a cursor instance-----------------------------
my_cursor = mydb.cursor()

# -----------------------------Create a Database------------------------------------
# my_cursor.execute("CREATE DATABASE testdb")

# -----------------------------Show Database----------------------------------------
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)

# -----------------------------Create a table in Database---------------------------
# my_cursor.execute("CREATE TABLE users (name VARCHAR(255),\
#                                     email VARCHAR(255),\
#                                     age INTEGER(10), \
#                                     user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
# my_cursor.execute("SHOW TABLES")
# for table in my_cursor:
#     print(table)

# -----------------------------Insert one record table into table-------------------
# sqlStuff = "INSERT INTO users(name, email, age) VALUES(%s, %s, %s)"
# record1 = ("john", "john@gmail.com", 40)
# my_cursor.execute(sqlStuff, record1)
# mydb.commit()

# -----------------------------Insert many records into a Table----------------------
# sqlstuff = "INSERT INTO users(name, email, age) VALUES(%s, %s, %s)"
# records = [
#     ("Tim", "tim@tim.com", 32),
#     ("Mary", "mary@mary.com", 21),
#     ("Steve", "steve@stevemail.com", 57),
#     ("Tina", "tina@somethingelse.com", 29)
# ]

# my_cursor.executemany(sqlstuff, records)
# mydb.commit()

# ------------------------------Select data from Table------------------------------
# my_cursor.execute("SELECT * FROM users")
# result = my_cursor.fetchall()
# print("NAME\tEMAIL\t\tAGE\tID")
# for row in result:
#     print(row[0] + "\t%s" %row[1] + "\t%s" %row[2] + "\t%s" %row[3])

# ------------------------------WHERE(To serach)------------------------------------
# my_cursor.execute("SELECT * FROM users WHERE age > 30")     #WHERE name = 'john'
# result = my_cursor.fetchall()
# for row in result:
#     print(row)

# -----------------------------LIKE(wild cards---------------------------------------
# my_cursor.execute("SELECT * FROM users WHERE name LIKE 'j%' ")  #%i% to find in the middle
# result = my_cursor.fetchall()
# for row in result:
#     print(row)
    
#------------------------------AND and OR clause-------------------------------------
# my_cursor.execute("SELECT * FROM users WHERE name LIKE '%i%' AND age = 29") 
# result = my_cursor.fetchall()
# for row in result:
#     print(row)   

#------------------------------Updating records--------------------------------------
# my_sql = "UPDATE users SET age = 41 WHERE name = 'john'"
# my_cursor.execute(my_sql)
# mydb.commit()

#------------------------------Limit and Ordering------------------------------------
#---LIMIT RESULTS---#
# my_cursor.execute("SELECT * FROM users LIMIT 3 ")  # use "OFFSET 1" if want to starts from second row.
# result = my_cursor.fetchall()
# for row in result:
#     print(row)

#---ORDER---#
# my_cursor.execute("SELECT * FROM users ORDER BY name ASC")   #DESC/ASC
# result = my_cursor.fetchall()
# for row in result:
#     print(row)    

#------------------------------DELETE records-----------------------------------------
# my_sql = "DELETE FROM users WHERE user_id = 5"
# my_cursor.execute(my_sql)
# mydb.commit()

#------------------------------DELETE Table-------------------------------------------
# my_sql = "DROP TABLE IF EXISTS users"
# my_cursor.execute(my_sql)

