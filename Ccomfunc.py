# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import sys

##数据目录
dirData="C:\\new_dxzq_v6\\T0002\\export\\" 

def convertDateStr2Date(dateStr):
    split1=dateStr.split('/')
    return datetime.date(int(split1[0]),int(split1[1]),int(split1[2]))
import Cstock

reload(sys)
sys.setdefaultencoding('utf-8')

##计算按周期计算涨停幅度

##将2008/08/08转换成dateTime
def convertDateStr2Date(dateStr):
    split1=dateStr.split('/')
    return datetime.date(int(split1[0]),int(split1[1]),int(split1[2]))

##计算两个日期间的自然日个数
def calNatureDays(dateStr1,dateStr2):
    d1= convertDateStr2Date(dateStr1)
    d2= convertDateStr2Date(dateStr2)
    return (d1-d2).days

##计算两个交易日直接的涨幅indexDay是指数，例如-1就是最后一个交易日，interValDay是间隔数，-5就是交易日的前5天，
def calRiseRateInterval(curStock,indexDay,intervalDay):
	if curStock.priceClosedFList[indexDay-intervalDay]>0:
		return 100*(curStock.priceClosedFList[indexDay]-curStock.priceClosedFList[indexDay-intervalDay])/curStock.priceClosedFList[indexDay-intervalDay]
	else:
		return -999
	    
##计算最后一个交易日前，interValDay个交易日的比今天的涨幅，intervalDay=5，就是交易日的前5天，
def calTrend(curStock,intervalDay):
	if curStock.priceClosedFList[-1-intervalDay]>0:
		return calRiseRateInterval(curStock,-1,intervalDay)
#		return 100*(curStock.priceClosedFList[-1]-curStock.priceClosedFList[-1-days])/curStock.priceClosedFList[-1-days]
	else:
		return -999
##输出交易日的差额
def printCalTrend(curStock,intervalDay):
	print(str(intervalDay)+" days riseRate",str(round(calTrend(curStock,intervalDay),2))+"%")


def printInfor():
    print("\n"+"#"*80)
    print(u"1.股市有风险，股市有无穷的机会，股市需要耐心，股市态度要认真。")
    print(u"2.每次交易前要提醒自己，目前的市场环境是什么，牛市越早越好，熊市越晚买越好，最好是下午2:45以后再买。")
    print(u"3.万不可盘中频繁的把一只票扔了，马上去买另一只票！这是非常不好的行为，因为，你扔的票你觉得跌了，去追涨的，要么涨的会跌 要么跌的会涨，必须有时间差。")
    print("\n"+"#"*80)
    
if __name__=="__main__":
    printInfor()

    


