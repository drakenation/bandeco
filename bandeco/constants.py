"""
Module with constant values for the whole application.
"""

# The URL where the menu is fetched from
BANDECO_MENU_URL = 'http://catedral.prefeitura.unicamp.br/cardapio.php'

# Timezone for the bandeco restaurant used to decide automatically if dinner should be shown instead
BANDECO_TIMEZONE = 'America/Sao_Paulo'

# The time when lunch is no longer served - used to decide automatically if dinner should be shown
# instead
LUNCH_END_HOUR = 14

# Valid values for the meal input parameter/argument
MEAL_LUNCH = 'almoco'
MEAL_DINNER = 'jantar'
MEAL_ALL = 'todas'
MEAL_CHOICES = (MEAL_LUNCH, MEAL_DINNER, MEAL_ALL)

# Valid values for the date input parameter/argument
DATE_TOMORROW = 'amanha'

# Code for formatting the output string in a bash terminal
TERMINAL_END = '\033[0m'
TERMINAL_BLUE = '\033[94m'
TERMINAL_GREEN = '\033[92m'
TERMINAL_YELLOW = '\033[93m'
TERMINAL_RED = '\033[91m'
