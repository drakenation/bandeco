"""
Module that contains the Menu model class.
"""

# Core imports
from pprint import pformat


class Menu(object):
    """Class that models a Food Menu."""

    # Allowed attributes for this class
    attributes = ('meal', 'rice', 'maindish', 'garnish', 'salad', 'dessert', 'juice', 'notes')
    # Allowed values for the attribute Menu.meal
    available_meals = ('lunch', 'lunch-vegetarian', 'dinner', 'dinner-vegetarian', None)
    # Portuguese translations for the allowed values for the Menu.meal attribute
    meal_translations = {
        'lunch': 'Almoço',
        'lunch-vegetarian': 'Almoço Vegetariano',
        'dinner': 'Jantar',
        'dinner-vegetarian': 'Jantar Vegetariano',
    }

    def __init__(self, meal=None, rice=None, maindish=None, garnish=None, salad=None,
                 dessert=None, juice=None, notes=None):
        """Instantiates a new Menu."""
        self.meal = meal
        self.rice = rice
        self.maindish = maindish
        self.garnish = garnish
        self.salad = salad
        self.dessert = dessert
        self.juice = juice
        self.notes = notes

    def __str__(self):
        """Returns the object's attributes in a dict-like format."""
        return pformat((vars(self)))

    def __setattr__(self, key, value):
        """Allow setting only valid attributes for this class."""
        if key not in Menu.attributes:
            raise AttributeError("'{}' is not a valid attribute".format(key))
        if key == 'meal' and value not in Menu.available_meals:
            raise AttributeError("'{}' is not a valid meal identifier - options are {}.".format(
                value, Menu.available_meals))
        super(Menu, self).__setattr__(key, value)

    def __getattr__(self, key):
        """Allow getting only valid attributes for this class."""
        if key not in Menu.attributes:
            raise AttributeError("'{}' is not a valid attribute".format(key))
        super(Menu, self).__getattribute__(key)

    def format(self):
        """Formats the contents of the Menu in a pretty, easy-to-read way."""
        values = vars(self)
        values['garnish'] = self.garnish if self.garnish else 'Nenhuma'
        values['meal'] = Menu.meal_translations[self.meal]
        values['border'] = '=' * len('Refeição: {}'.format(self.meal))
        return "\n".join(["{border}",
                          "Refeição: {meal}",
                          "{border}",
                          "  * Arroz: {rice}",
                          "  * Prato principal: {maindish}",
                          "  * Guarnição: {garnish}",
                          "  * Salada: {salad}",
                          "  * Sobremesa: {dessert}",
                          "  * Suco: {juice}",
                          "  * Observações: {notes}"]).format(**values) + "\n"
