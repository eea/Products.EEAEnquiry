""" Config
"""
from Products.CMFCore.permissions import setDefaultRoles
PROJECTNAME = "EEAEnquiry"

DEFAULT_ADD_CONTENT_PERMISSION = "Add portal content"
setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner'))

ADD_CONTENT_PERMISSIONS = {
    'Enquiry': 'Add Enquiry',
    'EnquiryRequestor': 'Add Enquiry requestor',
}

product_globals = globals()

