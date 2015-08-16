#!/usr/bin/env python
import sys
from setuptools import setup

setup(
  name='fakelxc',
  version='0.1',
  description="Fake LXC for testing in travis",
  long_description=open('README.md').read(),
  author='Jeremy Mouton',
  author_email='moutonjeremy@labbs.fr',
  url='https://github.com/Jeremmm/fake-lxc/',
  license="LGPL",
  keywords="lxc",
  packages=['fakelxc'],
  include_package_data=True,
  entry_points={
    'console_scripts': [
      'lxc-info = fakelxc.lxcinfo:main',
      'lxc-ls = fakelxc.lxcls:main'
    ]
  },
  data_files=[(sys.prefix + '/var/lib/lxc/test1', ['conf/test1/config']),
              (sys.prefix + '/var/lib/lxc/test2', ['conf/test2/config']),
              (sys.prefix + '/var/lib/lxc/test3', ['conf/test3/config'])]
)
