# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
from datetime import timedelta
import sys
import Cstock
import ctypes 
# import ConfigParser




##数据目录字符串
src="C:\\new_dxzq_v6\\T0002\\export\\"
dirData="dataManage\\stockSelect"
dirHisData="dataManage\\hisData"

## 改变路径到工作目录 
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print (os.path.curdir)

resultDir="resultDir"
dirSyn = "E:\\我的坚果云\\2_数据分析\\"

if not os.path.exists(resultDir):
    os.makedirs(resultDir)


def defaultDateInput():
    now =  datetime.datetime.now()
    inputDate = now 
    if now.hour<15: ##时间小于下午3点 用昨日数据
        inputDate = now-timedelta(days=1)
    if now.hour<15 and now.isoweekday()==1: ##时间小于下午3点 且周一 用上周5数据
        inputDate = now-timedelta(days=3)
    if now.isoweekday()==6 or now.isoweekday()==7:  ##周六周日 <F5>用上周5数据
        inputDate = now-timedelta(days=now.isoweekday()-5)
    return inputDate

def defaultDateInputStr():
    return defaultDateInput().strftime("%Y/%m/%d")

##根据输入的股票ID，返回对应的stockMarktet
def getMarketStock(curStockID):
    marketID='999999'
    if not curStockID.startswith('6'):
        marketID='399001'
    curMarket=Cstock.Stock(marketID)
    return curMarket
    
##寻找最后一个匹配值 
def rindex(_list, _value):
    return len(_list) - _list[::-1].index(_value) - 1


##将2008/08/08转换成dateTime
def convertDateStr2Date(dateStr):
    split1=dateStr.split('/')
    return datetime.date(int(split1[0]),int(split1[1]),int(split1[2]))


## 根据dateStr返回最接近的index，有就返回最近的指数，超出，返回-1
def getIndexByStrDate(_curStock,_dateStr):
    if _dateStr=="":
        return -1
    dateInput=convertDateStr2Date(_dateStr)
    return getIndexByDate(_curStock,dateInput)

## 根据date返回最接近的index，有就返回最近的指数，超出，返回-1
def getIndexByDate(_curStock,dateInput):
    for i in range(0,_curStock.count-1):
        if _curStock.dateList[i]<=dateInput<_curStock.dateList[i+1]:
            return i
    if len(_curStock.dateList)>1 and _curStock.dateList[-1]==dateInput:
        return _curStock.count-1
    return -1

## 根据输入的date，返回每个月的1号
def first_day_of_month( inputDate ):
    return datetime.date( inputDate.year, inputDate.month, 1 )

## 根据输入的date，返回每个月的最后一天
def last_day_of_month( inputDate ):
    monthDays=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    curMonth = inputDate.month
    curYear = inputDate.year
    if curMonth==2 and curYear/4==0 and curYear/400!=0 :
        return datetime.date( inputDate.year, inputDate.month, 29 )
    else:
        return datetime.date( inputDate.year, inputDate.month, monthDays[curMonth-1] )

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
    print("-"*72)
    print(u"0.耐心，耐心，还是耐心!")
    print(u"1.交易计划，多看少动")
    print(u"2.减少频率，绝对安全，盈利模型！防守措施！操作逻辑！")
    print(u"3.永远不要补仓去摊薄成本，短线不能做成长线")
    print(u"4.交易侧重于时间，而不要重于价格。建议的交易时间为 10:30 11:30 1:45 2:45，希望严格遵守，参考15分钟K线，走平台价 不必要在乎分分毛毛。")
    print("-"*72)

def write2Text(goalFilePath,lineList):
    fileWrited=open(goalFilePath,'w')
    for line in lineList:
        fileWrited.write(line+'\n')
    fileWrited.close()
    print("-"*72)
    print(u"数据保存在{}".format(goalFilePath))

if __name__=="__main__":
    today=datetime.date.today()
    # print today
    # print monday_of_week(today)
    # print last_day_of_month(today)
    # print first_day_of_month(today)

