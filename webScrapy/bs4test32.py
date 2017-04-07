import urllib.request
from bs4 import BeautifulSoup

curHtlm = urllib.request.urlopen('http://www.ximalaya.com/33943825/index_tracks?page=3')
soup = BeautifulSoup(curHtlm.read(),"lxml")
## print(soup.prettify())
print (soup.title)
##print ( soup.find_all('a'))


