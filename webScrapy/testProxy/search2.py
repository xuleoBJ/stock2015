#!/usr/bin/env python

# Listing 1-2. Fetching a JSON Document from the Google Maps URL
# Foundations of Python Network Programming - Chapter 1 - search2.py

import urllib
import urllib2

try:
    import json
except ImportError: # for Python 2.5
    import simplejson as json

# The following 2 lines don't work!
#params = {'q': '207 N. Defiance St, Archbold, OH', \
#                  'output': 'json', 'oe': 'utf8'}
#url = 'http://maps.google.com/maps/geo?' + urllib.urlencode(params)

# Use these two lines instead.
params = {'language': '', 'region': '', 'bounds': '', 'components': '',
                  'address': '207 N. Defiance St, Archbold, OH',
                  'sensor': False}
url = 'http://maps.google.com/maps/api/geocode/json?' + \
         urllib.urlencode(params)
print("url = %s" % url)

# Have to use a proxy to access the Google map service (Either does!).
#proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8087'}) # XX-Net
proxy = urllib2.ProxyHandler({'socks5': '127.0.0.1:9002'}) # Lantern
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

rawreply = urllib2.urlopen(url).read()
reply = json.loads(rawreply)
#print reply['Placemark'][0]['Point']['coordinates'][:-1] # obsolete
print reply['results'][0]['geometry']['location']

