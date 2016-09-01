#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='nmflib',
    packages=find_packages(include=["nmflib", "nmflib.*"],
                           exclude=["tests", "tests.*"]),
)
