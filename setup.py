# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="queue",
    description="Implementation of a queue",
    version='0.1.0',
    author="David Smith, Jeff Torres",
    author_email="dbsmith.dbs83@gmail.com, jeffrey.n.torres@gmail.com",
    license='MIT',
    py_modules=['queue'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-cov', 'tox']},
)
