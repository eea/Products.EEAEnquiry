from StringIO import StringIO
from Products.CMFCore.utils import getToolByName

def switchPathIndex(portal, out):
    """Changes the 'path' index to ExtendedPathIndex."""
    catalog = getToolByName(portal, 'portal_enquiry_catalog', None)
    if catalog is not None:
        try:
            index = catalog._catalog.getIndex('path')
        except KeyError:
            pass
        else:
            indextype = index.__class__.__name__
            if indextype == 'ExtendedPathIndex':
                return 0
            catalog.delIndex('path')
            out.append("Deleted %s 'path' from portal_catalog." % indextype)

        catalog.addIndex('path', 'ExtendedPathIndex')
        out.append("Added ExtendedPathIndex 'path' to portal_catalog.")
        return 1 # Ask for reindexing
    return 0

def afterInstall(self, reinstall, product):
    out = []
    switchPathIndex(self, out)
    return out


def install(portal):
    out = StringIO()
    catalog = getToolByName(portal, 'portal_enquiry_catalog', None)
    if catalog is None:
        portal.manage_addProduct['EEAEnquiry'].manage_addTool('Plone Catalog Tool', None)
        print >> out, 'Installed Enquiry catalog'
    return out
