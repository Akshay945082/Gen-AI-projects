import sqlite3
connection=sqlite3.connect("student.db")
cursor=connection.cursor()
# Table creation
table_info = """
create table STUDENT (NAME VARCHAR (25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT(5))
"""
cursor.execute(table_info)

# Insert records
cursor.execute("INSERT INTO STUDENT VALUES ('krish', 'Data science', 'A', 90)")
cursor.execute("INSERT INTO STUDENT VALUES ('John', 'Data science', 'B', 100)")
cursor.execute("INSERT INTO STUDENT VALUES ('Mukesh', 'Data science', 'A', 86)")
cursor.execute("INSERT INTO STUDENT VALUES ('Jacob', 'Data science', 'A', 50)")
cursor.execute("INSERT INTO STUDENT VALUES ('Dipesh', 'Data science', 'A', 35)")

# Commit changes to the database
connection.commit()

# Display all the records
print("The inserted records are:")
cursor.execute("SELECT * FROM STUDENT")
data = cursor.fetchall()

for row in data:
    print(row)




