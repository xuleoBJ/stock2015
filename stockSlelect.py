## -*- coding: GBK -*-  
# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import Cstock


##计算按周期计算涨停幅度

lineWrited=[]

def convertDateStr2Date(dateStr):
    split1=dateStr.split('/')
    return datetime.date(int(split1[0]),int(split1[1]),int(split1[2]))

if __name__=="__main__":
    print("\n"+"#"*80)
    print ("控制风险，保持耐心，态度认真。")
    print ("下跌过程永远不买票！企稳后再买卖！最好是尾盘15分钟买卖！要么就挂相对的低价单钓鱼。")
    print ("在历史K线中寻找有类似特征信息的日期，因为历史是重复的，错误也是循环的。")
    print("\n"+"#"*80)
    
    startClock=time.clock() ##记录程序开始计算时间
   

    stockIDList=[]
    sourceDirPath="export"
    fileNames=os.listdir(sourceDirPath)
    for fileItem in fileNames:
        stockIDList.append(os.path.splitext(fileItem)[0])
    
    ##输出文件名
    goalFilePath='result.txt'
    fileWrited=open(goalFilePath,'w')
    
    print ("正在根据条件筛选股票：")
    
    for stockID in stockIDList:
        ##读取股票代码，存储在curStock里
        curStock=Cstock.Stock(stockID)
        if curStock.riseRateFList[-3]<= curStock.riseRateFList[-2]<=curStock.riseRateFList[-1]<0 and curStock.priceCloseingFList[-3]>curStock.priceCloseingFList[-2]>curStock.priceCloseingFList[-1]:
               if curStock.tradeVolumeFList[-3]>curStock.tradeVolumeFList[i-2]>curStock.tradeVolumeFList[-1]: ## 成交量
                print(stockID)
                fileWrited.write(stockID+'\n')
    fileWrited.close()
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


