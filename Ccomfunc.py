# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import sys
import Cstock
import Tkinter
import ctypes 

reload(sys)
sys.setdefaultencoding('utf-8')


##数据目录
dirData="C:\\new_dxzq_v6\\T0002\\export\\" 


##将2008/08/08转换成dateTime
def convertDateStr2Date(dateStr):
    split1=dateStr.split('/')
    return datetime.date(int(split1[0]),int(split1[1]),int(split1[2]))

##计算两个日期间的自然日个数
def calNatureDays(dateStr1,dateStr2):
    d1= convertDateStr2Date(dateStr1)
    d2= convertDateStr2Date(dateStr2)
    return (d1-d2).days

##计算两个交易日直接的涨幅indexOfDate是指数，例如-1就是最后一个交易日，interValDay是间隔数，-5就是交易日的前5天与今天的涨幅，+3 就是三日后比今天的涨幅，
def calRiseRateInterval(curStock,indexOfDate,intervalDay):
	if indexOfDate+intervalDay<len(curStock.dayPriceClosedFList) and curStock.dayPriceClosedFList[indexOfDate+intervalDay]>0:
            if intervalDay>0: ##后推
                return 100*(curStock.dayPriceClosedFList[indexOfDate+intervalDay]-curStock.dayPriceClosedFList[indexOfDate])/curStock.dayPriceClosedFList[indexOfDate]
            else:    ##前推 
                return 100*(curStock.dayPriceClosedFList[indexOfDate]-curStock.dayPriceClosedFList[indexOfDate+intervalDay])/curStock.dayPriceClosedFList[indexOfDate+intervalDay]
	else:
		return -999
	    
##计算最后一个交易日，interValDay个交易日的比今天的涨幅，interValDay是间隔数，-5就是交易日的前5天与今天的涨幅，+3 就是三日后比今天的涨幅，
def calTrend(curStock,intervalDay):
    if intervalDay<0:
        return 100*(curStock.dayPriceClosedFList[-1]-curStock.dayPriceClosedFList[-1+intervalDay])/curStock.dayPriceClosedFList[-1+intervalDay]
    else:
		return -999
##输出交易日的差额
def printCalTrend(curStock,intervalDay):
    print(str(intervalDay)+u"个交易日日累计涨幅:"+str(round(calTrend(curStock,intervalDay),2))+"%")


def printInfor():
    ctypes.windll.user32.MessageBoxA(0, "0-patience 1-time,2-volume,3-price.Some money is not in my system.", "infor", 1)
    print("\n"+"#"*80)
    print(u"1.股市需要耐心")
    print(u"2.减少交易频率，每次交易前要提醒自己，目前的市场环境是什么，牛市越早越好，熊市越晚买越好，最好是下午2:45以后再买。")
    print(u"3.买卖交易之间必须有时间差！！！万不可盘中频繁的把一只票扔了，马上去买另一只票！买前想逻辑！")
    print(u"4.股市态度要认真,有的钱不去赚。")
    print(u"5.永远不要补仓去摊薄成本。")
    print("\n"+"#"*80)

def write2Text(goalFilePath,lineList):
    fileWrited=open(goalFilePath,'w')
    for line in lineList:
        fileWrited.write(line+'\n')
    fileWrited.close()


if __name__=="__main__":
    printInfor()

    


