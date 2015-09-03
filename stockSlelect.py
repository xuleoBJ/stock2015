# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import Cstock
import Ccomfunc

##计算按周期计算涨停幅度

lineWrited=[]

if __name__=="__main__":
   
    startClock=time.clock() ##记录程序开始计算时间
   

    stockIDList=[]
    
    fileNames=os.listdir(Ccomfunc.dirData)
    for fileItem in fileNames:
        ##根据字头选择文件 上证6 深圳 0 板块指8 创业板 3
        if os.path.basename(fileItem).startswith("8"):
            stockIDList.append(os.path.splitext(fileItem)[0])
    
    ##输出文件名
    goalFilePath='result.txt'
    fileWrited=open(goalFilePath,'w')
    
    print ("正在根据条件筛选股票：")
    ##分析板块指数月度数据的涨幅，进行股票板块筛选，这是周期性行情选择的一个主要方法

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


