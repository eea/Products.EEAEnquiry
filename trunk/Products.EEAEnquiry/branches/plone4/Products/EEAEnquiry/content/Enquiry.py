# -*- coding: utf-8 -*-
#
# File: Enquiry.py
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
from Products.Archetypes.atapi import (
        Schema, StringField, SelectionWidget, TextField, TextAreaWidget,
        ReferenceField, ReferenceWidget, BaseSchema, BaseContent, 
        registerType, StringWidget
)

import transaction
from Products.EEAEnquiry.config import PROJECTNAME
from Products.validation.validators import ExpressionValidator
from interfaces import IEnquiry
import zope.interface


schema = Schema((

    StringField(
        name='occupation',
        validators=(ExpressionValidator('''python:value != "Please select"'''),),
        widget=SelectionWidget(
            label='Occupation',
            label_msgid='EEAEnquiry_label_occupation',
            i18n_domain='EEAEnquiry',
        ),
        required=True,
        vocabulary=['Please select', 'Company','Government official / international organisation','Information centre / library / bookstore','Journalist','Media','NGO','Politician','Researcher','Student','Teacher (primary, secondary and tertiary)', 'N/A']
    ),

    StringField(
        name='purpuse',
        validators=(ExpressionValidator('''python:value != "Please select"'''),),
        widget=SelectionWidget(
            label="Purpose",
            label_msgid='EEAEnquiry_label_purpuse',
            i18n_domain='EEAEnquiry',
        ),
        required=True,
        vocabulary=['Please select','Administrative case work', 'Commercial purpose (companies)','Education (primary, secondary and tertiary)', 'Employment/ Contract opportunity', 'General interest', 'Information dissemination (incl. bookstores)','Non-commercial application',  'Policy-making/ public participation (incl. international institutions and NGO)', 'Research (incl. university assignments)', 'N/A']
    ),

    StringField(
        name='title',
        widget=StringWidget(
            label="Subject",
            label_msgid='EEAEnquiry_label_title',
            i18n_domain='EEAEnquiry',
        ),
        required=True,
        accessor="Title"
    ),

    TextField(
        name='description',
        widget=TextAreaWidget(
            label="Enquiry",
            label_msgid='EEAEnquiry_label_description',
            i18n_domain='EEAEnquiry',
        ),
        required=True,
        accessor="Description"
    ),

    StringField(
        name='email',
        widget=StringWidget(
            label="Email address",
            label_msgid='EEAEnquiry_label_email',
            i18n_domain='EEAEnquiry',
        ),
        required=1,
        validators=('isEmail',)
    ),

    ReferenceField(
        name='enquiryRequestor',
        widget=ReferenceWidget(
            label='Enquiryrequestor',
            label_msgid='EEAEnquiry_label_enquiryRequestor',
            i18n_domain='EEAEnquiry',
        ),
        allowed_types=('EnquiryRequestor',),
        multiValued=0,
        relationship='enquriyRequestor'
    ),

),
)

schema['enquiryRequestor'].widget.visible={'edit': 'invisible'}

Enquiry_schema = BaseSchema.copy() + \
    schema.copy()


class Enquiry(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Enquiry'

    meta_type = 'Enquiry'
    portal_type = 'Enquiry'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 0
    #content_icon = 'Enquiry.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Enquiry"
    typeDescMsgId = 'description_edit_enquiry'

    _at_rename_after_creation = True

    schema = Enquiry_schema

    zope.interface.implements(IEnquiry)

    security.declarePrivate('_renameAfterCreation')
    def _renameAfterCreation(self, check_auto_id=False):
        """Renames an requestor like its UID.
        """
        transaction.savepoint(optimistic=True)
        new_id = '%s' % self.UID()
        self.setId(new_id)
        return new_id


def register():
    registerType(Enquiry, PROJECTNAME)

