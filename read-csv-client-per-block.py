
import io

import pandas


def read_csv_custom(path, clients_per_block=100):
    """Read a client raw CSV.

    Read by blocks of clients so that a client cannot be split across two
    blocks.

    Args:
        path (str): path to input CSV file
        client_per_block (int): number of clients per block.
            The last block can contain less clients.

    Yields:
        pandas.DataFrame
    """
    with open(path, 'rt') as f:
        headers = next(f).rstrip().split(',')
        block = ''
        nclientids_in_block = 0
        last_clientid = None
        for line in f:
            clientid = line.split(',')[0]
            if clientid != last_clientid:
                if last_clientid:
                    nclientids_in_block += 1
                if nclientids_in_block == clients_per_block:
                    yield pandas.read_csv(io.StringIO(block), header=None, names=headers)
                    block = ''
                    nclientids_in_block = 0
                last_clientid = clientid
            block += line
        yield pandas.read_csv(io.StringIO(block), header=None, names=headers)


def get_data_by_month(df):
    """Arange the data so that they are ordered by month.

    Assumes each location has 12 rows.

    Returns:
        list[pandas.DataFrame]: a DataFrame for each month.
    """
    return [df[i::12] for i in range(12)]


def main():
    csv = 'output.csv'
    blocks = read_csv_custom(csv, clients_per_block=16000)
    for data in blocks:
        dat_mois = get_data_by_month(data)



if __name__ == "__main__":
    main()
