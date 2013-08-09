""" Folder
"""
from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import Schema, registerType
from Products.ATContentTypes.content.folder import ATBTreeFolder
from Products.EEAEnquiry.config import PROJECTNAME

schema = Schema((),)

EnquiryFolder_schema = getattr(ATBTreeFolder, 'schema', Schema(())).copy() + \
    schema.copy()


class EnquiryFolder(ATBTreeFolder):
    """ Enquiry Folder
    """
    security = ClassSecurityInfo()
    archetype_name = 'EnquiryFolder'
    meta_type      = 'EnquiryFolder'
    portal_type    = 'EnquiryFolder'
    _at_rename_after_creation = True
    schema = EnquiryFolder_schema

    security.declarePublic('getCatalogs')
    def getCatalogs(self):
        """ Catalogs
        """
        return []

    def is_folderish(self):
        """ EnquiryFolder is folderish
        """
        return True

def register():
    """ Register
    """
    registerType(EnquiryFolder, PROJECTNAME)
