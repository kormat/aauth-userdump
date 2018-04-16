#!/usr/bin/python3

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
    name='aauth-userdump',
    version='0.0.1',
    description='Simple exporter of chars and their groups',
    url='https://github.com/kormat/aauth-userdump',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=3',
)
