#!/usr/bin/env python

from setuptools import setup, find_packages
import os

here = os.path.dirname(os.path.dirname(__file__))
exec(open(os.path.join(here, 'documents/version.py')).read())

requirements = []

setup(
    name='documents',
    version=__version__,
    description='A database-like access to data without all the fuss of a database',
    author='Jason R. Jones',
    author_email='slightlynybbled@gmail.com',
    url='https://github.com/slightlynybbled/documents',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English'
    ],
    keywords='database json'
)

