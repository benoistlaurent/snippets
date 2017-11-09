
import time

import pandas


# @profile
def main():
    start = time.time()
    df = pandas.read_csv('output_small.csv', header=None)
    elapsed = time.time() - start
    print("Elapsed {:.1f}s".format(elapsed))


if __name__ == '__main__':
    main()

