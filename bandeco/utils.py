"""
Module with helpful functions for general use.
"""

# Core imports
from . import constants
from datetime import date
from sys import stdout
from sys import stderr


def parse_date(date_string):
    """
    Parses a date from a string in DD/MM/YYYY format.

    :param str date_string: A string containing a date in DD/MM/YYYY format.
    :return: A datetime.date parsed with the specified date.
    :raises ValueError: if the input is not in the proper date format.
    """
    try:
        day, month, year = date_string.strip().split('/')
        return date(int(year), int(month), int(day))
    except (ValueError, AttributeError):
        raise ValueError("Input '{}' is not a properly formatted date (must be in DD/MM/YYY format)"
                         "".format(date_string))


def format_date(dt):
    """
    Formats date as a brazilian date (DD/MM/YYYY).

    :param datetime.date dt: The date to be formatted.
    :return str: The formatted date, as a string.
    """
    return dt.strftime('%d/%m/%Y')


def write_plain(string):
    """
    Writes to the standard output stream with a newline at the end.

    :param str string: The string to the printed to the stdout.
    """
    stdout.write(string + '\n')


def write_pretty(string, effect):
    """
    Writes pretty (colored, bold, underlined) text to the standard output stream.

    :param str string: The string to the printed to the stdout.
    :param str effect: The effect to be used. Some effects are already predefiend present in the
                       constant package as TERMINAL_*.
    """
    stdout.write(effect + string + constants.TERMINAL_END)


def write_error(string):
    """
    Writes to the standard error stream with a newline at the end.

    :param str string: The string to the printed to the stderr.
    """
    stderr.write(string + '\n')
