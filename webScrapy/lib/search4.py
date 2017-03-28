#!/usr/bin/env python

# Listing 1-4. Talking to Google Maps Through a Bare Socket
# Foundations of Python Network Programming - Chapter 1 - search4.py

# A Python proxy
# socks.py: http://socksipy.sourceforge.net/
# Using SocksiPy to establish a connection thorough a proxy takes exactly 4 lines.
# Here is an example:
# import socks
# s = socks.socksocket()
# s.setproxy(socks.PROXY_TYPE_SOCKS5, "socks.example.com")
# s.connect(("www.example.com", 80))

import os
import sys
#import socket
import json

# Loads the lib path, where the SocksiPy file socks.py resides
current_path = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.join(current_path, os.pardir))
lib_path = os.path.join(root_path, 'lib')
sys.path.append(lib_path)

import socks

# This bit makes the function emulate a firefox request
# ...I really don't know if it is necessary.
userAgent = ("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8)"
                  "Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")

def main():
    """Have to use a proxy to overcome the GFW"""
    #sock = socket.socket() # Cannot work without a proxy
    #socks.set_default_proxy(socks.PROXY_TYPE_HTTP, "127.0.0.1", 8087) # ?No
    socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9002) # SS, OK    
    sock = socks.socksocket()
    #sock.setproxy(socks.PROXY_TYPE_HTTP, "10.0.0.4", 8787) # ?No
    
    sock.connect(('maps.google.com', 80))
    sock.sendall(
        'GET /maps/api/geocode/json?language=&region=&bounds=&components='
        '&address=207+N.+Defiance+St%2C+Archbold%2C+OH&sensor=false HTTP/1.1\r\n'
        'Host: maps.google.com:80\r\n'
        'User-Agent: userAgent\r\n'
        'Connection: close\r\n'
        '\r\n')
    rawreply = sock.recv(4096)
    print(rawreply)
    # Cannot work
    reply = json.loads(rawreply)
    print(reply['results'][0]['geometry']['location'])

if __name__ == '__main__':
    main()

