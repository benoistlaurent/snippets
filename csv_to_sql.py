

import sqlite3

import pandas


database = 'foo.db'     # database file name
database_name = 'data'  # table name inside the sql file

con = sqlite3.connect(database)

filename_fmt = '/path/to/file_{}.csv'


for i in range(6):
    filename = filename_fmt.format(i)
    df = pandas.read_csv(filename, header=None)

    # If this is the first file, replace the existing database with the new one.
    if i == 0:
        df.to_sql(database_name, con, if_exists='replace', index=False)
    else:
        df.to_sql(database_name, con, if_exists='append', index=False)


