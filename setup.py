import sys, os


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = open('README.rst').read()
requirements = [
    # TODO: put package requirements here
]
test_requirements = [
    'nose'
    # TODO: put package test requirements here
]

setup(
    name='difflib2',
    version='0.1.0',
    description='Difflib2, a sane replacement for Python difflib',
    long_description=readme + '\n\n',
    author='Matthias Bussonnier',
    author_email='bussonniermatthias@gmail.com',
    url='https://github.com/carreau/difflib2',
    packages=[
        'difflib2',
        'tests'
    ],
    package_dir={'difflib2':
                 'difflib2'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='difflib2, diff, levenstein, longuestcommon subsequence, python2, distances',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
