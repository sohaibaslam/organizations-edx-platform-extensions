#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='organizations-edx-platform-extensions',
    version='2.0.0',
    description='Organization management extension for edX platform',
    long_description=open('README.rst').read(),
    author='edX',
    url='https://github.com/edx-solutions/organizations-edx-platform-extensions.git',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django>=1.11,<1.12",
    ],
)
