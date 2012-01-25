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

#. Install ActivePython from http://www.activestate.com/activepython/downloads
#. Open Windows command prompt, and then::

    pypm install pyreadline
    pypm install ipython
    pypm install pytest
    pypm install flask

#. Test if it works by running IPython from the menu.


Documentation
=============

* Flask web stack: http://flask.pocoo.org/docs/quickstart/
