# -*- coding: utf-8 -*-
#
# File: EnquiryFolder.py
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

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import Schema, registerType 
from Products.ATContentTypes.content.folder import ATBTreeFolder
from Products.EEAEnquiry.config import PROJECTNAME

schema = Schema((),) 

EnquiryFolder_schema = getattr(ATBTreeFolder, 'schema', Schema(())).copy() + \
    schema.copy()


class EnquiryFolder(ATBTreeFolder):
    """
    """
    security = ClassSecurityInfo()
    #__implements__ = (getattr(ATBTreeFolder,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'EnquiryFolder'
    meta_type      = 'EnquiryFolder'
    portal_type    = 'EnquiryFolder'

    #allowed_content_types = ['Enquiry', 'EnquiryRequestorFolder'] + \
            #list(getattr(ATBTreeFolder, 'allowed_content_types', []))
    #filter_content_types = 1
    #global_allow = 1
    #content_icon = 'EnquiryFolder.gif'
    #immediate_view = 'base_view'
    #default_view = 'base_view'
    #suppl_views = ()
    #typeDescription = "EnquiryFolder"
    #typeDescMsgId = 'description_edit_enquiryfolder'

    _at_rename_after_creation = True

    schema = EnquiryFolder_schema

    security.declarePublic('getCatalogs')
    def getCatalogs(self):
        return []


def register():
    registerType(EnquiryFolder, PROJECTNAME)
