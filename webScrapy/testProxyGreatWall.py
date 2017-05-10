##测试翻墙代理实现
import requests
import json
import random
from bs4 import BeautifulSoup
# resp = requests.get("http://tor1024.com/static/proxy_pool.txt")
# ips_txt = resp.text.strip().split("\n")
# ips = []
# for i in ips_txt:
#     try:
#         k = json.loads(i)
#         ips.append(k)
#     except Exception as e:
#         print(e)

http_proxy  = "http://127.0.0.1:9002"
https_proxy = "https://127.0.0.1:9002"
socks_proxy = "https://127.0.0.1:9002"

proxyDict = { 
              "http"  : http_proxy,
              "https" : https_proxy,
              "socks4" : socks_proxy,
              "socks5" : socks_proxy
            }
s = requests.Session()
##s.verify ="D:\\ca'"
r = s.get('http://www.nytimes.com/',proxies=proxyDict,verify=True,timeout=6)
print(r.status_code)
soup = BeautifulSoup(r.content, 'lxml')
inforList = soup.find_all('h3')
print (inforList)
for item in inforList:
    print(item.get_text())
