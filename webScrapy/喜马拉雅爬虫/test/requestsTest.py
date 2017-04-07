import json
import re
import urllib.request
from bs4 import BeautifulSoup

import requests

def get_ids(urladdress):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0'}
   
    r = requests.get(urladdress,headers=headers)

    #print(str(r.status_code)+"\t"+urladdress)
    dataJson = r.json()
    stringHtml = dataJson["html"]
    soup = BeautifulSoup(stringHtml, 'lxml')
    inforList = soup.find_all("ul")
    idsList =[]
    for item in inforList:
        if item.has_attr("sound_ids"):
            sound_idsLine = item["sound_ids"]
            print(sound_idsLine)


if __name__ == '__main__':
    for i in range(1,22):
        urladdress = 'http://www.ximalaya.com/33943825/index_tracks?page='+str(i)
        get_ids(urladdress)

