#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='xmlbuilder',
    version="1.0.1",
    license='LGPL v3',
    description='pythonic way to crate xml/(x)html files',
    author='Nikita Shilnikov / '
           'based on xmlbuilder by Konstantin Danylov aka koder',
    author_email='fg@flashgordon.ru',
    url='https://github.com/latera/xmlbuilder',
    packages=find_packages(),
    test_suite='tests'
)
