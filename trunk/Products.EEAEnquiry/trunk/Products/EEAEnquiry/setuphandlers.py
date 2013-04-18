""" Various setup
"""
from Products.Archetypes.config import TOOL_NAME as ARCHETYPETOOLNAME
from Products.CMFCore.utils import getToolByName
from Products.PluginIndexes.FieldIndex.FieldIndex import FieldIndex
import logging

logger = logging.getLogger("Products.EEAEnquiry.setuphandlers")


def installTypesCatalog(context):
    """ Configure CatalogMultiplex:
        explicit add classes (meta_types) be indexed in catalogs (white)
        or removed from indexing in a catalog (black)
    """

    if context.readDataFile('Products.EEAEnquiry.txt') is None:
        return

    logger.info("Setting custom cataloging for types")

    site = context.getSite()
    atool = getToolByName(site, ARCHETYPETOOLNAME)
    catalogmap = {}
    catalogmap['Enquiry'] = {}
    catalogmap['Enquiry']['black'] = ['portal_catalog']
    catalogmap['EnquiryRequestor'] = {}
    catalogmap['EnquiryRequestor']['black'] = ['portal_catalog']
    for meta_type in catalogmap:
        submap = catalogmap[meta_type]
        current_catalogs = set([c.id for
                                c in atool.getCatalogsByType(meta_type)])
        if 'white' in submap:
            for catalog in submap['white']:
                if not getToolByName(site, catalog, False):
                    raise AttributeError(
                        'Catalog "%s" does not exist!' % catalog)
                current_catalogs.update([catalog])
        if 'black' in submap:
            for catalog in submap['black']:
                if catalog in current_catalogs:
                    current_catalogs.remove(catalog)
        atool.setCatalogsByType(meta_type, list(current_catalogs))


#TODO: plone4, see if this is needed

def switchPathIndex(context):
    """Changes the 'path' index to ExtendedPathIndex."""

    portal = context.getSite()
    catalog = getToolByName(portal, 'portal_enquiry_catalog', None)
    if catalog is not None:
        try:
            index = catalog._catalog.getIndex('path')
        except KeyError:
            pass
        else:
            indextype = index.__class__.__name__
            if indextype == 'ExtendedPathIndex':
                return
            catalog.delIndex('path')
            logger.info("Deleted %s 'path' from portal_catalog.", indextype)

        catalog.addIndex('path', 'ExtendedPathIndex')
        logger.info("Added ExtendedPathIndex 'path' to portal_catalog.")

        #TODO: If this is still needed, then catalog reindexing is needed


def installCatalogIndexes(context):
    """ Catalog indexes
    """
    if context.readDataFile('Products.EEAEnquiry.txt') is None:
        return

    portal = context.getSite()
    catalog = getToolByName(portal, 'portal_enquiry_catalog')

    try:
        catalog._catalog.getIndex('portal_type')
        catalog._catalog.getIndex('Title')
    except KeyError:
        logger.info("Adding indexes to catalog")
        FieldIndex("portal_type")

        class Empty:
            """ Empty """
            pass

        elem = []

        wordSplitter = Empty()
        wordSplitter.group = 'Word Splitter'
        wordSplitter.name = 'HTML aware splitter'

        caseNormalizer = Empty()
        caseNormalizer.group = 'Case Normalizer'
        caseNormalizer.name = 'Case Normalizer'

        stopWords = Empty()
        stopWords.group = 'Stop Words'
        stopWords.name = 'Remove listed and single char words'

        elem.append(wordSplitter)
        elem.append(caseNormalizer)
        elem.append(stopWords)
        catalog.manage_addProduct['ZCTextIndex'].manage_addLexicon(
            'plone_lexicon', 'Default Lexicon', elem)

        title_extras = Empty()
        title_extras.doc_attr = 'Title'
        title_extras.index_type = 'Okapi BM25 Rank'
        title_extras.lexicon_id = 'plone_lexicon'

        catalog.addIndex('portal_type', 'FieldIndex')
        catalog.addIndex('Title', "ZCTextIndex", title_extras)

        catalog.addColumn('portal_type')
        catalog.addColumn('Title')

