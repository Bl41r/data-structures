# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="deque",
    description="Implementation of a deque",
    version='0.1.0',
    author="David Smith, Jeff Torres",
    author_email="dbsmith.dbs83@gmail.com, jeffrey.n.torres@gmail.com",
    license='MIT',
    py_modules=['deque'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-cov', 'tox']},
)
