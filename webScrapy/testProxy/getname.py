#!/usr/bin/env python
# Listing 1-6. Turning a Hostname into an IP Address
# Foundations of Python Network Programming - Chapter 1 - getname.py

#import os
#import sys
import socket

# Loads the lib path, where the SocksiPy file socks.py resides
#current_path = os.path.dirname(os.path.abspath(__file__))
#root_path = os.path.abspath( os.path.join(current_path, os.pardir))
#lib_path = os.path.join(root_path, 'lib')
#sys.path.append(lib_path)
#import socks


def main():
    #socks.set_default_proxy(socks.PROXY_TYPE_HTTP, "127.0.0.1", 8787) # OK
    #sock = socks.socksocket()
    hostname = 'maps.google.com'
    addr = socket.gethostbyname(hostname)
    #addr = sock.gethostbyname(hostname)
    print('The address of %s is %s.' % (hostname, addr))


if __name__ == '__main__':
    main()

