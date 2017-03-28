#!/usr/bin/env python

# !!! Cannot work. See the solution in search2.py.
# Traceback (most recent call last):
#   File "search1.py", line 19, in <module>
#     from pygeocoder import Geocoder
# ImportError: No module named pygeocoder

# Note: version copied from edition 3 of the book.
# Listing 1-1. Fetching a Longitude and Latitude
# Foundations of Python Network Programming, 2nd ed. - Chapter 1 - search1.py

# http://stackoverflow.com/questions/27292897/cannot-import-name-googlemaps
# Maybe the documentation is a little bit outdated: use Client instead of GoogleMaps
# >>> from googlemaps import Client
# >>> dir(Client)
# >>> help(Client)
#from googlemaps import GoogleMaps
#from googlemaps import Client

import urllib
import urllib2

from pygeocoder import Geocoder

#print GoogleMaps().address_to_latlng(address)
# https://googlemaps.github.io/google-maps-services-python/docs/2.2/

# Uses XX-Net/Lantern as the proxy
proxyServer="http://10.0.0.5"
proxyPort="8787"
proxy = urllib2.ProxyHandler({ 'http': proxyServer + ":" + proxyPort })
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
 
# This bit makes the function emulate a firefox request
# ...I really don't know if it is necessary
userAgent = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)"
headers = { 'User-Agent' : userAgent }
#values = { 's' : 'nothing' }
url = "https://maps.google.com/maps/api/geocode/json"

def find_geo_via_proxy(address):
    global vlaues
    values = {"address":  address}
    data = urllib.urlencode(values)
    urlReq = urllib2.Request(url, data, headers)
    req = urllib2.urlopen(urlReq)
    return(json.loads(req.read()))


if __name__ == '__main__':
    address = '207 N. Defiance St, Archbold, OH' 
    #print(Geocoder.geocode(address)[0].coordinates)
    print(find_geo_via_proxy(address))

