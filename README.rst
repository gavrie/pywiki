Welcome to the Python course at IBM.

Installation
============

We will be using Python 2.7 along with these tools:

* The `IPython <http://ipython.org/>`_ interactive environment
* The `pytest <http://pytest.org/>`_ unit testing framework
* The `Flask <http://flask.pocoo.org/>`_ Web micro-framework

Ubuntu Users
------------

#. Install the Python prerequisites::

    sudo apt-get install python-pip 
    sudo pip install ipython pytest flask

#. Test if it works::

    ipython

Windows Users
-------------

The easiest method is to install ActivePython with PyPM.

*Note: Even if you have a 64-bit version of Windows, please install the 32-bit version of ActivePython. 
The 64-bit version is known to be problematic.*

#. Install ActivePython from http://www.activestate.com/activepython/downloads
#. Open Windows command prompt, and then::

    pypm install pyreadline
    pypm install ipython
    pypm install pytest
    pypm install flask

#. Test if it works by running IPython from the menu.


Documentation
=============

* Python Documentation: http://docs.python.org/
* Python Package Index (PyPI): http://pypi.python.org/pypi
* Python static analysis tools: `pyflakes <http://pypi.python.org/pypi/pyflakes>`_, pylint, pychecker
* Flask web micro-framework: http://flask.pocoo.org/docs/quickstart/


Downloading the Code
====================

(will be updated as the course progresses)

#. Stage 1: http://github.com/gavrie/pywiki/zipball/stage1_pages
#. Stage 2: http://github.com/gavrie/pywiki/zipball/stage2_render
#. Stage 3: http://github.com/gavrie/pywiki/zipball/stage3_web (to run: python web.py)
#. Stage 4: http://github.com/gavrie/pywiki/zipball/stage4_edit
#. Stage 5: http://github.com/gavrie/pywiki/zipball/stage5_memoize
#. Stage 6: http://github.com/gavrie/pywiki/zipball/stage6_oop
#. Stage 7: http://github.com/gavrie/pywiki/zipball/stage7_iter
#. Stage 8: http://github.com/gavrie/pywiki/zipball/stage8_contents
#. Stage 9: http://github.com/gavrie/pywiki/zipball/stage9_context
