~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ofxstatement-santander-es: Santander ES (XLSX) plugin for ofxstatement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This project provides a plugin for `ofxstatement`_ to support bank statements
from Santander ES in XLSX format.

`ofxstatement`_ is a tool to convert proprietary bank statement to OFX format,
suitable for importing to GnuCash or other financial software. This plugin
parses XLSX files downloaded from Santander ES online banking and produces a
common data structure that is then formatted into an OFX file.

.. _ofxstatement: https://github.com/kedder/ofxstatement

Installation
============

It is recommended to use ``pipenv`` or another virtual environment manager.

1.  Clone this repository (if you haven't already):
    ::

      $ git clone <your-repository-url> ofxstatement-santander-es
      $ cd ofxstatement-santander-es

2.  Install the plugin and its dependencies:
    ::

      $ pipenv sync --dev
      $ pipenv shell

    Alternatively, if you are not using pipenv, you can install it using pip:
    ::

      $ pip install .

Usage
=====

After installation, ``ofxstatement`` should be able to see the new plugin.
You can verify this by running:
::

  $ ofxstatement list-plugins

You should see ``SantanderEs`` listed among the available plugins, similar to this:
::

  The following plugins are available:

    SantanderEs      SantanderEs plugin for ofxstatement

To convert your Santander ES XLSX statement file to OFX:
::

  $ ofxstatement convert -t santanderes /path/to/your/santander-statement.xlsx output.ofx

Replace ``/path/to/your/santander-statement.xlsx`` with the actual path to your
downloaded statement file and ``output.ofx`` with your desired output file name.

Plugin Details
==============

This plugin uses the following main components:

*   **Plugin Class**: ``SantanderPlugin`` (located in ``src/ofxstatement_santander_es/plugin.py``)
    This class registers the plugin with ``ofxstatement``. The docstring of this
    class provides the description visible in ``ofxstatement list-plugins``.

*   **Parser Class**: ``SantanderXlsxParser`` (located in ``src/ofxstatement_santander_es/plugin.py``)
    This class handles the parsing of the XLSX file. It reads the transaction
    data from the "Sheet1" of the Excel file, expecting specific column headers
    like "Fecha operación".

The parser expects the XLSX file to have a specific structure, typically starting
data rows after a header row containing "Fecha operación".

Development and Testing
=========================

Setting up development environment
----------------------------------
If you want to contribute or modify the plugin:
::

  $ pipenv sync --dev
  $ pipenv shell

This will download all the dependencies and install them into your virtual
environment.

Testing
-------

Test your code as you would do with any other project. To make sure
ofxstatement is still able to load your plugin, run::

  (.venv)$ ofxstatement list-plugins

You should be able to see your plugin listed. The project also includes a Makefile
for running tests, black, and mypy:
::
  $ make test
  $ make black
  $ make mypy

After you are done
==================

If you've made improvements or fixed bugs, consider contributing back!
If this plugin is useful, you might also want to open an issue on the main
`ofxstatement`_ project to include this plugin in their "known plugin list".
That would hopefully make life of other clients of Santander ES easier.
