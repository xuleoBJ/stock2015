#  -*- coding:utf-8 -*-
## ������ƣ�ѡ���գ��ܣ��£���
## ��ȡ�����ļ��ķ�ʽ��������
## ���ܻ�Ҫ��ȡ�����룬��ŷ���
#Importing the modules
import os,sys
import datetime
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

##ͨ�����ڣ��������ڣ����˳�
installDateStr=config.get("softInfor","installDate")
installDate=datetime.datetime.strptime(installDateStr, '%Y%m%d').date()
today = datetime.date.today()
print installDate,today
if installDate<today:
    print "����ѹ���,����ϵ����787687312������:787687312@qq.com,qqȺ:150040288"
    sys.exit()
else:
    print "ok"

password=config.get("user","password")

encodeStr=base64.encodestring(userID)
print encodeStr
print base64.decodestring(encodeStr)

if password!= base64.decodestring(encodeStr):
    print "not"
else:
    pass
