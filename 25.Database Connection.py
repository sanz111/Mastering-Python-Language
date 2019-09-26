# importing the module
import MySQLdb

# opening a database connection
conn = MySQLdb.connect("localhost", "testprog", "stud", "PYDB")

# define a cursor object
cursor = conn.cursor

# drop table if exists
cursor.execute("IF STUDENT TABLE EXISTS DROP IT")

# query
sql = "CREATE TABLE STUDENT (NAME CHAR(30) NOT NULL, CLASS CHAR(5), AGE INT, GENDER CHAR(8), MARKS INT"

# execute query
cursor.execute(sql)

# close object
cursor.close()

# close connection
conn.close()
