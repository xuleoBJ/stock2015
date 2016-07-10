# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import sys
import Cstock
import ConfigParser
import Ccomfunc 
import numpy as np
import datetime

reload(sys)

if __name__=="__main__":
   stockID="999999"
   curStock=Cstock.Stock(stockID)
   strMonth="07"
   lineWritedList=[]
   ## read stockIDList

   ## 统计涨幅区间、波动区间个数统计
   goalFilePath = "result.txt" 
   Ccomfunc.write2Text(goalFilePath,lineWritedList)
   os.startfile(goalFilePath)

 #  print getDateIndexLowestPoint(curStock,-100,-1)


