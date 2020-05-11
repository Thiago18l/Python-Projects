import psycopg2

host = "localhost"
dbname = "python"
user = "thiago"
password = "181297"

conn_string = "host={} user={} dbname={} password={}".format(
    host, user, dbname, password)
connection = psycopg2.connect(conn_string)

cursor = connection.cursor()

cursor.execute("SELECT * FROM inventory")
rows = cursor.fetchall()

# Printando dados
for row in rows:
    print("Dados = ({}, {}, {})".format(str(row[0]), str(row[1]), str(row[2])))

connection.commit()
cursor.close()
connection.close()