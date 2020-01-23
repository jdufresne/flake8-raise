=========
Changelog
=========

UNRELEASED
----------

- Include ``CHANGELOG.rst``, ``LICENSE``, ``tox.ini``, and ``tests`` in the
  source distribution.
- Improved "R101 Use bare raise in except handler" for Python 3 nested
  ``except`` handlers.
- Changed version string use ``importlib.metadata``. Requires the dependency on
  importlib-metadata for Python < 3.8.

0.0.4 (2020-01-19)
------------------

- Added "R101 Use bare raise in except handler" rule.
- Restructured test suite to reduce boilerplate.

0.0.3 (2020-01-19)
------------------

- Fixed malformed reStructuredText syntax in README.rst to allow upload to
  PyPI.

0.0.2 (2020-01-19)
------------------

- Fixed malformed reStructuredText syntax in README.rst to allow upload to
  PyPI.

0.0.1 (2020-01-19)
------------------

- Added "R100 raise in except handler without from" rule.
