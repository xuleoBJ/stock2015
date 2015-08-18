## -*- coding: GBK -*-  
# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime

##数据目录
dirData="C:\\new_dxzq_v6\\T0002\\export\\" 

##读取指定代码List
class Stock:
    dateStrList=[]
    priceOpeningFList=[]
    priceCloseingFList=[]
    priceHighestFList=[]
    priceLowestFList=[]
    tradeVolumeFList=[] ##成交量
    turnOverFList=[]  ##成交额  注意有的数据没有成交金额 成交量又有送股除权的问题
    riseRateFList=[]  ##价格涨幅
    waveRateFList=[] ##波动涨幅
    riseOfTradeVolumeFList=[]  ##成交量涨幅
    riseOfTurnOverFList=[]  ##成交额涨幅
    def __init__(self,stockID):
        print("#"*80)
        stockDataFile=os.path.join(dirData,stockID+'.txt')
        if os.path.exists(stockDataFile):
            fileOpened=open(stockDataFile,'r')
            lineIndex=0
            for line in fileOpened.readlines():
                lineIndex=lineIndex+1
                splitLine=line.split()
                if lineIndex==1:
                    print(line)
                if line!="" and lineIndex>=3 and len(splitLine)>=5:
                    self.dateStrList.append(splitLine[0])
                    self.priceOpeningFList.append(float(splitLine[1]))
                    self.priceHighestFList.append(float(splitLine[2]))
                    self.priceLowestFList.append(float(splitLine[3]))
                    self.priceCloseingFList.append(float(splitLine[4]))
                    self.tradeVolumeFList.append(float(splitLine[5]))
                    self.turnOverFList.append(float(splitLine[6]))
                    ##计算涨幅
                    if len(self.priceCloseingFList)>=2 and self.priceCloseingFList[-1]>0:
                        self.riseRateFList.append(round(100*(self.priceCloseingFList[-1]-self.priceCloseingFList[-2])/self.priceCloseingFList[-1],2))
                        self.waveRateFList.append(round(100*(self.priceHighestFList[-1]-self.priceLowestFList[-2])/self.priceCloseingFList[-1],2))
                    else:
                        self.riseRateFList.append(0)
                        self.waveRateFList.append(0)
                    ##计算成交量涨幅
                    if len(self.tradeVolumeFList)>=2 and self.tradeVolumeFList[-1]>0:
                        self.riseOfTradeVolumeFList.append(round(100*(self.tradeVolumeFList[-1]-self.tradeVolumeFList[-2])/self.tradeVolumeFList[-1],2))
                    else:
                        self.riseOfTradeVolumeFList.append(0)
                        
                    if len(self.turnOverFList)>=2 and self.turnOverFList[-1]>0:
                        self.riseOfTurnOverFList.append(round(100*(self.turnOverFList[-1]-self.turnOverFList[-2])/self.turnOverFList[-1],2))
                    else:
                        self.riseOfTurnOverFList.append(0)
            fileOpened.close()
            print("数据读取完毕,数据开始日：\t"+self.dateStrList[0]+"\t数据结束日：\t"+self.dateStrList[-1])
        else:
            print(stockID+"数据不存在")


class StockSH:   
    shLineList=[]
    shDateStrList=[]
    shPriceOpeningFList=[]
    shPriceCloseingFList=[]
    shPriceHighestFList=[]
    shPriceLowestFList=[]
    shTradeVolumeFList=[]
    shTurnoverFList=[]
    shRiseRateFList=[]  ##涨幅
    shWaveRateFLst=[] ##波动涨幅
    def __init__(self):
        print("#"*80)
        print ("当前股票代码:"+"sh999999")
        stockDataFile=os.path.join("export",'999999.txt')
        fileOpened=open(stockDataFile,'r')
        lineIndex=0
        for line in fileOpened.readlines():
            lineIndex=lineIndex+1
            splitLine=line.split()
            if line!="" and lineIndex>=3 and len(splitLine)>=6:
                self.shLineList.append(line)
                self.shDateStrList.append(splitLine[0])
                self.shPriceOpeningFList.append(float(splitLine[1]))
                self.shPriceHighestFList.append(float(splitLine[2]))
                self.shPriceLowestFList.append(float(splitLine[3]))
                self.shPriceCloseingFList.append(float(splitLine[4]))
                self.shTradeVolumeFList.append(float(splitLine[5]))
                self.shTurnoverFList.append(float(splitLine[6]))
        fileOpened.close()
        print("上证数据读取完毕,数据开始日：\t"+self.shDateStrList[0]+"数据结束日：\t"+self.shDateStrList[-1])
if __name__=="__main__":
    print("\n"+"#"*80)
    print ("股市有风险，股市有无穷的机会，股市需要耐心，股市态度要认真。")
    print("\n"+"#"*80)
    
    startClock=time.clock() ##记录程序开始计算时间
    
    a=Stock('999999') 
    
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


