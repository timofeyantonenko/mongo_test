import pyodbc as pyodbc
from meza import io
import pypyodbc


# import pandas_access as mdb
# for tbl in mdb.list_tables("Борей.mdb", encoding="utf-8"):
#     print(tbl)
# df = mdb.read_table("Борей.mdb", "Заказы")
# for row in df:
#     print(row)



pypyodbc.lowercase = False
# conn = pypyodbc.connect(
#     '{Microsoft Access Driver (*.mdb)}' +
#     r"Dbq=Борей.mdb;")

import csv, pyodbc

# set up some constants
MDB = 'Борей.mdb'; DRV = '{Microsoft Access Driver (*.mdb)}'; PWD = 'pw'

# connect to db
con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(DRV,MDB,PWD))
cur = con.cursor()

# run a query and get the results
SQL = 'SELECT * FROM Заказы;' # your query goes here
rows = cur.execute(SQL).fetchall()
cur.close()
con.close()

# you could change the mode from 'w' to 'a' (append) for any subsequent queries
with open('mytable.csv', 'wb') as fou:
    csv_writer = csv.writer(fou) # default field-delimiter is ","
    csv_writer.writerows(rows)

# records = io.read('Борей.mdb') # only file path, no file objects
# print(dir(records))
# for record in records:
#     print(record)
# print(next(records))