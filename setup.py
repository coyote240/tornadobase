from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.txt'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='tornadobase',
      version='0.1.2',
      description='Starter application and handlers for tornado web apps.',
      long_description=long_description,
      author='Adam A.G. Shamblin',
      author_email='adam.shamblin@tutanota.com',
      license='MIT',
      url='https://github.com/coyote240/tornadobase',
      packages=find_packages(exclude=['tests']),
      install_requires=[
          'tornado>=4'
      ],
      tests_require=['nose'])
