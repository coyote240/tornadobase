# Base Application for Tornado Web [![Build Status](https://travis-ci.org/coyote240/tornadobase.svg?branch=master)](https://travis-ci.org/coyote240/tornadobase)

## Installation

To include tornadobase in your application, add a dependency link to your
setup.py:

```python
dependency_links=[
    'git+git://github.com/coyoto240/tornadobase/tarball/master#egg=tornadobase'
]
```

## Run the tests

    pip install nose
    nosetests

## Use

```python
from tornadobase.application import Application

class MyApp(Application):

    def init_settings(self):

        settings = {
            'debug': True
        }

        return settings
```
