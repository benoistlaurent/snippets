
"""projectdir.date - Date and time utilities.

From pykup: https://raw.githubusercontent.com/benoistlaurent/pykup
"""


import datetime


def now(fmt):
    """Return the date as a string in the format `fmt`.

    This is a useless image:

    .. figure:: images/sweat.jpg
       :align: center

       And this is a useless legend

    Args:
        fmt (str): date string format compatible with `datetime.strftime`.

    Returns:
        str: date as a string.
    """
    return datetime.datetime.today().strftime(fmt)


def isvaliddate(date, fmt):
    """Return True if `date` is a string date in the valid format.

    Args:
        date (str): string representing a date.
        fmt (str): date string format compatible with `datetime.strftime`.

    Returns:
        bool: True if date can be converted to datetime.date using `fmt`
    """
    try:
        datetime.datetime.strptime(date, fmt)
        return True
    except ValueError:
        return False