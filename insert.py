import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("INSERT INTO COMPANY1(ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES (1,'EMOBILIS',7,'WESTLANDS',25000.00)");
conn.execute("INSERT INTO COMPANY1(ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES (2,'safaricom',7,'WESTLANDS',26000.00)");
conn.execute("INSERT INTO COMPANY1(ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES (3,'EMOBILIS', 7,'WESTLANDS',28000.00)");
conn.execute("INSERT INTO COMPANY1(ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES (4,'EMOBILIS',7,'WESTLANDS',26000.00)");
conn.execute("INSERT INTO COMPANY1(ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES (5,'EMOBILIS',7,'WESTLANDS',23000.00)");

conn.commit()
print("Records created successfully")
conn.close()