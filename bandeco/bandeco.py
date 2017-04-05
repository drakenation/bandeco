"""
Contains the main function of the package.
"""

# Core imports
from argparse import ArgumentParser
# Project imports
from . import constants
from . import scrapper
from .utils import format_date
from .utils import parse_date
from .utils import format_for_terminal
from .utils import write_plain


def run(dt=None):
    """
    Fetches the menu, menu date and available dates for a date and returns them as a string.

    :param datetime.date dt: The date of the menu to be fetched.
    :return int: The error code of the execution (0 means no error)
    """
    parser = ArgumentParser()
    parser.add_argument('date', type=str, nargs='*')
    args = parser.parse_args()
    try:
        date = parse_date(args.date[0] if len(args.date) > 0 else dt or None)
    except ValueError:
        date = None
    try:
        html = scrapper.fetch_data(date)
    except ValueError as exception:
        return str(exception)
    current_date = scrapper.get_meal_date(html)
    available_dates = scrapper.get_available_dates(html)
    meals = scrapper.get_meals(html)
    result = ""
    result += format_for_terminal("Menu do dia {}\n".format(format_date(current_date)),
                                  constants.TERMINAL_GREEN)
    for meal in meals:
        result += meal.format()
    result += format_for_terminal(
        "Datas disponíves: {}".format(list(map(format_date, available_dates))),
        constants.TERMINAL_BLUE)
    return result


def run_and_print(dt=None):
    """
    Fetches the menu, menu date and available dates for a date and prints them to the stdout.

    :param datetime.date dt: The date of the menu to be fetched.
    :return int: The error code of the execution (0 means no error)
    """
    write_plain(run(dt))
