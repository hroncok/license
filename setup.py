#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='license',
    version='0.1.dev1',
    description='Library that encapsulates free software licenses',
    long_description=''.join(open('README.rst').readlines()),
    keywords='license',
    author='Miro Hrončok',
    author_email='miro@hroncok.cz',
    license='MIT',
    packages=[p for p in find_packages() if p != 'test'],
    package_data={'license': ['templates/*']},
    install_requires=['jinja2'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        ]
)
