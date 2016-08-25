# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="double linked-list",
    description="Implementation of a double linked list",
    version='0.1.0',
    author="David Smith, Jeff Torres",
    author_email="dbsmith.dbs83@gmail.com, jeffrey.n.torres@gmail.com",
    license='MIT',
    py_modules=['dbl_lnk_lst'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-cov', 'tox']},
)
