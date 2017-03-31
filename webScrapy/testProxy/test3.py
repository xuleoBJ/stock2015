import socks
import socket
from urllib import request

socks.set_default_proxy(socks.SOCKS5, "localhost", 9002)
socket.socket = socks.socksocket
r = request.urlopen('http://www.dwnews.com')
print(r.read()) # check ips
