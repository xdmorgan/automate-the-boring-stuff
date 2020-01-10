# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='mymodule',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Dan Morgan',
    author_email='spamdanny@icloud.com',
    url='https://github.com/xdmorgan/automate-the-boring-stuff',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
