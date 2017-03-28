#!/usr/bin/env python

# Works by using XX-Net as a proxy
# Listing 1-3. Making a Raw HTTP Connection to Google Maps
# Foundations of Python Network Programming - Chapter 1 - search3.py

import httplib

try:
    import json
except ImportError: # for Python 2.5
    import simplejson as json

def get_location():
    #path = ('/maps/geo?q=207+N.+Defiance+St%2C+Archbold%2C+OH'
    #'&output=json&oe=utf8') # not supported now

    # The line continuation with backslashes
    #path = '/maps/api/geocode/json?language=&region=&bounds=&components=' + \
    #       '&address=207+N.+Defiance+St%2C+Archbold%2C+OH&sensor=false'

    # The preferred line continuation
    path = (
        '/maps/api/geocode/json?language=&region=&bounds=&components=' 
        '&address=207+N.+Defiance+St%2C+Archbold%2C+OH&sensor=false'
    )
    #print("path = %s" % path)
    
    # The direct access cannot work,
    #connection = httplib.HTTPConnection('maps.google.com')
    # Use XX-Net as the proxy, instead.
    connection = httplib.HTTPConnection("127.0.0.1", "8087")
    connection.request('GET', "http://maps.google.com" + path)
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply)
    #print(reply['Placemark'][0]['Point']['coordinates'][:-1]) # cannot work
    print(reply['results'][0]['geometry']['location'])

if __name__ == '__main__':
    get_location()
