# import sqlite3
import pscyopg2

# def create_table():
#     conn = sqlite3.connect("lite.db")
#     cur = conn.cursor()
#     cur.execute("CREATE TABLE store (item TEXT, quantity INTEGER, price REAL)")
#     conn.commit()
#     conn.close()

def create_table():
    conn = psycopg2.connect("dbname='TestDB' user='postgres' pass='yD4qnMXp7xYvx7cUJ1a5' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

# def insert(item,quantity,price):
#     conn = sqlite3.connect("lite.db")
#     cur = conn.cursor()
#     cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
#     conn.commit()
#     conn.close()

# # insert("Water Glass",10,5)

# def view():
#     conn = sqlite3.connect("lite.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM store")
#     rows = cur.fetchall()
#     conn.close()
#     return rows

# def delete(item):
#     conn = sqlite3.connect("lite.db")
#     cur = conn.cursor()
#     cur.execute("DELETE FROM store WHERE item=?",(item,))
#     conn.commit()
#     conn.close()

# # delete("Water Glass")

# def update(quantity,price,item):
#     conn = sqlite3.connect("lite.db")
#     cur = conn.cursor()
#     cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))
#     conn.commit()
#     conn.close()

# # update(15,6.0,'Water Glass')

# print(view())