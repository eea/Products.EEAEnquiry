# -*- coding: utf-8 -*-
#
# File: testEnquiry.py
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
# Test-cases for class(es) Enquiry
#

#from Testing import ZopeTestCase
#from Products.EEAEnquiry.config import *
from Products.EEAEnquiry.tests.EnquiryTestCase import EnquiryTestCase

# Import the tested classes
#from Products.EEAEnquiry.content.Enquiry import Enquiry


class testEnquiry(EnquiryTestCase):
    """Test-cases for class(es) Enquiry."""

    def afterSetUp(self):
        pass

    # Manually created methods

    def test_Enquiry(self):
        self.setRoles('Manager')
        root = self.portal
        eid = root.invokeFactory(type_name='EnquiryFolder', id="enquiry",
                                title='Enquiries for EEA' )
        eFolder = getattr(root, eid)
        eid = eFolder.invokeFactory(type_name='EnquiryRequestorFolder', id="requestors",
                                title='Requestors for EEA' )
        eReqFolder = getattr(eFolder, eid)

        self.logout()
        eid = eFolder.invokeFactory(type_name='Enquiry', id="e1",
                                    title="Enquiry 1", description="description enquiry 1")
        en = getattr(eFolder, eid)
        self.failIf(en.getEnquiryRequestor() is not None)

        eid = eReqFolder.invokeFactory(type_name='EnquiryRequestor', id="er1",
                                   title="Enquiry requestor 1", description="description enquiry 1")

        eReq = getattr(eReqFolder, eid)
        en.setEnquiryRequestor(eReq)
        self.failIf(en.getEnquiryRequestor() != eReq)


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testEnquiry))
    return suite

