#  -*- coding:utf-8 -*-
## ������ƣ�ѡ���գ��ܣ��£���
## ��ȡ�����ļ��ķ�ʽ��������
## ���ܻ�Ҫ��ȡ�����룬��ŷ���
#Importing the modules
import os
import os
import ConfigParser
import time
import uuid
import base64

config = ConfigParser.ConfigParser()
config.read("config.ini")
userID= uuid.uuid1().hex[-12:]
config.set("user","userID",str(userID))
config.write(open("config.ini", "w"))

userID=config.get("user","userID")
print userID

password=config.get("user","password")

encodeStr=base64.encodestring(userID)
print encodeStr
print base64.decodestring(encodeStr)
if password!= base64.decodestring(encodeStr):
    print "not"
else:
    pass
