# -*- coding: utf-8 -*-
from setuptools import setup

setup(
<<<<<<< HEAD
    name="simple_graph",
    description="Implementation of a simple graph",
=======
    name="priorityq",
    description="Implementation of a priority queue",
>>>>>>> 14b8896b73f893f9a505b03ecbe2134a40066f57
    version='0.1.0',
    author="David Smith, Jeff Torres",
    author_email="dbsmith.dbs83@gmail.com, jeffrey.n.torres@gmail.com",
    license='MIT',
<<<<<<< HEAD
    py_modules=['simple_graph'],
=======
    py_modules=['priorityq', 'binheap'],
>>>>>>> 14b8896b73f893f9a505b03ecbe2134a40066f57
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-cov', 'tox']},
)
