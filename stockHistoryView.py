# -*- coding: utf-8 -*-  
import os
import shutil
import time
import datetime
import sys
import Cstock
import Ccomfunc
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter  
import candleStickPlot

lineWrited=[]

## 输出股票阶段涨幅


if __name__=="__main__":
   
    startClock=time.clock() ##记录程序开始计算时间

    stockID="002302"
    strMDStart="07/05"
    strMDEnd="07/18"
    
    ##读取股票代码，存储在curStock里
    curStock=Cstock.Stock(stockID)
    

    ##输出文件名
    goalFilePath='result.txt'
    fileWrited=open(goalFilePath,'w')
    fileWrited.write(stockID+'\n')
    curStock.printHeadLineDateData()
    for strYear in [str(iYear) for iYear in range(2010,2017)]:
        indexList=[] 
        strDateStart = strYear + "/" + strMDStart
        strDateEnd = strYear + "/" + strMDEnd
        indexStart = Ccomfunc.getIndexByStrDate(curStock,strDateStart)
        indexEnd =  Ccomfunc.getIndexByStrDate(curStock,strDateEnd)
        indexList=range(indexStart,indexEnd)
        for i in indexList:
           curStock.printLineDateData(i) 
        print "-"*72
  

    
    for line in lineWrited:
        fileWrited.write(line+'\n')
    fileWrited.close()
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))



