#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='codenamer',
    version='0.0.1',
    description='Whimsical code name generator',
    author='Sean Caulfield',
    author_email='sean@yak.net',
    url='https://meatspin.fr/',
    packages=find_packages(),
    scripts=['codename'],
    include_package_data=True,
    zip_safe=False,
)
