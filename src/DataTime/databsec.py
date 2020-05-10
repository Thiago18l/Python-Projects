import psycopg2

host = "localhost"
dbname = "python"
user = "thiago"
password = "181297"

connection_string = "host={} user={} dbname={} password={}".format(host, user, dbname, password)
connection = psycopg2.connect(connection_string)

cursor = connection.cursor()

# Fetch all rows of table

cursor.execute("UPDATE inventory SET quantity = %s WHERE name = %s;", (200, "banana"))
print("Updated 1 row of data")
connection.commit()
cursor.close()
connection.close()