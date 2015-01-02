#!/usr/bin/env python

from setuptools import setup

setup(
    name='gratipay-twisted',
    version='0.1.3',
    description='Library for accessing Gratipay APIs',
    author='Alexander Zykov',
    author_email='tigernwh@gmail.com',
    url='https://github.com/TigerND/gratipay-twisted',
    package_dir={
        'txgratipay': 'src'
    },
    packages=[
        'txgratipay',
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
