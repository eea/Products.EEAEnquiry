""" setup.py """

import os
from setuptools import setup, find_packages

name = 'Products.EEAEnquiry'
path = name.split('.') + ['version.txt']
version = open(os.path.join(*path)).read().strip()

setup(
 name='Products.EEAEnquiry',
 version=version,
 description="EEA Enquiry product",
 long_description=open("README.rst").read() + "\n" +
                  open(os.path.join("docs", "HISTORY.txt")).read(),
 # http://pypi.python.org/pypi?%3Aaction=list_classifiers
 classifiers=[
     "Framework :: Zope2",
     "Framework :: Plone",
     "Framework :: Plone :: 4.0",
     "Framework :: Plone :: 4.1",
     "Framework :: Plone :: 4.2",
     "Framework :: Plone :: 4.3",
     "Programming Language :: Zope",
     "Programming Language :: Python",
     "Programming Language :: Python :: 2.7",
     "Topic :: Software Development :: Libraries :: Python Modules",
     "License :: OSI Approved :: GNU General Public License (GPL)",
 ],
 keywords='EEA Enquiry Add-ons Plone Zope',
 author='European Environment Agency: IDM2 A-Team',
 author_email='eea-edw-a-team-alerts@googlegroups.com',
 url='https://github.com/eea/Products.EEAEnquiry',
 license='GPL',
 packages=find_packages(exclude=['ez_setup']),
 namespace_packages=['Products'],
 include_package_data=True,
 zip_safe=False,
 install_requires=[
     "setuptools",

     "Products.ATVocabularyManager",
     "Products.EEAPloneAdmin",  #has the necessary workflows

 ],
 entry_points="""
 # -*- Entry points: -*-
 """,
 )
