# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import Ccomfunc
import numpy as np

##根据StockID读入数据
class Stock:
    def list2array(self):
        self.dayPriceOpenArray=np.array(self.dayPriceOpenFList)    ##day开盘价array
        self.dayPriceClosedArray=np.array(self.dayPriceClosedFList)    ##day收盘价array
        self.dayPriceHighestArray=np.array(self.dayPriceHighestFList)    ##day最高价array
        self.dayPriceLowestArray=np.array(self.dayPriceLowestFList)     ##day最低array
        self.dayTradeVolumeArray=np.array(self.dayTradeVolumeFList)     ##day成交量array
        self.dayTurnOverArray=np.array(self.dayTurnOverFList)       ##day成交额  注意有的数据没有成交金额 成交量又有送股除权的问题array
        self.dayRiseRateCloseArray=np.array(self.dayRiseRateCloseFList)        ##day价格涨幅array
        self.dayRiseRateLowestArray=np.array(self.dayRiseRateLowestFList)        ##day最低价涨幅array
        self.dayRiseRateHighestArray=np.array(self.dayRiseRateHighestFList)        ##day最低价涨幅array
        self.dayWaveRateArray=np.array(self.dayWaveRateFList)       ##day波动涨幅array
        self.dayRiseRateOpenArray=np.array(self.dayRiseRateOpenFList)       ##day开盘幅度，主要分析高开、低开等array
        self.dayOpenCloseRateArray=np.array(self.dayOpenCloseRateFList)	##day收盘价和开盘价的波动幅度，主要分析高开低走，低开高走等趋势array
        self.dayRadioLinkOfTradeVolumeArray=np.array(self.dayRadioLinkOfTradeVolumeFList)  ##day成交量倍数价array
        
    ##构造均价数据
        self.day3PriceAverageArray=np.zeros(self.count)     ##3日均价
        self.day5PriceAverageArray=np.zeros(self.count)     ##5日均价
        self.day10PriceAverageArray=np.zeros(self.count)     ##10日均价
        self.day30PriceAverageArray=np.zeros(self.count)     ##30日均价
        self.day60PriceAverageArray=np.zeros(self.count)     ##60日均价
        for i in range(3,self.count):
            self.day3PriceAverageArray[i]= round(self.dayPriceClosedArray[i-3:i].mean(),2)
            if i>=5:
                self.day5PriceAverageArray[i] = round(self.dayPriceClosedArray[i-5:i].mean(),2)
            if i>=10:
                self.day10PriceAverageArray[i]= round(self.dayPriceClosedArray[i-10:i].mean(),2)
            if i>=30:
                self.day30PriceAverageArray[i]=round(self.dayPriceClosedArray[i-30:i].mean(),2)
            if i>=60:
                self.day60PriceAverageArray[i]=round(self.dayPriceClosedArray[i-60:i].mean(),2)

    ##构造均成交量数据
        self.day3TradeVolumeArray=np.zeros(self.count)     ##3日均价
        self.day5TradeVolumeArray=np.zeros(self.count)     ##5日均价
        self.day10TradeVolumeArray=np.zeros(self.count)     ##10日均价
        self.day20TradeVolumeArray=np.zeros(self.count)     ##20日均价
        self.day60TradeVolumeArray=np.zeros(self.count)     ##60日均价
        for i in range(3,self.count):
            self.day3TradeVolumeArray[i]= round(self.dayTradeVolumeArray[i-3:i].mean(),2)
            if i>=5:
                self.day5TradeVolumeArray[i] = round(self.dayTradeVolumeArray[i-5:i].mean(),2)
            if i>=10:
                self.day10TradeVolumeArray[i]= round(self.dayTradeVolumeArray[i-10:i].mean(),2)
            if i>=20:
                self.day20TradeVolumeArray[i]=round(self.dayTradeVolumeArray[i-20:i].mean(),2)
            if i>=60:
                self.day60TradeVolumeArray[i]=round(self.dayTradeVolumeArray[i-60:i].mean(),2)
    
    ##构造周级别数据
    def initWeekData(self):
        self.weekPriceOpenFList=[]       ##week开盘价
        self.weekPriceClosedFList=[]     ##week收盘价
        self.weekPriceHighestFList=[]    ##week最高价
        self.weekPriceLowestFList=[]     ##week最低价
        self.weekTradeVolumeFList=[]     ##week成交量
        self.weekTurnOverFList=[]        ##week成交额  注意有的数据没有成交金额 成交量又有送股除权的问题
        self.weekRiseRateFList=[]        ##week价格涨幅
        self.weekRiseRateLowestFList=[]        ##week价格涨幅
        self.weekRiseRateHighestFList=[]        ##week价格涨幅
        self.weekWaveRateFList=[]        ##week波动涨幅
        self.weekOpenRateFList=[]	       ##week开盘幅度，主要分析高开、低开等
        self.weekPriceAverageFList=[]     ##日均价
        self.weekOpenCloseRateFList=[]	##week收盘价和开盘价的波动幅度，主要分析高开低走，低开高走等趋势
        self.weekRadioLinkOfTradeVolumeFList=[]  ##week成交量倍数
        self.weekRiseOfTurnOverFList=[]  ##week成交额倍数
    
    ##构造月级别数据
    def initMonthData(self):
        self.monthStrList=[]          ##月，string
        self.monthPriceOpenFList=[]    ##month开盘价
        self.monthPriceClosedFList=[]     ##month收盘价
        self.monthPriceHighestFList=[]    ##month最高价
        self.monthPriceLowestFList=[]     ##month最低价
        self.monthTradeVolumeFList=[]     ##month成交量
        self.monthTurnOverFList=[]        ##month成交额  注意有的数据没有成交金额 成交量又有送股除权的问题
        self.monthRiseRateFList=[]        ##month价格涨幅
        self.monthWaveRateFList=[]        ##month波动涨幅
        self.monthOpenRateFList=[]		##month开盘幅度，主要分析高开、低开等
        self.monthOpenCloseRateFList=[]	##month收盘价和开盘价的波动幅度，主要分析高开低走，低开高走等趋势
        self.monthRiseOfTradeVolumeFList=[]  ##month成交量涨幅
        self.monthRiseOfTurnOverFList=[]  ##month成交额涨幅
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
            if len(self.monthPriceClosedFList)>=2 and self.monthPriceClosedFList[-2]>0:
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
    

    def printHeadLineDateData(self):
        wordList=[]
        wordList.append(u"日期(星期)")
        wordList.append(u"收盘价")
        wordList.append(u"收盘涨幅")
        wordList.append(u"开盘涨幅")
        wordList.append(u"最高涨幅")
        wordList.append(u"最低涨幅")
        headLine= "\t".join(wordList)
        print (headLine)
        return headLine

    def printLineDateData(self,indexDate):
        wordList=[]
        wordList.append(self.dayStrList[indexDate]+" "+str(self.weekDayList[indexDate]))
        wordList.append(str(self.dayPriceClosedFList[indexDate]))
        wordList.append(str(self.dayRiseRateCloseFList[indexDate]))
        wordList.append(str(self.dayRiseRateOpenFList[indexDate]))
        wordList.append(str(self.dayRiseRateHighestFList[indexDate]))
        wordList.append(str(self.dayRiseRateLowestFList[indexDate]))
        dataLine= "\t".join(wordList)
        print (dataLine)
        return dataLine

    def __init__(self,stockID,stockDirData="C:\\new_dxzq_v6\\T0002\\export\\"):
        self.stockName=""
        self.stockID=stockID
        self.count = 0
        print("-"*72)
        self.dayStrList=[]           ##day日期，string
        self.weekDayList=[]           ##day日期，string
        self.dateList=[]             ##date日期，date格式
        
        ##日级别
        self.dayPriceOpenFList=[]       ##day开盘价
        self.dayPriceClosedFList=[]     ##day收盘价
        self.dayPriceHighestFList=[]    ##day最高价
        self.dayPriceLowestFList=[]     ##day最低价
        self.dayTradeVolumeFList=[]     ##day成交量
        self.dayTurnOverFList=[]        ##day成交额  注意有的数据没有成交金额 成交量又有送股除权的问题
        self.dayRiseRateCloseFList=[]        ##day价格涨幅
        self.dayRiseRateLowestFList=[]        ##day价格涨幅
        self.dayRiseRateHighestFList=[]        ##day价格涨幅
        self.dayWaveRateFList=[]        ##day波动涨幅
        self.dayRiseRateOpenFList=[]	       ##day开盘幅度，主要分析高开、低开等
        self.dayOpenCloseRateFList=[]	##day收盘价和开盘价的波动幅度，主要分析高开低走，低开高走等趋势
        self.dayRadioLinkOfTradeVolumeFList=[]  ##day成交量倍数
        self.dayRiseOfTurnOverFList=[]  ##day成交额倍数
       
        stockDataFile=os.path.join(stockDirData,stockID+'.txt')

        if os.path.exists(stockDataFile):
            fileOpened=open(stockDataFile,'r')
            ##从文件中读取日数据，并计算构造相关的日数据
            lineIndex=0
            for line in fileOpened.readlines():
                lineIndex=lineIndex+1
                splitLine=line.split()
                if lineIndex==1: ## 第一行是文件头 
                    self.stockName=splitLine[1]
                    print ("{},{}".format(self.stockID,self.stockName))
                if line!="" and lineIndex>=5 and len(splitLine)>=5:  ## 第5行才是数据
                    self.dayStrList.append(splitLine[0])
                    curDate = Ccomfunc.convertDateStr2Date(self.dayStrList[-1])
                    curWeekDay = curDate.isoweekday()
                    self.dateList.append(curDate)
                    self.weekDayList.append(curWeekDay)
                    
                    self.dayPriceOpenFList.append(float(splitLine[1]))
                    self.dayPriceHighestFList.append(float(splitLine[2]))
                    self.dayPriceLowestFList.append(float(splitLine[3]))
                    self.dayPriceClosedFList.append(float(splitLine[4]))
                    tradeVolume=float(splitLine[5])
                    self.dayTradeVolumeFList.append(tradeVolume)
                    turnOver=float(splitLine[6])
                    self.dayTurnOverFList.append(turnOver)
                    
                    ##计算涨幅和振幅
                    if len(self.dayPriceClosedFList)>=2 and self.dayPriceClosedFList[-2]>0:
						##(当日收盘-上日收盘)/上一日收盘
                        self.dayRiseRateCloseFList.append(round(100*(self.dayPriceClosedFList[-1]-self.dayPriceClosedFList[-2])/self.dayPriceClosedFList[-2],2))
						##(当日最低-上日收盘)/上一日收盘
                        self.dayRiseRateLowestFList.append(round(100*(self.dayPriceLowestFList[-1]-self.dayPriceClosedFList[-2])/self.dayPriceClosedFList[-2],2))
						##(当日最高-上日收盘)/上一日收盘
                        self.dayRiseRateHighestFList.append(round(100*(self.dayPriceHighestFList[-1]-self.dayPriceClosedFList[-2])/self.dayPriceClosedFList[-2],2))
						##(当日最高-当日最低)/上一日收盘
                        self.dayWaveRateFList.append(round(100*(self.dayPriceHighestFList[-1]-self.dayPriceLowestFList[-1])/self.dayPriceClosedFList[-2],2))
						##(当日开盘-上日收盘)/上一日收盘
                        self.dayRiseRateOpenFList.append(round(100*(self.dayPriceOpenFList[-1]-self.dayPriceClosedFList[-2])/self.dayPriceClosedFList[-2],2))
						##(当日收盘-当日开盘)/上一日收盘
                        self.dayOpenCloseRateFList.append(round(100*(self.dayPriceClosedFList[-1]-self.dayPriceOpenFList[-1])/self.dayPriceClosedFList[-2],2))
                    else:
                        self.dayRiseRateOpenFList.append(-999)
                        self.dayRiseRateLowestFList.append(-999)
                        self.dayRiseRateHighestFList.append(-999)
                        self.dayRiseRateCloseFList.append(-999)
                        self.dayWaveRateFList.append(-999)
                        self.dayOpenCloseRateFList.append(-999)
                    ##计算成交量涨幅
                    if len(self.dayTradeVolumeFList)>=2 and self.dayTradeVolumeFList[-2]>0:
                        self.dayRadioLinkOfTradeVolumeFList.append(round(self.dayTradeVolumeFList[-1]/self.dayTradeVolumeFList[-2],2))
                    else:
                        self.dayRadioLinkOfTradeVolumeFList.append(-999)
                        
                    if len(self.dayTurnOverFList)>=2 and self.dayTurnOverFList[-2]>100:
                        self.dayRiseOfTurnOverFList.append(round(100*(self.dayTurnOverFList[-1]-self.dayTurnOverFList[-2])/self.dayTurnOverFList[-2],2))
                    else:
                        self.dayRiseOfTurnOverFList.append(-999)
            fileOpened.close()
            self.count=len(self.dayStrList)
            
            if len(self.dayStrList)>0:
                self.count=len(self.dayStrList)
                print("DateStart: "+self.dayStrList[0]+"\tDateEnd: "+self.dayStrList[-1]+ \
                        "\tPriceClosedLastDay: "+str(self.dayPriceClosedFList[-1]))
            else:
                print(u"数据列为空")
            
            self.list2array()

        else:
            print(stockID+"数据不存在")
    
##构造和输入数据统一时间的stock对象。
class StockUniDate:
    def __init__(self,stockID,inputStockDateStrList,stockDirData="C:\\new_dxzq_v6\\T0002\\export\\"):
        self.stockName=""
        self.stockID=stockID
        self.count = len(inputStockDateStrList)
        print("-"*72)
        self.dayStrList=inputStockDateStrList          ##day日期，string
        for i in range(self.count):
            self.dateList.append(Ccomfunc.convertDateStr2Date(self.dayStrList[i]))##date日期，date格式
        ##日级别
        self.dayPriceOpenArray=np.array(np.zeros(self.count))    ##day开盘价array
        self.dayPriceClosedArray=np.array(np.zeros(self.count))    ##day收盘价array
        self.dayPriceHighestArray=np.array(np.zeros(self.count))    ##day最高价array
        self.dayPriceLowestArray=np.array(np.zeros(self.count))     ##day最低array
        self.dayTradeVolumeArray=np.array(np.zeros(self.count))     ##day成交量array
        self.dayTurnOverArray=np.array(np.zeros(self.count))       ##day成交额  注意有的数据没有成交金额 成交量又有送股除权的问题array
        self.dayRiseRateCloseArray=np.array(np.zeros(self.count))        ##day价格涨幅array
        self.dayRiseRateLowestArray=np.array(np.zeros(self.count))        ##day最低价涨幅array
        self.dayRiseRateHighestArray=np.array(np.zeros(self.count))        ##day最低价涨幅array
        self.dayWaveRateArray=np.array(np.zeros(self.count))       ##day波动涨幅array
        self.dayRiseRateOpenArray=np.array(np.zeros(self.count))       ##day开盘幅度，主要分析高开、低开等array
        self.dayOpenCloseRateArray=np.array(np.zeros(self.count))	##day收盘价和开盘价的波动幅度，主要分析高开低走，低开高走等趋势array
        self.dayRadioLinkOfTradeVolumeArray=np.array(np.zeros(self.count))  ##day成交量倍数价array
        self.day3TradeVolumeArray=np.zeros(self.count)     ##3日均价
        self.day5TradeVolumeArray=np.zeros(self.count)     ##5日均价
        self.day10TradeVolumeArray=np.zeros(self.count)     ##10日均价
        self.day20TradeVolumeArray=np.zeros(self.count)     ##20日均价
        self.day60TradeVolumeArray=np.zeros(self.count)     ##60日均价
       
        stockDataFile=os.path.join(stockDirData,stockID+'.txt')

        if os.path.exists(stockDataFile):
            fileOpened=open(stockDataFile,'r')
            ##从文件中读取日数据，并计算构造相关的日数据
            lineIndex=0
            for line in fileOpened.readlines():
                lineIndex=lineIndex+1
                splitLine=line.split()
                if lineIndex==1:
                    self.stockName=splitLine[1]
                    print ("{},{}".format(self.stockID,self.stockName))
                if line!="" and lineIndex>=3 and len(splitLine)>=5:
                    indexOfdate = self.dayStrList.index(splitLine[0])
                    self.dayPriceOpenArray[indexOfdate] = float(splitLine[1])
                    self.dayPriceHighestArray[indexOfdate]=float(splitLine[2])
                    self.dayPriceLowestArray[indexOfdate]=float(splitLine[3])
                    self.dayPriceClosedArray[indexOfdate] = float(splitLine[4])
                    self.dayTradeVolumeArray[indexOfdate] = float(splitLine[5])
                    self.dayTurnOverArray[indexOfdate] = float(splitLine[6])
            fileOpened.close()
            
            if len(self.dayStrList)>0:
                self.count=len(self.dayStrList)
                print("DateStart: "+self.dayStrList[0]+"\tDateEnd: "+self.dayStrList[-1]+ \
                        "\tPriceClosedLastDay: "+str(self.dayPriceClosedFList[-1]))
            else:
                print(u"数据列为空")
            
        else:
            print(stockID+"数据不存在")

if __name__=="__main__":
    print("\n"+"#"*80)
    print(u"股市有风险，股市有无穷的机会，股市需要耐心，股市态度要认真。")
    print("\n"+"#"*80)
    
    startClock=time.clock() ##记录程序开始计算时间
    shStock=Stock('999999')
    shStock.printHeadLineDateData()
    for i in range(10,20):
        shStock.printLineDateData(i)
    print (shStock.dateList[-10:])
    
    
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


