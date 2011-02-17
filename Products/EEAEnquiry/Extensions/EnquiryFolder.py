# -*- coding: utf-8 -*-
#
# File: EEAEnquiry.py
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


from Products.CMFCore.utils import getToolByName
from Products.CMFCore.WorkflowTool import addWorkflowFactory
from Products.DCWorkflow.DCWorkflow import DCWorkflowDefinition
from Products.ExternalMethod.ExternalMethod import ExternalMethod
from Products.EEAEnquiry.config import *

##code-section create-workflow-module-header #fill in your manual code here
##/code-section create-workflow-module-header


productname = 'EEAEnquiry'

def setupEnquiryFolder(self, workflow):
    """Define the EnquiryFolder workflow.
    """

    workflow.setProperties(title='EnquiryFolder')

    ##code-section create-workflow-setup-method-header #fill in your manual code here
    ##/code-section create-workflow-setup-method-header


    for s in ['open', 'closed']:
        workflow.states.addState(s)

    for t in ['close', 'open']:
        workflow.transitions.addTransition(t)

    for v in ['review_history', 'comments', 'time', 'actor', 'action']:
        workflow.variables.addVariable(v)

    workflow.addManagedPermission('Add Enquiry')
    workflow.addManagedPermission('Copy or Move')
    workflow.addManagedPermission('Delete objects')
    workflow.addManagedPermission('Add portal content')
    workflow.addManagedPermission('Add Enquiry requestor')

    for l in []:
        if not l in workflow.worklists.objectValues():
            workflow.worklists.addWorklist(l)

    ## Initial State

    workflow.states.setInitialState('open')

    ## States initialization

    stateDef = workflow.states['open']
    stateDef.setProperties(title="""open""",
                           transitions=['close'])
    stateDef.setPermission('Add Enquiry',
                           0,
                           ['Anonymous'])
    stateDef.setPermission('Copy or Move',
                           0,
                           ['Anonymous'])
    stateDef.setPermission('Delete objects',
                           0,
                           ['Anonymous'])
    stateDef.setPermission('Add portal content',
                           0,
                           ['Anonymous'])
    stateDef.setPermission('Add Enquiry requestor',
                           0,
                           ['Anonymous'])

    stateDef = workflow.states['closed']
    stateDef.setProperties(title="""closed""",
                           transitions=['open'])

    ## Transitions initialization

    transitionDef = workflow.transitions['close']
    transitionDef.setProperties(title="""close""",
                                new_state_id="""closed""",
                                trigger_type=1,
                                script_name="""""",
                                after_script_name="""""",
                                actbox_name="""close""",
                                actbox_url="""""",
                                actbox_category="""workflow""",
                                props={},
                                )

    transitionDef = workflow.transitions['open']
    transitionDef.setProperties(title="""open""",
                                new_state_id="""open""",
                                trigger_type=1,
                                script_name="""""",
                                after_script_name="""""",
                                actbox_name="""open""",
                                actbox_url="""""",
                                actbox_category="""workflow""",
                                props={},
                                )

    ## State Variable
    workflow.variables.setStateVar('review_state')

    ## Variables initialization
    variableDef = workflow.variables['review_history']
    variableDef.setProperties(description="""Provides access to workflow history""",
                              default_value="""""",
                              default_expr="""state_change/getHistory""",
                              for_catalog=0,
                              for_status=0,
                              update_always=0,
                              props={'guard_permissions': 'Request review; Review portal content'})

    variableDef = workflow.variables['comments']
    variableDef.setProperties(description="""Comments about the last transition""",
                              default_value="""""",
                              default_expr="""python:state_change.kwargs.get('comment', '')""",
                              for_catalog=0,
                              for_status=1,
                              update_always=1,
                              props=None)

    variableDef = workflow.variables['time']
    variableDef.setProperties(description="""Time of the last transition""",
                              default_value="""""",
                              default_expr="""state_change/getDateTime""",
                              for_catalog=0,
                              for_status=1,
                              update_always=1,
                              props=None)

    variableDef = workflow.variables['actor']
    variableDef.setProperties(description="""The ID of the user who performed the last transition""",
                              default_value="""""",
                              default_expr="""user/getId""",
                              for_catalog=0,
                              for_status=1,
                              update_always=1,
                              props=None)

    variableDef = workflow.variables['action']
    variableDef.setProperties(description="""The last transition""",
                              default_value="""""",
                              default_expr="""transition/getId|nothing""",
                              for_catalog=0,
                              for_status=1,
                              update_always=1,
                              props=None)

    ## Worklists Initialization


    # WARNING: below protected section is deprecated.
    # Add a tagged value 'worklist' with the worklist name to your state(s) instead.

    ##code-section create-workflow-setup-method-footer #fill in your manual code here
    ##/code-section create-workflow-setup-method-footer



def createEnquiryFolder(self, id):
    """Create the workflow for EEAEnquiry.
    """

    ob = DCWorkflowDefinition(id)
    setupEnquiryFolder(self, ob)
    return ob

addWorkflowFactory(createEnquiryFolder,
                   id='EnquiryFolder',
                   title='EnquiryFolder')

##code-section create-workflow-module-footer #fill in your manual code here
##/code-section create-workflow-module-footer

