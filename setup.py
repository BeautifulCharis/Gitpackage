from setuptools import setup, Gitpackage
setup(
name ='Gitpackage',
version= '0.1',
packages=find_package(exclude=['tests']),
license= 'MIT',
description= 'EDSA example python package',
long_dscription=open('README.md').read(),
install_requires= ['numpy'],
url= 'https://github.com/BeautifulCharis/Gitpackage.git',
author= 'Olubukola Alayande',
author_email= 'olubukkyalayand@gmail.com')