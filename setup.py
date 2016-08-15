# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="linked-list",
    description="Implementation of a linked list",
    version='0.1.0',
    author="David Smith, Jeff Torres",
    author_email="dbsmith.dbs83@gmail.com, jeffrey.n.torres@gmail.com",
    license='MIT',
    py_modules=['linked-list'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'tox']},
)
