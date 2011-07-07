# -*- coding: utf-8 -*-
#
# File: EnquiryTestCase.py
#
# Copyright (c) 2006 by []
# Generator: ArchGenXML Version 1.5.1-svn
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

#
# Base TestCase for EEAEnquiry
#


from Products.PloneTestCase import PloneTestCase
from Products.PloneTestCase.layer import onsetup
from Testing import ZopeTestCase as ztc
import logging


logger = logging.getLogger("Products.EEAEnquiry.tests.EnquiryTestCase")


PRODUCTS = ['EEAEnquiry']
PROFILES = [
            'Products.EEAEnquiry:default',
            'Products.EEAEnquiry:testfixture',
            ]

ztc.installProduct('EEAEnquiry')

@onsetup
def setup_site():
    """ Set up
    """
    pass



setup_site()

PloneTestCase.setupPloneSite(products=PRODUCTS, extension_profiles=PROFILES)

class EnquiryTestCase(PloneTestCase.PloneTestCase):
    """Base TestCase for EEAEnquiry."""


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(EnquiryTestCase))
    return suite

