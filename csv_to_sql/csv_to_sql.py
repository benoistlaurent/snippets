

import sqlite3
import time

import pandas


START = time.time()


def main():
    db = 'foo.db'     # database file name
    db_name = 'data'  # table name inside the sql file

    con = sqlite3.connect(db)  # connector to the database

    filename_fmt = 'output_{}.csv'
    for i in range(6):
        start = time.time()
        csv = filename_fmt.format(i + 1)
        if_exists = 'replace' if i == 0 else 'append'
        df = pandas.read_csv(csv, header=None)
        df.to_sql(db_name, con, if_exists=if_exists, index=False, chunksize=4096)
        print("-- File {} - done ({:.1f}s)".format(i + 1, time.time() - start), flush=True)

    print("Elapsed time: {:.1f}m".format((time.time() - START) / 60))


if __name__ == '__main__':
    main()
