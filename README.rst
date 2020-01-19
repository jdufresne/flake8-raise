============
flake8-raise
============

A `flake8 <https://flake8.readthedocs.io/>`_ plugin that finds improvements for
raise statements.

Installation
------------

Install using ``pip``:

.. code-block:: sh

    $ pip install flake8-raise

When installed, the plugin will automatically be used by ``flake8``. To check
it is installed correctly, run ``flake8 --version`` and look in the list of
installed plugins:

.. code-block:: sh

    $ flake8 --version
    3.7.9 (flake8-raise: 0.0.3, mccabe: 0.6.1, pycodestyle: 2.5.0, pyflakes: 2.1.1) CPython 3.8.1 on Linux

Rules
-----

==== ====
Code Rule
==== ====
R100 raise in except handler without from.
==== ====

Examples
--------

The following example:

.. code-block:: py

    try:
        foo["bar"]
    except KeyError:
        raise MyException

Will result in the flake8 error:

.. code-block:: text

    R100 raise in except handler without from.

To fix, change the code to:

.. code-block:: py

    try:
        foo['bar']
    except KeyError as e:
        raise MyException from e
