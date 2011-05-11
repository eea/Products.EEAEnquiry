# -*- coding: utf-8 -*-
#
# File: Install.py
#
# Copyright (c) 2006 by []
# Generator: ArchGenXML Version 1.5.1-svn
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'


from StringIO import StringIO
from sets import Set
#from App.Common import package_home
from Products.CMFCore.utils import getToolByName
#from Products.CMFCore.utils import manage_addTool
from Products.ExternalMethod.ExternalMethod import ExternalMethod
from zExceptions import NotFound #, BadRequest

from Products.Archetypes.Extensions.utils import installTypes
from Products.Archetypes.Extensions.utils import install_subskin
from Products.Archetypes.config import TOOL_NAME as ARCHETYPETOOLNAME
from Products.Archetypes.atapi import listTypes
from Products.EEAEnquiry.config import PROJECTNAME
from Products.EEAEnquiry.config import product_globals as GLOBALS
from transaction import get as get_transaction
import logging
logger = logging.getLogger("Products.EEAEnquiry.Extensions.Install")

#renamed to prevent having it active. This module should be removed during plone4 migration
def install_old(self):
    """ External Method to install EEAEnquiry """
    out = StringIO()
    print >> out, "Installation log of %s:" % PROJECTNAME

    # If the config contains a list of dependencies, try to install
    # them.  Add a list called DEPENDENCIES to your custom
    # AppConfig.py (imported by config.py) to use it.
    try:
        from Products.EEAEnquiry.config import DEPENDENCIES
        DEPENDENCIES
    except ImportError:
        DEPENDENCIES = []
    portal = getToolByName(self,'portal_url').getPortalObject()
    quickinstaller = portal.portal_quickinstaller
    for dependency in DEPENDENCIES:
        print >> out, "Installing dependency %s:" % dependency
        quickinstaller.installProduct(dependency)
        get_transaction().commit()

    classes = listTypes(PROJECTNAME)
    installTypes(self, out,
                 classes,
                 PROJECTNAME)
    install_subskin(self, out, GLOBALS)


    # Configure CatalogMultiplex:
    # explicit add classes (meta_types) be indexed in catalogs (white)
    # or removed from indexing in a catalog (black)
    atool = getToolByName(self, ARCHETYPETOOLNAME)
    catalogmap = {}
    catalogmap['Enquiry'] = {}
    catalogmap['Enquiry']['black'] = ['portal_catalog']
    catalogmap['EnquiryRequestor'] = {}
    catalogmap['EnquiryRequestor']['black'] = ['portal_catalog']
    for meta_type in catalogmap:
        submap = catalogmap[meta_type]
        current_catalogs = Set([c.id for c in atool.getCatalogsByType(meta_type)])
        if 'white' in submap:
            for catalog in submap['white']:
                if not getToolByName(self, catalog, False):
                    raise AttributeError, 'Catalog "%s" does not exist!' % catalog
                current_catalogs.update([catalog])
        if 'black' in submap:
            for catalog in submap['black']:
                if catalog in current_catalogs:
                    current_catalogs.remove(catalog)
        atool.setCatalogsByType(meta_type, list(current_catalogs))

    # try to call a workflow install method
    # in 'InstallWorkflows.py' method 'installWorkflows'
    try:
        installWorkflows = ExternalMethod('temp', 'temp',
                                          PROJECTNAME+'.InstallWorkflows',
                                          'installWorkflows').__of__(self)
    except NotFound:
        installWorkflows = None

    if installWorkflows:
        print >>out,'Workflow Install:'
        res = installWorkflows(self,out)
        print >>out,res or 'no output'
    else:
        print >>out,'no workflow install'

    #bind classes to workflows
    #wft = getToolByName(self,'portal_workflow')

    # enable portal_factory for given types
    factory_tool = getToolByName(self,'portal_factory')
    factory_types=[
        "Enquiry",
        "EnquiryRequestor",
        "EnquiryFolder",
        "EnquiryRequestorFolder",
        ] + factory_tool.getFactoryTypes().keys()
    factory_tool.manage_setPortalFactoryTypes(listOfTypeIds=factory_types)
