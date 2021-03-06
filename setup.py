#!/usr/bin/env python

# see http://bugs.python.org/issue8876
# this is just a quick hack so we can test build in vagrant
import os
if os.environ.get('USER','') == 'vagrant':
  del os.link

from setuptools import setup, find_packages

def requirements():
    with open('./requirements.txt') as f:
        return [l.strip('\n') for l in f if l.strip('\n') and not l.startswith('#')]

setup(name='lrdatatypes',
      version='0.1',
      description='Provides core Land Registry data types to dependent applications',
      author='Land Registry',
      author_email='adam.shimali@digital.cabinet-office.gov.uk',
      url='http://github.com/LandRegistry/audit-plugin',
      download_url = 'http://github.com/LandRegistry/audit-plugin/tarball/alpha',
      packages=find_packages(exclude=['tests']),
      zip_safe=False,
      include_package_data=True,
      license='MIT',
      platforms='any',
      install_requires=requirements(),
      keywords = ['validation'],
      classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 2.7',
        ),
)
