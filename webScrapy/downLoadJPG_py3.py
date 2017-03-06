import urllib.request
import random
import string
import os
from string import ascii_uppercase
from datetime import datetime

def randomword(length):
    return ''.join(random.choice(ascii_uppercase) for i in range(length))

strUrl="http://wx2.sinaimg.cn/large/47481d23gy1fdc3d0k561g20b40et1l8.gif"
response = urllib.request.urlopen(strUrl)
image = response.read()

# Now to generate a random string of length 10
strFileName = randomword(6)
strFileExtension = os.path.splitext(strUrl)[1]

strToday = datetime.now().strftime("%Y%m%d")
strPath = "e:/webScrapy/"+strToday

if not os.path.exists(strPath):
    os.makedirs(strPath)

strFilePath=os.path.join(strPath, strFileName+strFileExtension)
with open(strFilePath,'wb') as f:
    f.write(image)
