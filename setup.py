#!/usr/bin/env python

import os
import sys

from setuptools import setup, find_packages
import KindlePush


setup(
		name = 'KindlePush',
		version = KindlePush.__version__,
		description = "Kindle Push",
		long_description = open('README.rst').read(),
		author='saeedwang',
		author_email='blandlove123@gmail.com',
		url='',
		packages = find_packages('KindlePush'),
		package_dir = {'':'KindlePush'},  
		install_requires=['mailthon'],
		scripts=['KindlePush/KindlePush.py'],
		entry_points = {
			'console_scripts': [
				'KindlePush = KindlePush:main',
				]
		}
)


