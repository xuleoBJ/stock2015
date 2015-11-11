# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import Ccomfunc
import numpy as np
import Cstock

if __name__=="__main__":
    
    print("\n"+"#"*80)
    
    startClock=time.clock() ##��¼����ʼ����ʱ��
    
    curStock=Cstock.Stock('002001')
    
    print ("��T�۸���㣬��t�����ɴ������������ķ�����")
    arrayDayPriceLowest=np.array(curStock.dayPriceLowestFList)

    print(arrayDayPriceLowest[-5:])
    print(arrayDayPriceLowest[-5:].mean())
    
    print ("�ϸ��ִ��ֹ�𷽰���")
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


