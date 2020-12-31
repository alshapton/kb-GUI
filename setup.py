#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import io
from setuptools import setup, find_packages


setup(name='kb-gui',
      version='0.1.0',
      description='A GUI for kb - the minimalist knowledge manager',
      keywords='kb-gui',
      author='alshaptono',
      author_email='alshapton@gmail.com',
      url='https://github.com/alshapton/kb-gui',
      #download_url='https://github.com/gnebbia/kb/archive/v0.1.5.tar.gz',
      license='GPLv3',
      long_description=io.open(
          './docs/README.md', 'r', encoding='utf-8').read(),
      long_description_content_type="text/markdown",
      platforms='any',
      zip_safe=False,
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[ 'Programming Language :: Python',
                    'Programming Language :: Python :: 3',
                    'Programming Language :: Python :: 3.6',
                    'Programming Language :: Python :: 3.7',
                    'Programming Language :: Python :: 3.8',
                    'Programming Language :: Python :: 3.9',
                    'Operating System :: OS Independent',
                   ], 
      packages=find_packages(exclude=('tests',)),
      include_package_data=True,
      install_requires=["kb-manager>=0.1.5","toml","attr","attrs","flask","flask-httpauth","MarkupSafe"],
      python_requires='>=3.6',
      )
