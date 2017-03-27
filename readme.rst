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

    $ bandeco

Will print the menu for the today or the next available day

.. code-block:: bash

    $ bandeco DD/MM/YYYY

Will print the menu for the specified date (pay attention to the format). It will print an error
message if the specified date doesn't have an associated menu.


Package Usage
-------------

To print the menu of a date, use

.. code-block:: bash

    from bandeco import bandeco
    # Will print the menu for the current or next available date
    bandeco.run()

    from datetime import date
    # Will print the menu for the specified date, if it exists, or return an error message
    bandeco.run(date(...))

Use the scrapper package to get the menu, menu date and available dates:

.. code-block:: bash

    from bandeco import scrapper
    from bandeco.utils import parse_date

    html = scrapper.fetch_data(parse_date('31/12/1999'))
    menu = scrapper.get_meals(html)
    menu_date = scrapper.get_meal_date(html)
    available_date = scrapper.get_available_dates(html)


Documentation
-------------

The code is properly documented with docstrings, and the package is small enough not to need a
guide. At most, you need to know that the import hierarchy is as follows:

.. code-block::

    init
    └── bandeco
        └── scrapper
            └── menu

The rest you can probably figure it out.
