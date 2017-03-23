import urllib.request
from bs4 import BeautifulSoup

curHtlm = urllib.request.urlopen('https://www.zhihu.com/')
soup = BeautifulSoup(curHtlm.read(),"lxml")
## print(soup.prettify())
print (soup.title)
##print ( soup.find_all('a'))


