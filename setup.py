#!/usr/bin/env python
# coding: utf8

VERSION = '1.0.0'

import sys
import os
from setuptools import setup, find_packages
from setuptools.extension import Extension

extra_args = {}
if (sys.version_info[0] >= 3):
    extra_args['use_2to3'] = True


setup(name='py_assist',
      version=VERSION,
      description='python commandline console',
      author='zluo',
      url='https://github.com/zluo/py_assist',
      packages=find_packages(),
      package_data={'':['*.csv']},
      install_requires=['numpy', 'pandas>=0.19', 'pyyaml'],
      test_suite='nose.collector',
      setup_requires=['pytest_runner'],
      tests_require=['pytest'],
      **extra_args
      )
