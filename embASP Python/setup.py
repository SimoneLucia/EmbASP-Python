#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages
import sys

if sys.version_info < (3,6):
    sys.exit('Sorry, Python < 3,6 is not supported')
    
setup(name='embASP',
      version='0.1',
      description='embASP',
      author='Department of Mathematics and Computer Science, University of Calabria',
      author_email='embasp@mat.unical.it',
      url='https://www.mat.unical.it/calimeri/projects/embasp/',
      packages=find_packages(),
     )
