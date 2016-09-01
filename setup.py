#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='nmflib',
    packages=find_packages(include=["nmflib", "nmflib.*",
                                    "nmflib.cluster", "nmflib.cluster.*",
                                    "nmflib.utils", "nmflib.utils.*"],
                           exclude=["tests", "tests.*"]),
)
