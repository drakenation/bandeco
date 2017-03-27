"""
Fetches food menu information from the restaurant page.
"""

# Third party libs
from bs4 import BeautifulSoup
from requests import get as request_get
# Project imports
from .constants import BANDECO_MENU_URL
from .menu import Menu
from .utils import parse_date


def fetch_data(dt=None):
    """
    Fetches the HTML data from the restaurant.

    :param datetime.date dt: The date of the menu to be fetched. If blank, will use today or the
                             next weekday (this is the behaviour of the scrapped website).
    :return bs4.BeautifulSoup: The parsed HTML.
    :raises ValueError: if the response doesn't contain the menu.
    """
    url = BANDECO_MENU_URL if not dt else '{}?d={}'.format(BANDECO_MENU_URL, str(dt))
    response = request_get(url)
    if len(response.text) < 1000 or 'Não existe cardápio cadastrado no momento' in response.text:
        raise ValueError("Erro: cardápio inexistente!")
    return BeautifulSoup(response.text, 'html.parser')


def get_meals(html):
    """
    Parses the HTML and get the menus for the chosen date.

    :param bs4.BeautifulSoup html: The root of the HTML, already parsed by BeautifulSoup.
    :return list<bandeco.menu.Menu>: A list of meals, filled with their current menu.
    """
    meals = [
        Menu('lunch'),
        Menu('lunch-vegetarian'),
        Menu('dinner'),
        Menu('dinner-vegetarian'),
    ]
    result = html.find_all('table', class_='fundo_cardapio')
    menu_number = 0
    for table in result:
        meal = meals[menu_number]
        for table_row in table.children:
            try:
                row = str(table_row.td)
                if 'ARROZ' in row:
                    meal.rice = _get_menu_item(table_row)
                elif 'PRATO PRINCIPAL' in row:
                    meal.maindish = str(table_row.td.contents[-1].contents[0]).strip().title()
                elif 'SALADA' in row:
                    meal.salad = _get_menu_item(table_row)
                elif 'SOBREMESA' in row:
                    meal.dessert = _get_menu_item(table_row)
                elif 'SUCO' in row:
                    meal.juice = _get_menu_item(table_row)
                elif 'Observações' in row:
                    meal.notes = str(table_row.td.contents[0]).split(
                        '<br>')[-1].replace('</br>', '').strip().title()
                else:
                    garnish = str(table_row.td.contents[-1]).strip().title()
                    meal.garnish = garnish if meal.garnish is None else (
                        meal.garnish + ', ' + garnish)
            # Ignore rows that don't have the attributes we want
            except AttributeError:
                pass
        menu_number += 1
    return meals


def get_meal_date(html):
    """
    Gets the date of the current menu from the html.

    :param bs4.BeautifulSoup html: The root of the HTML, already parsed by BeautifulSoup.
    :return datetime.date: Date of the scrapped menu.
    """
    menu_date = html.find('p', class_='titulo')
    # Use some splits instead of regex for simplicity - hopefully they wont change the format soon!
    return parse_date(menu_date.contents[0].split(' ')[5])


def get_available_dates(html):
    """
     Gets which dates already have a menu available.

    :param bs4.BeautifulSoup html: The root of the HTML, already parsed by BeautifulSoup.
    :return list<datetime.date>: A list with the dates that already have a menu available.
    """
    week_dates = []
    dates_table = html.find('table', class_='dias_semana')
    for row in dates_table.children:
        try:
            week_dates.append(parse_date(row.td.a.contents[0]))
        # Ignore items that do not have the attributes we desire
        except AttributeError:
            pass
    return week_dates


def _get_menu_item(tag):
    """
    Convenience function to extract the menu item as a string from the HTML.

    :param bs4.element.Tag tag: the tag that contains the relevant text.
    :return str: The menu item, as a string.
    """
    return str(tag.td.contents[-1]).strip().title()
