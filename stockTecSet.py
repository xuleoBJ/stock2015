# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import Ccomfunc
import numpy as np
import Cstock
import stockPatternRecognition

import scipy.optimize as optimize

def func(fData,a,b,c,d):
    return fData[0]*a+fData[1]*b+fData[2]*c + d

def main(curStock):
    
    marketID='999999'
    if not curStock.stockID.startswith('6'):
        marketID='399001'

    curMarket=Cstock.Stock(marketID)
   
    print ("��T�۸���㣬��t�����ɴ������������ķ�����һ��Ҫ�м۲�������롣��")
    
    ##����㣺��15����K�ߵ�֧��λ����T
    ##�����㣺5���ڸߵ㣬��������3���㡣
    ##����㣺������λ���ߴ����鲻�á�

## ���Ԥ�⵱�մ��̺ã��ý��ڸߵ��97%��Ϊ�����λ��
## Ԥ����̲��ã��ý��ڵ͵�97%��Ϊ��λ��

## �����һ��Ҫ ��������Ԥ�ڣ�������Ҫ����׼ 

    indexMax=len(curStock.dayStrList)
    dayRadioLinkPriceLowArray=np.zeros(indexMax)
    for i in range(1,indexMax):
        if curStock.dayPriceLowestArray[i-1]>0:
            dayRadioLinkPriceLowArray[i]=100*(curStock.dayPriceLowestArray[i]-curStock.dayPriceLowestArray[i-1])/curStock.dayPriceLowestArray[i-1]
#    print(dayRadioLinkPriceLowArray[-10:])
    
    
    ## ����ƥ������ȡ�����
    ##�������һ��ƥ���յ���ͼ۵��Ƿ�
    matchDateIndex=-1 ##ʶ���յ�ָ��
    stockPatternRecognition.patternRecByMarketAndStock(curMarket,curStock,matchDateIndex)
    listPatternRecBycurStock=stockPatternRecognition.patternRecByRiseRate(curStock,300,3,matchDateIndex)
#    print listPatternRecBycurStock
    findIndex=curStock.findIndexByDayStr("2012/05/21")
    scale= dayRadioLinkPriceLowArray[findIndex+1]
#    print "ƥ���մ˴�Ԥ��ͼ�{:.2f}".format(curStock.dayPriceLowestArray[-1]*(1+scale*0.01))
  

##��ϸ��������㷨
##����3�յ���ͼ�������ʽ��ϣ�����ѡ14��
    kPeriod=7 ##�������
    indexDateFit=-3
    ##Ҳ������np.vstack((x,y,z))���fData
    fData=np.array([curStock.dayPriceLowestArray[indexDateFit-2-kPeriod:indexDateFit-2],\
            curStock.dayPriceLowestArray[indexDateFit-1-kPeriod:indexDateFit-1],\
            curStock.dayPriceLowestArray[indexDateFit-kPeriod:indexDateFit]])
    guess = (0.3,0.4,0.3,0)
    params, pcov = optimize.curve_fit(func, fData,curStock.dayPriceLowestArray[-kPeriod:], guess)
    print(params)
    ##��ģʽʶ������ڣ�Ѱ��ָ����Ȼ���ҳ����� 
    for indexDate in range(indexMax-kPeriod,indexMax-1):
        knum=3
        print("-"*72)
        print(curStock.dayStrList[indexDate-knum:indexDate])
        priceRiseRate3day=(curStock.dayRiseRateArray[indexDate-knum:indexDate]).mean()
        priceHigh3days=curStock.dayPriceHighestArray[indexDate-knum:indexDate].mean()
        priceClose3days=curStock.dayPriceClosedArray[indexDate-knum:indexDate].mean()
        priceLowFit=(curStock.dayPriceLowestArray[indexDate-knum:indexDate]*params[:3]).sum()+params[3]
        priceLow3days=curStock.dayPriceLowestArray[indexDate-knum:indexDate].mean()
        priceOpen3days=curStock.dayPriceOpenArray[indexDate-knum:indexDate].mean()
        priceWave3days=curStock.dayWaveRateArray[indexDate-knum:indexDate].mean()
        print("{}���Ƿ�ƽ��{:.2f}�����̾���{:.2f}���߾���{:.2f}���;���{:.2f}�����̾���{:.2f},ƽ������{:.2f}".format\
                (knum,priceRiseRate3day,priceOpen3days,priceHigh3days,priceLow3days,priceClose3days,priceWave3days))
        print("{}����ͼ�{:.2f}����߼�{:.2f}����С����{:.2f}".format\
                (knum,curStock.dayPriceLowestArray[indexDate-knum:indexDate].min(),\
                curStock.dayPriceHighestArray[indexDate-knum:indexDate].max(),\
                curStock.dayWaveRateArray[indexDate-knum:indexDate].min() \
                )\
                )

        priceTbuy=priceLowFit*0.5+priceLow3days*0.5
        priceTsell=priceTbuy*1.025
        printTStop=priceTbuy*0.975
        print("3��T-buy��{:.2f}���������{},T-sell��{:.2f}���������{},����ֹ��{:.2f},��������{}".format(\
                priceTbuy,curStock.dayPriceLowestArray[indexDate+1],\
                priceTsell,curStock.dayPriceHighestArray[indexDate+1],\
                printTStop,curStock.dayPriceClosedArray[indexDate+1])\
                )

    print("$"*72)
    priceTbuy=(curStock.dayPriceLowestArray[-3:]*params[:3]).sum()+params[3]
    priceTsell=priceTbuy*1.025
    printTStop=priceTbuy*0.975
    print("{}���̼�{},{}����ͼ�{:.2f}����߼�{:.2f}����С����{:.2f}".format\
                ( curStock.dayStrList[-1],curStock.dayPriceClosedArray[-1],\
                  knum,curStock.dayPriceLowestArray[-3:].min(), curStock.dayPriceHighestArray[-3:].max(),\
                curStock.dayWaveRateArray[-3:].min() \
                )\
        )
    print("3��T-buy��{:.2f}��T-sell��{:.2f},T-stop��{:.2f}".format(priceTbuy,priceTsell,printTStop))
    
    for period in [3,5,10]:
        indexHighPoint=curStock.dayPriceHighestFList.index(max(curStock.dayPriceHighestFList[-period:]))
        indexLowPoint=curStock.dayPriceLowestFList.index(min(curStock.dayPriceLowestFList[-period:]))
        priceHigh=curStock.dayPriceHighestFList[indexHighPoint]
        priceLow=curStock.dayPriceLowestFList[indexLowPoint]
        print("{}����ߵ�{}����������{},{}����͵�{}����������{}".format( \
                period,priceHigh,curStock.dayStrList[indexHighPoint], \
                period,priceLow,curStock.dayStrList[indexLowPoint]))
        print("%95buy: {:.2f},%93buy: {:.2f}".format(priceHigh*0.95,priceHigh*0.93))
    print("$"*72)

    for i in range(-3,0): ##ѭ��ָ����ʼ��ƥ��ָ����1
        weekDay=Ccomfunc.convertDateStr2Date(curStock.dayStrList[i]).isoweekday() 
        resultLine="{},����{}\t���̼�:{}\t�Ƿ�:{}\t���ܻ���:{}\t��������:{}".format(\
                curStock.dayStrList[i],weekDay,curStock.dayPriceClosedArray[i],curStock.dayRiseRateFList[i],\
                curStock.dayRadioLinkOfTradeVolumeFList[i],curStock.dayWaveRateFList[i])
        print resultLine
##��������
    if curStock.dayRadioLinkOfTradeVolumeArray[-1]>1 and curStock.dayRiseRateArray[-1]>0:
        print("�������ǡ�")
##��������
    if curStock.dayRadioLinkOfTradeVolumeArray[-1]<1 and curStock.dayRiseRateArray[-1]>0:
        print("�������ǡ�")
##�����µ�
    if curStock.dayRadioLinkOfTradeVolumeArray[-1]<1 and curStock.dayRiseRateArray[-1]<0:
        print("�����µ���")
##�����µ�
    if curStock.dayRadioLinkOfTradeVolumeArray[-1]<1 and curStock.dayRiseRateArray[-1]<0:
        print("�����µ���")
    
    marketMood=1
    if marketMood<=0.5:
        print("3��T����{:.2f}".format(priceLow3days*0.5+priceClose3days*0.5))



    ## ����-1.5���ϣ��������粻����T�������ʶȵ����������T�� 
    ## �����T�ļ۸���15����K�ߵ�֧�Ż���������λ��
    ## �����Ǽ��� ���Ҷ� �������ߡ� 
    


    ##��T�ļ۸��������2���� �������

    ## �������Ԥ�����鲻�ã����Բ��Ӳ������ɲ��� 
    ## ��TӦ�ø��ݿ��̼ۣ���������ɵ����ƹ�ϵ���������׵�����ע�Ᵽ�ֲ�λ�����Ǵ��̱��������У������ǵ�����
    ## �����к����е��жϣ���Ҫ��ϴ��̺͸�����������
    ## ���T���� ���߲�λ�����Ļ�������β��2��45������������ɲ�׬Ǯ��������Ǯ��
    ## ���Ʊ����ű��ǣ����˾��Ƿ��ˣ����ֿ�����Ҳ������ô��ġ�һ��Ҳ���ᷢ�����ء�����ƽ̯�˲�λ���ա������˶��١�

    
    print ("�ϸ��ִ��ֹ�𷽰���")

if __name__=="__main__":
    
    print("\n"+"#"*80)
    
    startClock=time.clock() ##��¼����ʼ����ʱ��
    for stockID in ["600178","002001"]:
        curStock=Cstock.Stock(stockID)
        curStock.list2array()
        main(curStock)
    
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
