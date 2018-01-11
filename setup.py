"""
Setup of autolab_suction python codebase
Author: Jeff Mahler
"""
from setuptools import setup

requirements = [
    'pyserial'
]

setup(name='autolab_suction',
      version='0.1.0',
      description='AUTOLAB suction control code for YuMi',
      author='Xinyu Liu',
      author_email='xinyuliu@berkeley.edu',
      package_dir = {'': '.'},
      packages=['autolab_suction'],
      install_requires=requirements
     )

