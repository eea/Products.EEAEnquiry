""" Test-cases for class(es) Enquiry
"""
from Products.EEAEnquiry.tests.EnquiryTestCase import EnquiryTestCase

class testEnquiry(EnquiryTestCase):
    """Test-cases for class(es) Enquiry."""

    def afterSetUp(self):
        """ Setup """
        pass

    # Manually created methods
    def test_Enquiry(self):
        """ Test
        """
        self.setRoles('Manager')
        root = self.portal
        eid = root.invokeFactory(type_name='EnquiryFolder', id="enquiry",
                                title='Enquiries for EEA' )
        eFolder = getattr(root, eid)
        eid = eFolder.invokeFactory(
            type_name='EnquiryRequestorFolder', id="requestors",
            title='Requestors for EEA' )
        eReqFolder = getattr(eFolder, eid)
        self.logout()

        eid = eFolder.invokeFactory(
            type_name='Enquiry', id="e1",
            title="Enquiry 1", description="description enquiry 1")
        en = getattr(eFolder, eid)
        self.failIf(en.getEnquiryRequestor() is not None)

        eid = eReqFolder.invokeFactory(
            type_name='EnquiryRequestor', id="er1",
            title="Enquiry requestor 1", description="description enquiry 1")

        eReq = getattr(eReqFolder, eid)
        en.setEnquiryRequestor(eReq)
        self.failIf(en.getEnquiryRequestor() != eReq)


def test_suite():
    """ Suite
    """
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testEnquiry))
    return suite

