""" Initialize
"""
import logging
logger = logging.getLogger('Products.EEAEnquiry')

from Products.CMFCore import utils as cmfutils
from Products.CMFCore import DirectoryView
from Products.Archetypes import atapi
from Products.Archetypes import listTypes
from Products.EEAEnquiry import config

CustomizationPolicy = None
try:
    import CustomizationPolicy
except ImportError, err:
    logger.debug(err)

DirectoryView.registerDirectory('skins', config.product_globals)
DirectoryView.registerDirectory('skins/EEAEnquiry',
                                    config.product_globals)

def initialize(context):
    """ Zope 2
    """
    from tools import catalog

    cmfutils.ToolInit('Enquiry Tool'
             , tools=( catalog.EnquiryCatalog,  )
             , icon='tool.gif'
             ).initialize( context )

    ##/code-section custom-init-top

    # imports packages and types for registration
    import content

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

    # Apply customization-policy, if theres any
    if CustomizationPolicy and hasattr(CustomizationPolicy, 'register'):
        CustomizationPolicy.register(context)
        print 'Customization policy for EEAEnquiry installed'
