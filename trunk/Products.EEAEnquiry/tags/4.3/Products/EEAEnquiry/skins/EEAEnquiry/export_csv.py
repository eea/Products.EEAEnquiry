## Script (Python) "export_csv"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Export to CSV
##
from Products.CMFCore.utils import getToolByName
request = container.REQUEST
RESPONSE =  request.RESPONSE

def updateEuropeDomain(email):
  #domain and subdomain updates
  email = email.replace('esc.eu.int', 'eesc.europa.eu')                     #esc.eu.int --> eesc.europa.eu
  email = email.replace('cec.eu.int', 'ec.europa.eu')                       #cec.eu.int --> ec.europa.eu

  #domain updates
  email = email.replace('eea.eu.int', 'eea.europa.eu')                      #eea.eu.int --> eea.europa.eu
  email = email.replace('ear.eu.int', 'ear.europa.eu')                      #ear.eu.int --> ear.europa.eu
  email = email.replace('europarl.eu.int', 'europarl.europa.eu')            #europarl.eu.int --> europarl.europa.eu
  email = email.replace('consilium.eu.int', 'consilium.europa.eu')          #consilium.eu.int --> consilium.europa.eu
  email = email.replace('cedefop.eu.int', 'cedefop.europa.eu')              #cedefop.eu.int --> cedefop.europa.eu
  email = email.replace('oami.eu.int', 'oami.europa.eu')                    #oami.eu.int --> oami.europa.eu
  email = email.replace('eurofound.eu.int', 'eurofound.europa.eu')          #eurofound.eu.int --> eurofound.europa.eu
  email = email.replace('etf.eu.int', 'etf.europa.eu')                      #etf.eu.int --> etf.europa.eu
  email = email.replace('efsa.eu.int', 'efsa.europa.eu')                    #efsa.eu.int --> efsa.europa.eu
  email = email.replace('emea.eu.int', 'emea.europa.eu')                    #emea.eu.int --> emea.europa.eu
  email = email.replace('osha.eu.int', 'osha.europa.eu')                    #osha.eu.int --> osha.europa.eu
  email = email.replace('emsa.eu.int', 'emsa.europa.eu')                    #emsa.eu.int --> emsa.europa.eu
  email = email.replace('nfp-bg.eionet.eu.int', 'nfp-bg.eionet.europa.eu')  #nfp-bg.eionet.eu.int --> nfp-bg.eionet.europa.eu
  return email

def removeIllegalChars(email):
  email = email.replace('\n','')
  email = email.replace('\r','')
  email = updateEuropeDomain(email)
  return email

def formatEmail(email):
  res = []
  l_separators = [',', ';']
  for k in l_separators:
    email = email.replace(k, ' ')
  [res.append(k) for k in email.split(' ') if k]
  return res

cat = getToolByName(container, 'portal_enquiry_catalog')
requestors = cat.searchResults( portal_type = 'EnquiryRequestor' )

#csv header
print "email,active,format"
for k in requestors:
  #row data
  req_title = k.getObject().title
  req_subscribed = k.getObject().subscribed
  req_format = 'html'
  #1/0 instead of True/False
  if req_subscribed:    req_subscribed = 1
  else:                 req_subscribed = 0

  #format data
  tmp_emails = []
  try:      req_title.sort()
  except:   tmp_emails.append(req_title)

  for k in tmp_emails:
    for email in formatEmail(k):
      #write to csv
      print '%s,%s,%s' % (removeIllegalChars(email), req_subscribed, req_format)

RESPONSE.setHeader('content-type', 'text/plain')
RESPONSE.setHeader('Content-Disposition', 'attachment;filename=export.csv')
return printed

