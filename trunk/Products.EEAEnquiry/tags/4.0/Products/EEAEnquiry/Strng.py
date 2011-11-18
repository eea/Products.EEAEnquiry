""" Strng
"""

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import (
        Schema, BaseSchema, BaseContent, registerType )
from Products.EEAEnquiry.config import PROJECTNAME

schema = Schema((
),
)

Strng_schema = BaseSchema.copy() + \
    schema.copy()

class Strng(BaseContent):
    """ Strng
    """
    security = ClassSecurityInfo()

    # This name appears in the 'add' box
    archetype_name = 'Strng'

    meta_type = 'Strng'
    portal_type = 'Strng'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 1
    #content_icon = 'Strng.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Strng"
    typeDescMsgId = 'description_edit_strng'

    _at_rename_after_creation = True

    schema = Strng_schema


registerType(Strng, PROJECTNAME)
