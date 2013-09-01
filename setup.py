from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='difflib2',
      version=version,
      description="A surpriseless alternative to difflib",
      long_description="""\
If you prefer a difflib that is developper friendly instead of visualy pleasant for the end user and are disapointed by difflib, difflib2 is for you""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='diff, levenstein, longuestcommon subsequence, python2, distances',
      author='Bussonnier Matthias',
      author_email='bussonniermatthias@gmail.com',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
