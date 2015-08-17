#  -*- coding:utf-8 -*-
## 加密设计，选择日，周，月，年
## 读取配置文件的方式进行配置
## 加密机要读取机器码，算号服务。
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

##通过日期，超过日期，就退出
installDateStr=config.get("softInfor","installDate")
installDate=datetime.datetime.strptime(installDateStr, '%Y%m%d').date()
today = datetime.date.today()
print installDate,today
if installDate<today:
    print "软件已过期,请联系作者787687312，邮箱:787687312@qq.com,qq群:150040288"
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
