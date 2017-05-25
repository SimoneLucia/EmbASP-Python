#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

from codecs import open
from os import path

# import sys

# if sys.version_info < (3,6):
#     sys.exit('Sorry, Python < 3,6 is not supported')

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='embASP',
      version='0.4',
      description='embASP',
      long_description=long_description,
      author='Department of Mathematics and Computer Science, University of Calabria',
      license='MIT',
      author_email='embasp@mat.unical.it',
      url='https://www.mat.unical.it/calimeri/projects/embasp/',
      packages=find_packages(exclude=["*.unitTests", "*.unitTests.*", "unitTests.*", "unitTests"]),
      
      classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        ],
      
     )





