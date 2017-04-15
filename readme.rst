Bandeco: what's today's meal?
=============================

Installation
------------


This package is not available on pypi. To install the CLI, cd into the package directory and install
it with:

.. code-block:: bash

    $ python setup.py install


CLI Usage
---------

.. code-block:: bash

    $ bandeco -d [DD/MM/YYYY|amanha]

Will print the menu for the specified date (pay attention to the format) or tomorrow, respectively.
It will print an error message if the specified date doesn't have an associated menu.

.. code-block:: bash

    $ bandeco -m [almoco|jantar|todas]

Will print the specified meal for the next date.

You can combine the -m and -d options to fetch anspecific meal of an specific date.

    $ bandeco -m [almoco|jantar|todas]  -d [DD/MM/YYYY|amanha]

The CLI also has a default behavior:

.. code-block:: bash

    $ bandeco

Will print the menu for a single meal of today's or the next available day's menu.
If today's menu, then it will choose lunch or dinner based on the current time (before or after 14h).
It not today's menu, it will always print the lunch menu.


Package Usage
-------------

To get the menu as a string, use

.. code-block:: python

    # Will print the menu for the current or next available date
    from bandeco import bandeco
    bandeco.run(input_date=None, input_meal=None)

The possible values for *input_date* and *input_meal* are the same as the CLI version.
The resulting string is formatted for displaying in a bash terminal. If you desire to remove this formatting,
use the remove_terminal_formatting() function from the utils package.

You can use the scrapper package to get the menu, menu date and available dates as objects, instead of a string:

.. code-block:: bash

    from bandeco import scrapper
    from bandeco.utils import parse_date

    html = scrapper.fetch_data(parse_date('31/12/1999'))
    menu = scrapper.get_meals(html)
    menu_date = scrapper.get_meal_date(html)
    available_dates = scrapper.get_available_dates(html)


Documentation
-------------

The code is properly documented with docstrings, and the package is small enough not to need a
guide. At most, you need to know that the call hierarchy is as follows:

.. code-block::

    init
    └── bandeco
        └── scrapper
            └── menu

The rest you can probably figure it out.
