#!/usr/bin/env python

from setuptools import setup

setup(
    name='gittip-twisted',
    version='0.1.2',
    description='Library for accessing Gittip APIs',
    author='Alexander Zykov',
    author_email='tigernwh@gmail.com',
    url='https://github.com/TigerND/gittip-twisted',
    package_dir={
        'txgittip': 'src'
    },
    packages=[
        'txgittip',
    ],
    data_files=[
    ],
    install_requires = [
        'Twisted>=14.0.0',
    ],
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)
