# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import sys
import Cstock
import ctypes 
import ConfigParser

reload(sys)
sys.setdefaultencoding('utf-8')


##数据目录字符串
src="C:\\new_dxzq_v6\\T0002\\export\\"
dirData="dataManage\\stockSelect"
dirHisData="dataManage\\hisData"

## 改变路径到工作目录 
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print os.path.curdir
resultDir="resultDir"
if not os.path.exists(resultDir):
    os.makedirs(resultDir)

##根据输入的股票ID，返回对应的stockMarktet
def getMarketStock(curStockID):
    marketID='999999'
    if not curStockID.startswith('6'):
        marketID='399001'
    curMarket=Cstock.Stock(marketID)
    curMarket.list2array()
    return curMarket
    
##寻找最后一个匹配值 
def rindex(_list, _value):
    return len(_list) - _list[::-1].index(_value) - 1


##将2008/08/08转换成dateTime
def convertDateStr2Date(dateStr):
    split1=dateStr.split('/')
    return datetime.date(int(split1[0]),int(split1[1]),int(split1[2]))


def findIndexByDayStr(_curStock,dayStr="2015/01/05"):
    if dayStr in _curStock.dayStrList:
        return _curStock.dayStrList.index(dayStr)
    else:
        return -1

## 根据dateStr返回最接近的index，有就返回最近的指数，超出，返回-1
def getIndexByStrdate(_curStock,_dateStr):
    dateInput=convertDateStr2Date(_dateStr)
    return getIndexByDate(_curStock,dateInput)

## 根据date返回最接近的index，有就返回最近的指数，超出，返回-1
def getIndexByDate(_curStock,dateInput):
    for i in range(0,len(_curStock.dateList)-1):
        if _curStock.dateList[i]<=dateInput<_curStock.dateList[i+1]:
            return i
    return -1

## 根据输入的date，返回每个月的1号
def first_day_of_month( inputDate ):
    return datetime.date( inputDate.year, inputDate.month, 1 )


## 根据输入的date，返回当周周1的日期
def monday_of_week( inputDate ):
    return  getDayOfWeek( inputDate , 1 )

## 根据输入的date，获得当周周几的日期，周1 用1，周5 用5
def getDayOfWeek( inputDate , weekday ):
    days = inputDate.isoweekday()
    return inputDate + datetime.timedelta( -days + weekday)

##计算两个日期间的自然日个数
def calNatureDays( dateStr1 , dateStr2 ):
    d1= convertDateStr2Date(dateStr1)
    d2= convertDateStr2Date(dateStr2)
    return (d1-d2).days



def printInfor():
    ctypes.windll.user32.MessageBoxA(0, "1-What's your trade plan today?\n2-Every Trade is a complete chance?\n3-0-patience 1-time,2-volume,3-price.\n4-Some money is not in my system.", "infor", 1)
    print("\n"+"#"*80)
    print(u"0.市场是我的好朋友。")
    print(u"1.朋友相处，需要耐心。")
    print(u"2.减少交易频率，每次交易前要提醒自己，确定性机会，最好是下午2:45以后再买。")
    print(u"3.买卖交易之间必须有时间差！！！万不可盘中频繁的把一只票扔了，马上去买另一只票！买前想逻辑！")
    print(u"4.股市态度要认真,有的钱不去赚。")
    print(u"5.永远不要补仓去摊薄成本。")
    print(u"6.普涨行情不适合追高，特别是行情好的时候，因为热点不突出。")
    print("\n"+"#"*80)

def write2Text(goalFilePath,lineList):
    fileWrited=open(goalFilePath,'w')
    for line in lineList:
        fileWrited.write(line+'\n')
    fileWrited.close()


if __name__=="__main__":
    today=datetime.date.today()
    print today
    print monday_of_week(today)

