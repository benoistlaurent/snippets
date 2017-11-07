
"""Create a csv file in which each row has 720 columns."""

import random


def create_csv_file(path):
    """Create a single csv file with 100k rows and 720 columns."""
    nrows = 100000
    ncols = 720

    with open(path, 'wt') as f:
        for i in range(nrows):
            rowid = '{:07d}'.format(i + 1)
            cols = ['{:.18e}'.format(random.random()) for i in range(ncols)]
            print("{},{}".format(rowid, ','.join(cols)), file=f)
            print("\r{}: progress: {:.0%}".format(path, (i + 1) / nrows), end='', flush=True)
        print()


def main():
    for i in range(6):
        path = 'output_{}.csv'.format(i + 1)
        create_csv_file(path)
    


if __name__ == '__main__':
    main()
