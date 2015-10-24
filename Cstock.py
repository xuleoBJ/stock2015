## -*- coding: GBK -*-  
# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import Ccomfunc

##数据目录
dirData="C:\\new_dxzq_v6\\T0002\\export\\" 

##读取指定代码List
class Stock:
    stockID=""
    stockName=""
    dayStrList=[]          ##day日期，string
    dateList=[]             ##date日期，date格式
    dayPriceOpenFList=[]    ##day开盘价
    dayPriceClosedFList=[]     ##day收盘价
    dayPriceHighestFList=[]    ##day最高价
    dayPriceLowestFList=[]     ##day最低价
    dayTradeVolumeFList=[]     ##day成交量
    dayTurnOverFList=[]        ##day成交额  注意有的数据没有成交金额 成交量又有送股除权的问题
    dayRiseRateFList=[]        ##day价格涨幅
    dayWaveRateFList=[]        ##day波动涨幅
    dayOpenRateFList=[]	       ##day开盘幅度，主要分析高开、低开等
    dayOpenCloseRateFList=[]	##day收盘价和开盘价的波动幅度，主要分析高开低走，低开高走等趋势
    dayRiseOfTradeVolumeFList=[]  ##day成交量涨幅
    dayRiseOfTurnOverFList=[]  ##day成交额涨幅

    dayPriceAverageFList=[]     ##日均价
    day3PriceAverageFList=[]     ##3日均价
    day5PriceAverageFList=[]     ##5日均价
    day10PriceAverageFList=[]     ##10日均价
    
    monthStrList=[]          ##月，string
    monthPriceOpenFList=[]    ##month开盘价
    monthPriceClosedFList=[]     ##month收盘价
    monthPriceHighestFList=[]    ##month最高价
    monthPriceLowestFList=[]     ##month最低价
    monthTradeVolumeFList=[]     ##month成交量
    monthTurnOverFList=[]        ##month成交额  注意有的数据没有成交金额 成交量又有送股除权的问题
    monthRiseRateFList=[]        ##month价格涨幅
    monthWaveRateFList=[]        ##month波动涨幅
    monthOpenRateFList=[]		##month开盘幅度，主要分析高开、低开等
    monthOpenCloseRateFList=[]	##month收盘价和开盘价的波动幅度，主要分析高开低走，低开高走等趋势
    monthRiseOfTradeVolumeFList=[]  ##month成交量涨幅
    monthRiseOfTurnOverFList=[]  ##month成交额涨幅
    def __init__(self,stockID):
        print("#"*80)
        del self.dayStrList[:]
        del self.dateList[:]
        del self.dayPriceOpenFList[:]
        del self.dayPriceClosedFList[:]
        del self.dayPriceHighestFList[:]
        del self.dayPriceLowestFList[:]
        del self.dayTradeVolumeFList[:]
        del self.dayTurnOverFList[:]
        del self.dayRiseRateFList[:]
        del self.dayWaveRateFList[:]
        del self.dayOpenRateFList[:]
        del self.dayOpenCloseRateFList[:]
        del self.dayRiseOfTradeVolumeFList[:]
        del self.dayRiseOfTurnOverFList[:]
        
        del self.monthStrList[:]
        del self.monthPriceOpenFList[:]
        del self.monthPriceClosedFList[:]
        del self.monthPriceHighestFList[:]
        del self.monthPriceLowestFList[:]
        del self.monthTradeVolumeFList[:]
        del self.monthTurnOverFList[:]
        del self.monthRiseRateFList[:]
        del self.monthWaveRateFList[:]
        del self.monthOpenRateFList[:]
        del self.monthOpenCloseRateFList[:]
        del self.monthRiseOfTradeVolumeFList[:]
        del self.monthRiseOfTurnOverFList[:]
        
        stockDataFile=os.path.join(dirData,stockID+'.txt')
        if os.path.exists(stockDataFile):
            fileOpened=open(stockDataFile,'r')
            ##从文件中读取日数据，并计算构造相关的日数据
            lineIndex=0
            for line in fileOpened.readlines():
                lineIndex=lineIndex+1
                splitLine=line.split()
                if lineIndex==1:
                    self.stockID=splitLine[0]
                    self.stockName=splitLine[1]
                    print(line)
                if line!="" and lineIndex>=3 and len(splitLine)>=5:
                    self.dayStrList.append(splitLine[0])
                    self.dateList.append(Ccomfunc.convertDateStr2Date(splitLine[0]))
                    
                    self.dayPriceOpenFList.append(float(splitLine[1]))
                    self.dayPriceHighestFList.append(float(splitLine[2]))
                    self.dayPriceLowestFList.append(float(splitLine[3]))
                    self.dayPriceClosedFList.append(float(splitLine[4]))
                    tradeVolume=float(splitLine[5])
                    self.dayTradeVolumeFList.append(tradeVolume)
                    turnOver=float(splitLine[6])
                    self.dayTurnOverFList.append(turnOver)
                    
                    ##计算均价
                    if(tradeVolume>0):
                        self.dayPriceAverageFList.append(round(turnOver/tradeVolume,2))
                    else:
                        self.dayPriceAverageFList.append(-999)

                    
                    ##计算涨幅和振幅
                    if len(self.dayPriceClosedFList)>=2 and self.dayPriceClosedFList[-2]>0:
						##(当日收盘-上日收盘)/上一日收盘
                        self.dayRiseRateFList.append(round(100*(self.dayPriceClosedFList[-1]-self.dayPriceClosedFList[-2])/self.dayPriceClosedFList[-2],2))
						##(当日最高-当日最低)/上一日收盘
                        self.dayWaveRateFList.append(round(100*(self.dayPriceHighestFList[-1]-self.dayPriceLowestFList[-1])/self.dayPriceClosedFList[-2],2))
						##(当日开盘-上日收盘)/上一日收盘
                        self.dayOpenRateFList.append(round(100*(self.dayPriceOpenFList[-1]-self.dayPriceClosedFList[-2])/self.dayPriceClosedFList[-2],2))
						##(当日收盘-当日开盘)/上一日收盘
                        self.dayOpenCloseRateFList.append(round(100*(self.dayPriceClosedFList[-1]-self.dayPriceOpenFList[-1])/self.dayPriceClosedFList[-2],2))
                    else:
                        self.dayRiseRateFList.append(-999)
                        self.dayWaveRateFList.append(-999)
                        self.dayOpenRateFList.append(-999)
                        self.dayOpenCloseRateFList.append(-999)
                    ##计算成交量涨幅
                    if len(self.dayTradeVolumeFList)>=2 and self.dayTradeVolumeFList[-2]>0:
                        self.dayRiseOfTradeVolumeFList.append(round(100*(self.dayTradeVolumeFList[-1]-self.dayTradeVolumeFList[-2])/self.dayTradeVolumeFList[-2],2))
                    else:
                        self.dayRiseOfTradeVolumeFList.append(-999)
                        
                    if len(self.dayTurnOverFList)>=2 and self.dayTurnOverFList[-2]>100:
                        self.dayRiseOfTurnOverFList.append(round(100*(self.dayTurnOverFList[-1]-self.dayTurnOverFList[-2])/self.dayTurnOverFList[-2],2))
                    else:
                        self.dayRiseOfTurnOverFList.append(-999)
            fileOpened.close()
            
            ##从日数据构造月度分析数据
            ##为了得到月度数据统计结果，把dateList分片的指数按年月存储在元组里
            indexYearMonthList=[]  ##定义一个List 存储 按月度分离的指数，存元组（年，月，在dateList起始下标，在dateList结束下标）
            indexStart=0
            for i in range(1,len(self.dateList)):
                itemCur = self.dateList[i]
                itemBefore=self.dateList[i-1]
                if  itemCur.month!=itemBefore.month or itemCur.year!=itemBefore.year:
                    dictIndex={}
                    dictIndex["year"]=itemBefore.year
                    dictIndex["month"]=itemBefore.month
                    dictIndex["indexStart"]=indexStart
                    dictIndex["indexEnd"]=i-1
                    indexYearMonthList.append(dictIndex)
                    indexStart=i
                if i==len(self.dateList)-1:
                    dictIndex={}
                    dictIndex["year"]=itemCur.year
                    dictIndex["month"]=itemCur.month
                    dictIndex["indexStart"]=indexStart
                    dictIndex["indexEnd"]=i
                    indexYearMonthList.append(dictIndex)

            for item in indexYearMonthList:
#                print item  ##print dictIndex debug used
                self.monthStrList.append("{}{:02}".format(item["year"],item["month"]))
                self.monthPriceOpenFList.append(self.dayPriceOpenFList[item["indexStart"]])
                self.monthPriceClosedFList.append(self.dayPriceClosedFList[item["indexEnd"]])
                if item["indexEnd"]>item["indexStart"]: ##处理一个月只有1个交易日，导致indexStart==indexEnd==0
                    self.monthPriceHighestFList.append(max(self.dayPriceHighestFList[item["indexStart"]:item["indexEnd"]]))
                    self.monthPriceLowestFList.append(min(self.dayPriceLowestFList[item["indexStart"]:item["indexEnd"]]))
                    self.monthTradeVolumeFList.append(sum(self.dayTradeVolumeFList[item["indexStart"]:item["indexEnd"]]))
                    self.monthTurnOverFList.append(sum(self.dayTurnOverFList[item["indexStart"]:item["indexEnd"]]))
                else:
                    self.monthPriceHighestFList.append(self.dayPriceHighestFList[item["indexEnd"]])
                    self.monthPriceLowestFList.append(self.dayPriceLowestFList[item["indexEnd"]])
                    self.monthTradeVolumeFList.append(self.dayTradeVolumeFList[item["indexEnd"]])
                    self.monthTurnOverFList.append(self.dayTurnOverFList[item["indexEnd"]])

                ##计算月度涨幅和振幅
                if len(self.monthPriceClosedFList)>=2 and self.monthPriceClosedFList[-1]>0:
                    ##(当日收盘-上日收盘)/上一日收盘
                    self.monthRiseRateFList.append(round(100*(self.monthPriceClosedFList[-1]-self.monthPriceClosedFList[-2])/self.monthPriceClosedFList[-2],2))
                    ##(当日最高-当日最低)/上一日收盘
                    self.monthWaveRateFList.append(round(100*(self.monthPriceHighestFList[-1]-self.monthPriceLowestFList[-1])/self.monthPriceClosedFList[-2],2))
                    ##(当日开盘-上日收盘)/上一日收盘
                    self.monthOpenRateFList.append(round(100*(self.monthPriceOpenFList[-1]-self.monthPriceClosedFList[-2])/self.monthPriceClosedFList[-2],2))
                    ##(当日收盘-当日开盘)/上一日收盘
                    self.monthOpenCloseRateFList.append(round(100*(self.monthPriceClosedFList[-1]-self.monthPriceOpenFList[-1])/self.monthPriceClosedFList[-2],2))
                else:
                    self.monthRiseRateFList.append(-999)
                    self.monthWaveRateFList.append(-999)
                    self.monthOpenRateFList.append(-999)
                    self.monthOpenCloseRateFList.append(-999)
            if len(self.dayStrList)>0:
                print("数据读取完毕,数据开始日：\t"+self.dayStrList[0]+"\t数据结束日：\t"+self.dayStrList[-1])
            else:
                print("数据列为空")

        else:
            print(stockID+"数据不存在")

if __name__=="__main__":
    print("\n"+"#"*80)
    print ("股市有风险，股市有无穷的机会，股市需要耐心，股市态度要认真。")
    print("\n"+"#"*80)
    
    startClock=time.clock() ##记录程序开始计算时间
    
    curStock=Stock('601818')
    print curStock.monthStrList[-10:]
    print curStock.monthPriceOpenFList[-10:]
    print curStock.monthPriceClosedFList[-10:]
    print curStock.monthRiseRateFList[-10:]
    print curStock.monthPriceHighestFList[-10:]
    print curStock.monthPriceLowestFList[-10:]
    print curStock.dayStrList[-10:]
    print curStock.dateList[-10:]
    print curStock.dayPriceClosedFList[-10:]
    print curStock.dayPriceHighestFList[-10:]
    print curStock.dayPriceLowestFList[-10:]
    print curStock.dayRiseRateFList[-10:]
    print curStock.dayWaveRateFList[-10:]
    print curStock.dayOpenRateFList[-10:]
    print curStock.dayOpenCloseRateFList[-10:]
    print curStock.dayPriceAverageFList[-10:]
    
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


