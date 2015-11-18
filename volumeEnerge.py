# -*- coding: UTF-8 -*-
import datetime
import lxml.etree as etree
import lxml.html
import ConfigParser
import time,sched,os,urllib2,re,string
import ctypes
from Cstock import Stock

def mymain():
    curStock=Stock('399001')
    shStock=Stock('999999')
    print (u"正在进行量能分析：")
    print shStock.stockID,shStock.stockName,shStock.dayStrList[-5:],shStock.dayRadioLinkOfTradeVolumeFList[-5:]
    print curStock.stockID,curStock.stockName,curStock.dayStrList[-5:],curStock.dayRadioLinkOfTradeVolumeFList[-5:]

if __name__ == "__main__":
    print (u"成交量反应了市场情绪。")
    shStock=Stock('999999')
    curStock=Stock('399001')
    mymain()



