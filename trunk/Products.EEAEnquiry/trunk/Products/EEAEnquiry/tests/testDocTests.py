import unittest
from zope.testing import doctest
#from Testing import ZopeTestCase
from Testing.ZopeTestCase import ZopeDocTestSuite


import EnquiryTestCase

optionflags =  (doctest.ELLIPSIS |
                doctest.NORMALIZE_WHITESPACE |
                doctest.REPORT_ONLY_FIRST_FAILURE)

def test_suite():
    return unittest.TestSuite(
        [ZopeDocTestSuite(module,
                          test_class=EnquiryTestCase.EnquiryTestCase,
                          optionflags=optionflags)
         for module in ('Products.EEAEnquiry.browser.enquiry',
                        )]
        )
