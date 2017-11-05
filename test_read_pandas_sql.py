

import sqlite3

import pandas


database = 'foo.db'     # database file name
database_name = 'data'  # table name inside the sql file

con = sqlite3.connect(database)

idlist = ['0012142', '0123123']

query = 'select * from data where "0" in {}'.format(tuple(idlist))

df = pandas.read_sql(query, con)