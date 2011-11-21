""" Browser views
"""
from Products.Five import BrowserView as FiveBrowserView
from Products.CMFCore.utils import getToolByName
from AccessControl.SecurityManagement import newSecurityManager
from AccessControl.SecurityManagement import setSecurityManager
from AccessControl import getSecurityManager, SpecialUsers

def ownerOfObject(obj):
    """Provides acl_user acquisition wrapped owner of object"""
    udb, uid = obj.getOwnerTuple()
    root = obj.getPhysicalRoot()
    udb = root.unrestrictedTraverse(udb, None)
    if udb is None:
        user = SpecialUsers.nobody
    else:
        user = udb.getUserById(uid, None)
        if user is None:
            user = SpecialUsers.nobody
        else:
            user = user.__of__(udb)
    return user


#TODO: this is deprecated, not needed anymre
class BrowserView(FiveBrowserView):
    """ View
    """
    def _getContext(self):
        """ Context getter
        """
        return self._context[0]

    def _setContext(self, value):
        """ Context setter
        """
        self._context = [value]
    context = property(_getContext, _setContext)


class SendEnquiry(BrowserView):
    """ Send enquiry
    """
    def sendUnsentEnquiries(self):
        """ Send
        """
        context = self.context
        workflow = getToolByName(context, 'portal_workflow')
        enquiries = self.context.getEnquiries()
        for enq in enquiries:
            if workflow.getInfoFor(enq, 'review_state') == 'submitted':
                workflow.doActionFor(enq, 'send')
        return self.request.response.redirect(
            context.absolute_url() + '/enquiry_sent_confirmation')

    def subscribePloneGazette(self):
        """ Subscribe
        """
        subscriber = self.context
        subscriber_id = subscriber.id
        subscriber_email = subscriber.title
        REQUEST = self.context.REQUEST
        cat = getToolByName(subscriber, 'portal_catalog')
        newsletter_themes = cat.searchResults(portal_type='NewsletterTheme')

        for nt in newsletter_themes:
            #TODO: to be setup for multiple 'NewsletterTheme' instances case
            nt_ob = nt.getObject()
            nt_subscriber = None

            oldSecurityManager = getSecurityManager()
            newSecurityManager(REQUEST, ownerOfObject(nt_ob))
            if subscriber.subscribed:
                if nt_ob.alreadySubscriber(subscriber_email):
                    if nt_ob.alreadySubscriber(subscriber_email):
                        nt_subscriber = nt_ob.getSubscriberById(subscriber_id)
                    if nt_subscriber is not None:
                        nt_subscriber.edit(format='HTML',
                        active=subscriber.subscribed, email=subscriber_email)
                else:
                    newId = nt_ob._getRandomIdForSubscriber()
                    nt_subscriber = nt_ob.createSubscriberObject(newId)
                    nt_subscriber.edit(format='HTML',
                        active=subscriber.subscribed, email=subscriber_email)
                    nt_ob._subscribersCount += 1
            else:
                if nt_ob.alreadySubscriber(subscriber_email):
                    nt_subscriber = nt_ob.getSubscriberById(subscriber_id)
                if nt_subscriber is not None:
                    nt_ob.unSubscribe(nt_subscriber.id)
            setSecurityManager(oldSecurityManager)


class SubmitEnquiry(BrowserView):
    """ Submit
    """
    def hasCanceled(self):
        """ Canceled?
        """
        if self.request.get('portal_status_message'
                            ) == 'Add New Item operation was cancelled.':
            return True
        return False

    def getErrors(self):
        """ Errors
        """
        errors = {}
        context = self.context
        if self.request.get('login', None) is not None:
            email = self.request.get('email' , '')
            password = self.request.get('password' , '')
            if email == '':
                errors['email'] = 'Please enter your email address.'
            if password == '':
                errors['password'] = ("Please enter your password, "
                                      "if you have forgotten your password "
                                      "press 'please send my password'")
            if email != '' and password != '':
                cat = getToolByName(context, 'portal_enquiry_catalog')
                requestors = cat.searchResults(
                    portal_type='EnquiryRequestor', Title=email)
                for req in requestors:
                    obj = req.getObject()
                    if obj.getPassword() == password:
                        return {}
                return  {'email' : 'Password or email did not match',
                         'password' : 'Password or email did not match'}

        return errors

    def enquiryStep2(self):
        """ Step 2
        """
        context = self.context
        enquiry = context.UID()
        email = context.getEmail()
        password = self.request.get('password' , '')
        cat = getToolByName(context, 'portal_enquiry_catalog')
        requestors = cat.searchResults(
                portal_type='EnquiryRequestor',
                Title=email
                )

        if len(requestors) == 0:
            folder = context.aq_inner.aq_parent.objectValues(
                'EnquiryRequestorFolder')[0]
            reqObj = getattr(folder, enquiry)
            if reqObj is None or reqObj.portal_type != 'EnquiryRequestor':
                reqId = folder.invokeFactory(type_name='EnquiryRequestor',
                                             id=enquiry, title='')
                reqObj = getattr(folder, reqId)
                reqObj.setTitle(email)

            self._connectRequestorAndEnquiry(reqObj, enquiry)
            return self.request.response.redirect(
                reqObj.absolute_url() + '/edit')

        if self.request.get('login', None) is not None:
            for req in requestors:
                obj = req.getObject()
                if obj.getPassword() == password:
                    self._connectRequestorAndEnquiry(obj, enquiry)
                    return self.request.response.redirect(
                        obj.absolute_url() + '/edit?enquiry=%s' % enquiry)

        if self.request.get('mailpassword', None) is not None:
            email = self.request.get('email')
            requestors = cat.searchResults(portal_type='EnquiryRequestor',
                                            Title=email)
            if len(requestors) > 0:
                password = requestors[0].getObject().getPassword()
                mail_text = context.enquiry_mail_password_template(
                    context,
                    self.request,
                    email=email,
                    password=password,
                    enquiryUrl=context.absolute_url()
                )

                host = context.MailHost
                host.send(mail_text)
                return self.request.response.redirect(
                    context.absolute_url() + '/mail_password_response')

    def _connectRequestorAndEnquiry(self, requestor, enquiryUID):
        """ Connect
        """
        cat = getToolByName(self.context, 'reference_catalog')
        enqObj = cat.lookupObject(enquiryUID)
        enquiries = requestor.getEnquiries()
        enquiries.append(enqObj)
        requestor.setEnquiries(enquiries)
        enqObj.setEnquiryRequestor(requestor)
        wf = getToolByName(self.context, 'portal_workflow')
        if wf.getInfoFor(enqObj, 'review_state') == 'new':
            wf.doActionFor(enqObj, 'submit')

    def canView(self):
        """ Can view?
        """
        context = self.context

        mb = getToolByName(context, 'portal_membership')
        if 'Manager' in mb.getAuthenticatedMember().getRoles():
            return True

        wf = getToolByName(context, 'portal_workflow')
        state = wf.getInfoFor(context, 'review_state')
        if state == 'open':
            if context.getEnquiryrequestors() is None:
                pass
            else:
                pass
                # already submitted
                # state should be other

        return False


class EnquiryRequestor(BrowserView):
    """ Requestor
    """
    def canView(self):
        """ Can view?
        """
        context = self.context
        if context.checkCreationFlag():
            return True

        mb = getToolByName(context, 'portal_membership')
        if 'Manager' in mb.getAuthenticatedMember().getRoles():
            return True

        email = self.request.get('email' , None)
        password = self.request.get('password' , None)
        if context.getPassword() == password and context.Title() == email:
            return True

        enquiry = self.request.get('enquiry' , '')
        for enq in context.getEnquiries():
            if enq.UID() == enquiry:
                return True

        return False

    def getUnsentEnquiry(self):
        """ Unsent
        """
        context = self.context
        wf = getToolByName(context, 'portal_workflow')
        enquiries = self.context.getEnquiries()
        for enq in enquiries:
            if wf.getInfoFor(enq, 'review_state') == 'submitted':
                return enq
        return None

    def getUserInfo(self, userid):
        """ User info
        """
        context = self.context

        cat = getToolByName(context, 'portal_enquiry_catalog')
        requestors = cat.searchResults(
            portal_type='EnquiryRequestor', Title=userid)
        if len(requestors) > 0:
            user = requestors[0].getObject()
            return  ('OperationSuccess', {'COUNTRYREGION': user.getRegion(),
                     'EMAIL': user.Title(),
                     'PHONENUMBER': user.getPhone(),
                     'STREETADDRESS': user.getAddress(),
                     'COUNTRY': user.getCountry(),
                     'FAXNUMBER': user.getFax(),
                     'ZIPCODE': user.getPostalcode(),
                     'FAMILYNAME': user.getLastname(),
                     'ORGANISATION': user.getOrg(),
                     'GENDER': user.getSex() == 'Mr' and 1 or 0,
                     'FIRSTNAME': user.getFirstname(),
                     'CITY': user.getCity() })

        return ('InvalidUser', 'No such user')
