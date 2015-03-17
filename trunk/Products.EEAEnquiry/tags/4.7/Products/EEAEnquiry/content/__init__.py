""" Enquiry Content
"""
from Products.EEAEnquiry.content import Enquiry
from Products.EEAEnquiry.content import EnquiryRequestor
from Products.EEAEnquiry.content import EnquiryFolder
from Products.EEAEnquiry.content import EnquiryRequestorFolder

def register_content():
    """ Register content
    """
    Enquiry.register()
    EnquiryRequestor.register()
    EnquiryFolder.register()
    EnquiryRequestorFolder.register()
