""" Base TestCase for EEAEnquiry
"""


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
    """ Suite
    """
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(EnquiryTestCase))
    return suite

