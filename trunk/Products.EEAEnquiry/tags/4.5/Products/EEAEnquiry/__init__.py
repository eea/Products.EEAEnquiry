""" Initialize
"""
from Products.Archetypes import atapi
from Products.Archetypes import listTypes
from Products.CMFCore import utils as cmfutils
from Products.EEAEnquiry import config
import logging
logger = logging.getLogger('Products.EEAEnquiry')

def initialize(context):
    """ Zope 2
    """
    from Products.EEAEnquiry.tools import catalog

    cmfutils.ToolInit('Enquiry Tool'
             , tools=( catalog.EnquiryCatalog,  )
             , icon='tool.gif'
             ).initialize( context )

    from Products.EEAEnquiry import content
    content.register_content()

    # Initialize portal content
    all_content_types, all_constructors, all_ftis = atapi.process_types(
        listTypes(config.PROJECTNAME),
        config.PROJECTNAME)

    cmfutils.ContentInit(
        config.PROJECTNAME + ' Content',
        content_types      = all_content_types,
        permission         = config.DEFAULT_ADD_CONTENT_PERMISSION,
        extra_constructors = all_constructors,
        fti                = all_ftis,
        ).initialize(context)

    # Give it some extra permissions to control them on a per class limit
    for i in range(0, len(all_content_types)):
        klassname = all_content_types[i].__name__
        if not klassname in config.ADD_CONTENT_PERMISSIONS:
            continue

        context.registerClass(
            meta_type   = all_ftis[i]['meta_type'],
            constructors= (all_constructors[i],),
            permission  = config.ADD_CONTENT_PERMISSIONS[klassname])
