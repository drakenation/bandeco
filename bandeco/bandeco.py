"""
Contains the main function of the package.
"""

# Core imports
from argparse import ArgumentParser
from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta
# Third party imports
from pytz import timezone
# Project imports
from . import constants
from . import scrapper
from .utils import format_date
from .utils import parse_date
from .utils import format_for_terminal
from .utils import write_plain


def _parse_args(input_date, input_meal):
    """
    Parses the date and meal for a menu, both from CLI and function calls.

    This method will only return a non-None value if that's what the user specified, since more
    information then available at this point is necessary to make an automatic decision (namely,
    the menu date), in which case it returns None so that whichever function called it can make the
    decision by itself.

    :param str|None input_date: A string with a date in format DD/MM/YYYY or None.
    :param str|None input_meal: A string with one of the following values: 'almoco', 'jantar' or
           'todas' or None.
    :return (datetime.date|None, str|None): A tuple containing the values for the date and meal.
            Can return None, then the application must then choose which meal and date to use.
    :raises ValueError: if the input_meal value isn't valid.
    """
    parser = ArgumentParser()
    parser.add_argument('-d', '--date', type=str)
    parser.add_argument('-m', '--meal', type=str)
    args = parser.parse_args()
    # Allows getting the args from either CLI or as the function parameters
    query_date = args.date or input_date
    query_meal = args.meal or input_meal
    # Validate and sanitize the meal
    if query_meal and query_meal not in constants.MEAL_CHOICES:
        raise ValueError("Refeições suportadas são apenas 'almoço', 'jantar' e 'todas'.")
    # Validate and sanitize the date
    if query_date == constants.DATE_TOMORROW:
        query_date = date.today() + timedelta(days=1)
    else:
        try:
            query_date = parse_date(args.date if args.date else input_date or None)
        except ValueError:
            query_date = None
    return query_date, query_meal


def run(input_date=None, input_meal=None):
    """
    Fetches the menu, menu date and available dates for a date and returns them as a string.

    :param str input_date: The date of the menu to be fetched.
    :param str input_meal: The meal to be fetched on the menu.
    :return int: The error code of the execution (0 means no error)
    """
    query_date, query_meal = _parse_args(input_date, input_meal)
    # Get the data and instantiate the required classes
    html = scrapper.fetch_data(query_date)
    meal_date = scrapper.get_meal_date(html)
    available_dates = scrapper.get_available_dates(html)
    meals = scrapper.get_meals(html)
    result = ""
    result += format_for_terminal("Cardápio do dia {}\n".format(format_date(meal_date)),
                                  constants.TERMINAL_GREEN)
    # Automatically decide which meal should be shown if none was specified
    if not query_meal:
        if meal_date != date.today():
            query_meal = constants.MEAL_LUNCH
        elif (datetime.now(timezone(constants.BANDECO_TIMEZONE)).time() <
                  time(hour=constants.LUNCH_END_HOUR)):
            query_meal = constants.MEAL_LUNCH
        else:
            query_meal = constants.MEAL_DINNER
    # Formats the meal menu
    if query_meal == constants.MEAL_LUNCH:
        result += meals[0].combine(meals[1]).format()
    elif query_meal == constants.MEAL_DINNER:
        result += meals[2].combine(meals[3]).format()
    else:
        for meal in meals:
            result += meal.format()
    # Show other dates available for fetching
    result += format_for_terminal(
        "Datas disponíves: {}".format(", ".join(list(map(format_date, available_dates)))),
        constants.TERMINAL_BLUE)
    # Shows a warning if the menu is not from today
    today = date.today()
    if not query_date and meal_date != today:
        result += format_for_terminal("\nAviso: este cardápio não é de hoje, mas para daqui {} dias"
                                      .format((meal_date - today).days), constants.TERMINAL_RED)
    return result


def run_and_print(dt=None):
    """
    Fetches the menu, menu date and available dates for a date and prints them to the stdout.

    :param datetime.date dt: The date of the menu to be fetched.
    """
    write_plain(run(dt))
