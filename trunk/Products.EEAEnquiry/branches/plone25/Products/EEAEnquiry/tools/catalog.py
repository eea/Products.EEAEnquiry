from Globals import InitializeClass
from Products.CMFPlone.CatalogTool import CatalogTool as BaseTool

class EnquiryCatalog(BaseTool):
    """ Catalog for enquiries and requestors since we don't want public to find them. """
    
    id = 'portal_enquiry_catalog'

def register_catalog():
    InitializeClass(EnquiryCatalog)
