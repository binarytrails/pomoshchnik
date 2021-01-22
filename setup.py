#!/usr/bin/env python

# @author Vsevolod Ivanov <seva@binarytrails.net>

from setuptools import setup, find_packages, Extension

setup(
    name='pomoshchnik',
    version='0.1',
    description='Pomoshchnik - Web Automation Assistant',
    url='https://github.com/binarytrails/pomoshchnik',
    author='Vsevolod (Seva) Ivanov',
    author_email='seva@binarytrails.net',
    license='GPLv3+',
    keywords='pomoshchnik selenium automation',
    platforms='any',
    packages=['pomoshchnik'],
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Automation',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'selenium'
    ],
    entry_points={
        'console_scripts': [ 'pomoshchnik=pomoshchnik.main:main']
    }
)
