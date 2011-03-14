# -*- coding: utf-8 -*-
#
# File: Requestor.py
#
# Copyright (c) 2006 by []
# Generator: ArchGenXML Version 1.5.0 svn/devel
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
        Schema, StringField, StringWidget, SelectionWidget, BaseSchema, 
        BaseContent, registerType
    )

from Products.EEAEnquiry.config import PROJECTNAME

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='email',
        widget=StringWidget(
            label="Email address",
            label_msgid='EEAEnquiry_label_email',
            i18n_domain='EEAEnquiry',
        ),
        required=True
    ),

    StringField(
        name='password',
        widget=StringWidget(
            label='Password',
            label_msgid='EEAEnquiry_label_password',
            i18n_domain='EEAEnquiry',
        )
    ),

    StringField(
        name='sex',
        widget=SelectionWidget(
            label="Mr/Ms",
            label_msgid='EEAEnquiry_label_sex',
            i18n_domain='EEAEnquiry',
        ),
        multiValued=0,
        vocabulary=('Mr','Ms')
    ),

    StringField(
        name='firstname',
        widget=StringWidget(
            label="First name",
            label_msgid='EEAEnquiry_label_firstname',
            i18n_domain='EEAEnquiry',
        ),
        required=True
    ),

    StringField(
        name='lastname',
        widget=StringWidget(
            label="surname",
            label_msgid='EEAEnquiry_label_lastname',
            i18n_domain='EEAEnquiry',
        ),
        required=True
    ),

    StringField(
        name='country',
        widget=SelectionWidget(
            label='Country',
            label_msgid='EEAEnquiry_label_country',
            i18n_domain='EEAEnquiry',
        ),
        required=True,
        vocabulary=['Please select', 'Albania', 'Algeria', 'American Samoa','Andorra','Angola','Anguilla','Antarctica','Antigua and Barbuda','Argentina','Armenia','Aruba','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bermuda','Bhutan','Bolivia','Bosnia and Herzegovina','Botswana','Bouvet Island','Brazil','British Indian Ocean Territory','Brunei Darussalam','Bulgaria','Burkina FASO','Burma','Burundi','Cambodia','Cameroon','Canada','Canary Island','Cape Verde','Cayman Islands','Central African Republic','Chad','Chile','China','Christmas Island','Cocos (Keeling) Islands','Colombia','Comoros','Congo','Congo, The Democratic Republic of the','Cook Islands','Costa Rica','Cote d\'Ivoire','Croatia','Cyprus','Czech Republic','Denmark','Djibouti','Dominica','Dominican Republic','East Timor','Ecuador','Egypt','El Salvador','England','Equatorial Guinea','Eritrea','Espana','Estonia','Ethiopia','Falkland Islands','Faroe Islands','Fiji','Finland','France','French Guiana','French Polynesia','French Southern Territories','Gabon','Gambia','Georgia','Germany','Ghana','Gibraltar','Great Britain','Greece','Greenland','Grenada','Guadeloupe','Guam','Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti','Heard and Mc Donald Islands','Honduras','Hong Kong','Hungary','Iceland','India','Indonesia','Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati','Korea, Republic of','Korea (South)','Kuwait','Kyrgyzstan','Lao People\'s Democratic Republic','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Macau','Macedonia','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands','Martinique','Mauritania','Mauritius','Mayotte','Mexico','Micronesia, Federated States of','Moldova, Republic of','Monaco','Mongolia','Montserrat','Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal','Netherlands','Netherlands Antilles','New Caledonia','New Zealand','Nicaragua','Niger','Nigeria','Niue','Norfolk Island','Northern Ireland','Northern Mariana Islands','Norway','Oman','Pakistan','Palau','Panama','Papua New Guinea','Paraguay','Peru','Philippines','Pitcairn','Poland','Portugal','Puerto Rico','Qatar','Reunion','Romania','Russia','Russian Federation','Rwanda','Saint Kitts and Nevis','Saint Lucia','Saint Vincent and the Grenadines','Samoa (Independent)','San Marino','Sao Tome and Principe','Saudi Arabia','Scotland','Senegal','Serbia and Montenegro','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands','Somalia','South Africa','South Georgia and the South Sandwich Islands','South Korea','Spain','Sri Lanka','St. Helena','St. Pierre And Miquelon','Suriname','Svalbard and Jan Mayen Islands','Swaziland','Sweden','Switzerland','Tajikistan','Tanzania','Thailand','Togo','Tokelau','Tonga','Trinidad','Trinidad and Tobago','Tunisia','Turkey','Turkmenistan','Turks and Caicos Islands','Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom','United States','United States Minor Outlying Islands','Uruguay','U.S.A.','Uzbekistan','Vanuatu','Vatican City State (Holy See)','Venezuela','Viet Nam','Virgin Islands (British)','Virgin Islands (U.S.)','Wales','Wallis and Futuna Islands','Western Sahara','Yemen','Zambia','Zimbabwe']
    ),

    StringField(
        name='org',
        widget=StringWidget(
            label="Organisation",
            label_msgid='EEAEnquiry_label_org',
            i18n_domain='EEAEnquiry',
        )
    ),

    StringField(
        name='phone',
        widget=StringWidget(
            label="Phone number",
            label_msgid='EEAEnquiry_label_phone',
            i18n_domain='EEAEnquiry',
        )
    ),

    StringField(
        name='fax',
        widget=StringWidget(
            label="Fax number",
            label_msgid='EEAEnquiry_label_fax',
            i18n_domain='EEAEnquiry',
        )
    ),

    StringField(
        name='address',
        widget=StringWidget(
            label='Address',
            label_msgid='EEAEnquiry_label_address',
            i18n_domain='EEAEnquiry',
        )
    ),

    StringField(
        name='postalcode',
        widget=StringWidget(
            label="Postal code",
            label_msgid='EEAEnquiry_label_postalcode',
            i18n_domain='EEAEnquiry',
        )
    ),

    StringField(
        name='city',
        widget=StringWidget(
            label='City',
            label_msgid='EEAEnquiry_label_city',
            i18n_domain='EEAEnquiry',
        )
    ),

    StringField(
        name='region',
        widget=StringWidget(
            description="Please enter your state or region.",
            label='Region',
            label_msgid='EEAEnquiry_label_region',
            description_msgid='EEAEnquiry_help_region',
            i18n_domain='EEAEnquiry',
        )
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Requestor_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Requestor(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Requestor'

    meta_type = 'Requestor'
    portal_type = 'Requestor'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 1
    #content_icon = 'Requestor.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Requestor"
    typeDescMsgId = 'description_edit_requestor'

    _at_rename_after_creation = True

    schema = Requestor_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(Requestor, PROJECTNAME)
# end of class Requestor

##code-section module-footer #fill in your manual code here
##/code-section module-footer



