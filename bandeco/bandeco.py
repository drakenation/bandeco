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
from .utils import write_plain
from .utils import write_pretty


def run(dt=None):
    """
    Prints the menu, menu date and available dates for a date.

    :param datetime.date dt: The date of the menu t
    :return int: 1 if the
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
    write_pretty("Menu do dia {}\n".format(format_date(current_date)), constants.TERMINAL_GREEN)
    for meal in meals:
        write_plain(meal.format())
    write_pretty("Datas disponíves: {} \n".format(list(map(format_date, available_dates))),
                 constants.TERMINAL_BLUE)
