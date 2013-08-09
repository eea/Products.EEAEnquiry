""" Requestor folder
"""
from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import registerType, Schema
from Products.ATContentTypes.content.folder import ATBTreeFolder
from Products.EEAEnquiry.config import PROJECTNAME
from Products.CMFCore.permissions import ModifyPortalContent

schema = Schema((

),
)

EnquiryRequestorFolder_schema = getattr(
    ATBTreeFolder, 'schema', Schema(())).copy() + schema.copy()

class EnquiryRequestorFolder(ATBTreeFolder):
    """ Enquiry Requestor Folder
    """
    security = ClassSecurityInfo()

    # This name appears in the 'add' box
    archetype_name = 'EnquiryRequestorFolder'
    meta_type = 'EnquiryRequestorFolder'
    portal_type = 'EnquiryRequestorFolder'
    allowed_content_types = ['EnquiryRequestor'] + list(
        getattr(ATBTreeFolder, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 0
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "EnquiryRequestorFolder"
    typeDescMsgId = 'description_edit_enquiryrequestorfolder'
    actions = (
          {'id': 'export_csv',
           'name': 'Export to CSV',
           'action': 'string:${object_url}/export_csv',
           'permissions': (ModifyPortalContent,)},
              )

    _at_rename_after_creation = True
    schema = EnquiryRequestorFolder_schema

    security.declarePublic('getCatalogs')
    def getCatalogs(self):
        """ Catalogs
        """
        return []

def register():
    """ Register
    """
    registerType(EnquiryRequestorFolder, PROJECTNAME)
