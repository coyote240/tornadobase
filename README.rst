tornadobase
===========

.. _travis: https://travis-ci.org/coyote240/tornadobase.svg

A base application and boilerplate for the Tornado web server.

Installation
------------

To include tornadobase in your application install using pip:

    pip install tornadobase

Run the tests
-------------

    pip install nose
    nosetests

Use
---

tornadobase provides basic Application and Handler classes that wrap up some of
the boilerplate you'll typically need when using the Tornado web server.  To get
a simple site running, create a file called ``application.py``:

.. code-block:: python

    from tornadobase.handlers import BaseHandler
    from tornadobase.application import Application

    class IndexHandler(BaseHandler):

        def get(self):
            self.write('Hello, World!')


    class MyApp(Application):

        def init_handlers(self):

            self.handlers = [
                (r'/', IndexHandler)
            ]

Then start the web server:

    python application.py
