"""
Module that contains the Menu model class.
"""

# Core imports
from pprint import pformat


class Menu(object):
    """Class that models a Food Menu."""

    # Allowed attributes for this class
    attributes = ('meal', 'meal_combination', 'rice', 'maindish', 'garnish', 'salad', 'dessert',
                  'juice', 'notes')
    # Allowed values for the attribute Menu.meal
    MEAL_LUNCH = 'lunch'
    MEAL_LUNCH_VEGGIE = 'lunch-vegetarian'
    MEAL_DINNER = 'dinner'
    MEAL_DINNER_VEGGIE = 'dinner-vegetarian'
    available_meals = (MEAL_LUNCH, MEAL_LUNCH_VEGGIE, MEAL_DINNER, MEAL_DINNER_VEGGIE, None)
    # Portuguese translations for the allowed values for the Menu.meal attribute
    meal_translations = {
        MEAL_LUNCH: 'Almoço',
        MEAL_LUNCH_VEGGIE: 'Almoço Vegetariano',
        MEAL_DINNER: 'Jantar',
        MEAL_DINNER_VEGGIE: 'Jantar Vegetariano',
    }

    def __init__(self, meal=None, rice=None, maindish=None, garnish=None, salad=None,
                 dessert=None, juice=None, notes=None):
        """Instantiates a new Menu."""
        self.meal = meal
        self.meal_combination = None
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
        if key in ('meal', 'meal_combination') and value not in Menu.available_meals:
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
        if self.meal_combination:
            values['meal'] = '{} + {}'.format(
                Menu.meal_translations.get(self.meal, 'Desconhecido'),
                Menu.meal_translations.get(self.meal_combination, 'Desconhecido'),
            )
        else:
            values['meal'] = Menu.meal_translations.get(self.meal, 'Desconhecido')
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

    @staticmethod
    def _combine_attribute(attribute, other_attribute, separator=', '):
        """
        Combines two attributes in a Meal.

        The values are only combined if the attributes are different, don't contain each other
        and other_attribute is not None.
        If the values are not combined, the first attribute is returned.

        :param str attribute: one attribute to be combined.
        :param str other_attribute: another attribute to be combined.
        :param str separator: a string to separate the attributes in the resulting string.
        :return str: The attributes combined in a string, separated by a separator, or the original
                attribute.
        """
        if (other_attribute and attribute != other_attribute and
           attribute not in other_attribute and other_attribute not in attribute):
            return '{}{}{}'.format(attribute, separator, other_attribute)
        return attribute

    def combine(self, menu):
        """
        Combines the attributes of two Menus. The result is a new Menu, originals are not modified.

        :param bandeco.menu.Menu menu: the menu to be combined with the instance.
        :return bandeco.menu.Menu: A new Menu with combined attributes.
        """
        if type(self) != type(menu):
            raise TypeError("Só é possível combinar um cardápio com outro cardápio")
        combined = Menu()
        combined.meal = self.meal
        combined.meal_combination = menu.meal
        combined.rice = Menu._combine_attribute(self.rice, menu.rice)
        combined.maindish = Menu._combine_attribute(self.maindish, menu.maindish)
        combined.garnish = Menu._combine_attribute(self.garnish, menu.garnish)
        combined.salad = Menu._combine_attribute(self.salad, menu.salad)
        combined.dessert = Menu._combine_attribute(self.dessert, menu.dessert)
        combined.juice = Menu._combine_attribute(self.juice, menu.juice)
        combined.notes = Menu._combine_attribute(self.notes, menu.notes, ' ')
        return combined
