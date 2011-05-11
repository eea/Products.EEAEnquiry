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

setDefaultRoles('Add Enquiry', ('Manager',))
setDefaultRoles('Add Enquiry requestor', ('Manager',))

product_globals = globals()

# Dependencies of Products to be installed by quick-installer
# override in custom configuration
DEPENDENCIES = [ 'ATVocabularyManager', ]

# Dependend products - not quick-installed - used in testcase
# override in custom configuration
PRODUCT_DEPENDENCIES = []

# STYLESHEETS = [{'id': 'my_global_stylesheet.css'},
#                {'id': 'my_contenttype.css',
#              'expression': 'python:object.getTypeInfo().getId() == "MyType"'}]
# You can do the same with JAVASCRIPTS.
STYLESHEETS = []
JAVASCRIPTS = []
