from setuptools import setup

setup(name='tornadobase',
      version='0.1',
      description='Starter application and handlers for tornado web apps.',
      author='Adam A.G. Shamblin',
      author_email='adam.shamblin@tutanota.com',
      license='MIT',
      url='https://github.com/coyote240/tornadobase',
      install_requires=[
          'tornado>=4'
      ],
      tests_require=['nose'])
