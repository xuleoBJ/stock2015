# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import Ccomfunc
import numpy as np
import Cstock
import stockPatternRecognition
import configOS
import scipy.optimize as optimize
import math

def func(fData,a,b,c,d):
    return fData[0]*a+fData[1]*b+fData[2]*c + d

def historyPrint_optimize_curve_fit(cStock,countOfEle,kPeriod,params): 
    ##��ģʽʶ������ڣ�Ѱ��ָ����Ȼ���ҳ����� 
    for indexDate in range(countOfEle-kPeriod,countOfEle-1):
        knum=3
        print("-"*72)
        print(cStock.dayStrList[indexDate-knum:indexDate])
        priceRiseRate3day=(cStock.dayRiseRateArray[indexDate-knum:indexDate]).mean()
        priceHigh3days=cStock.dayPriceHighestArray[indexDate-knum:indexDate].mean()
        priceClose3days=cStock.dayPriceClosedArray[indexDate-knum:indexDate].mean()
        priceLowFit=(cStock.dayPriceLowestArray[indexDate-knum:indexDate]*params[:3]).sum()+params[3]
        priceLow3days=cStock.dayPriceLowestArray[indexDate-knum:indexDate].mean()
        priceOpen3days=cStock.dayPriceOpenArray[indexDate-knum:indexDate].mean()
        priceWave3days=cStock.dayWaveRateArray[indexDate-knum:indexDate].mean()
        print("{}���Ƿ�ƽ��{:.2f}�����̾���{:.2f}���߾���{:.2f}���;���{:.2f}�����̾���{:.2f},ƽ������{:.2f}".format\
                (knum,priceRiseRate3day,priceOpen3days,priceHigh3days,priceLow3days,priceClose3days,priceWave3days))
        print("{}����ͼ�{:.2f}����߼�{:.2f}����С����{:.2f}".format\
                (knum,cStock.dayPriceLowestArray[indexDate-knum:indexDate].min(),\
                cStock.dayPriceHighestArray[indexDate-knum:indexDate].max(),\
                cStock.dayWaveRateArray[indexDate-knum:indexDate].min() \
                )\
                )

        priceTbuy=priceLowFit*0.5+priceLow3days*0.5
        priceTsell=priceTbuy*1.025
        printTStop=priceTbuy*0.975
        print("���Ż�T-buy��{:.2f}���������{},T-sell��{:.2f}���������{},����ֹ��{:.2f},��������{}".format(\
                priceTbuy,cStock.dayPriceLowestArray[indexDate+1],\
                priceTsell,cStock.dayPriceHighestArray[indexDate+1],\
                printTStop,cStock.dayPriceClosedArray[indexDate+1])\
                )
def patternRecCalTPrice(cStock,dayRadioLinkPriceLowArray):
    curMarket=Ccomfunc.getMarketStock(cStock.stockID)
    matchDateIndex=-1 ##ʶ���յ�ָ��
    stockPatternRecognition.patternRecByMarketAndStock(curMarket,cStock,matchDateIndex)
    listPatternRecBycStock=stockPatternRecognition.patternRecByRiseRate(cStock,300,3,matchDateIndex)
#    print listPatternRecBycStock
    findIndex=cStock.findIndexByDayStr("2012/05/21")
    scale= dayRadioLinkPriceLowArray[findIndex+1]
    print "ƥ���մ˴�Ԥ��ͼ�{:.2f}".format(cStock.dayPriceLowestArray[-1]*(1+scale*0.01))

def outPutPriceRef(cStock):
    headWrited=[]
    wordWrited=[]
    for i in [3,5,8,13,21]:
        argsort=cStock.dayPriceLowestArray.argsort()
        headWrited.append("{}�յ�".format(i))
        headWrited.append("{}�ո�".format(i))
        wordWrited.append("{}".format(cStock.dayPriceLowestArray[-i:].min()))
        wordWrited.append("{}".format(cStock.dayPriceHighestArray[-i:].max()))
    print("\t".join(headWrited))
    print("\t".join(wordWrited))

def main(cStock):
    print ("һ�� ������Ŀ�ģ�1 ���� 2 T�۲� 3 ���Ʋ�λ 4 ֹ��")
    print ("���� ����������1 �۲� 2 ʱ��� �۲�û����ʱ���ˣ�ҲҪ����")
    print ("���� ��������Ҫע�⣺1. ���ɱ�����10��30ǰ���� 2.�߿�10��30ǰ����")
    print ("�ġ� ���壬ָ����ѹ��λ��������������")
    print ("-"*72)
    
    outPutPriceRef(cStock)
   
   
    ##����㣺��15����K�ߵ�֧��λ����T
    ##׷�ߵ㣺�Ƿ�����3������Բ���׷�ߡ�
    ##�����㣺5���ڸߵ㣬��������3���㡣
    ##����㣺������λ���ߴ����鲻�á�

## ���Ԥ�⵱�մ��̺ã��ý��ڸߵ��97%��Ϊ�����λ��
## Ԥ����̲��ã��ý��ڵ͵�97%��Ϊ��λ��

## �����һ��Ҫ ��������Ԥ�ڣ�������Ҫ����׼ 

    countOfEle=len(cStock.dayStrList)
    dayRadioLinkPriceLowArray=np.zeros(countOfEle)
    for i in range(1,countOfEle):
        if cStock.dayPriceLowestArray[i-1]>0:
            dayRadioLinkPriceLowArray[i]=100*(cStock.dayPriceLowestArray[i]-cStock.dayPriceLowestArray[i-1])/cStock.dayPriceLowestArray[i-1]
#    print(dayRadioLinkPriceLowArray[-10:])
    
    
##----ģʽʶ�������ۼ���ģ��
    ## ����ƥ������ȡ�����
    ##�������һ��ƥ���յ���ͼ۵��Ƿ�
    print("-"*72)
    print("\nģʽʶ�𷨼��㣺")
    print("-"*72)
#    patternRecCalTPrice(cStock,dayRadioLinkPriceLowArray)
##----ģʽʶ�������ۼ���ģ��
  
##----���Ż����������ۼ���ģ��
##��ϸ��������㷨
##����3�յ���ͼ�������ʽ��ϣ�����ѡ14��
    kPeriod=7 ##�������
    indexDateFit=-3
    ##Ҳ������np.vstack((x,y,z))���fData
    fDataLow=np.array([cStock.dayPriceLowestArray[indexDateFit-2-kPeriod:indexDateFit-2],\
            cStock.dayPriceLowestArray[indexDateFit-1-kPeriod:indexDateFit-1],\
            cStock.dayPriceLowestArray[indexDateFit-kPeriod:indexDateFit]])
    guess = (0.3,0.4,0.3,0)
    paramsLow, pcovLow = optimize.curve_fit(func, fDataLow,cStock.dayPriceLowestArray[-kPeriod:], guess)
    
    fDataHigh=np.array([cStock.dayPriceHighestArray[indexDateFit-2-kPeriod:indexDateFit-2],\
            cStock.dayPriceHighestArray[indexDateFit-1-kPeriod:indexDateFit-1],\
            cStock.dayPriceHighestArray[indexDateFit-kPeriod:indexDateFit]])
    paramsHigh, pcovHigh = optimize.curve_fit(func, fDataHigh,cStock.dayPriceHighestArray[-kPeriod:], guess)
#    print(paramsLow) ##��С���˷��������
    
#    historyPrint_optimize_curve_fit(cStock,countOfEle,kPeriod,paramsLow)
    
    print("-"*72)
    print("���Ż����㣺")
    print("-"*72)
    priceTbuy=(cStock.dayPriceLowestArray[-3:]*paramsLow[:3]).sum()+paramsLow[3]
    priceTsell=priceTbuy*1.025
    printTStop=priceTbuy*0.975
    priceTfitHigh=(cStock.dayPriceHighestArray[-3:]*paramsHigh[:3]).sum()+paramsHigh[3]
    print("���Ż�T-buy��: {:.2f}��T-sell��: {:.2f}, T-FitHigh��: {:.2f}, T-stop��: {:.2f}".format(priceTbuy,priceTsell,priceTfitHigh,printTStop))
##----���Ż�����������

    print("-"*72)
##----5����ֵ��������ģ��
    print("\n��ֵ�����㣺")
    print("-"*72)
    for period in [3,5,7]:
        indexHighPoint=Ccomfunc.rindex(cStock.dayPriceHighestFList,max(cStock.dayPriceHighestFList[countOfEle-period:]))
        indexLowPoint=Ccomfunc.rindex(cStock.dayPriceLowestFList,min(cStock.dayPriceLowestFList[countOfEle-period:]))
        priceHigh=cStock.dayPriceHighestFList[indexHighPoint]
        priceLow=cStock.dayPriceLowestFList[indexLowPoint]
        print("{}����ߵ�:{}����������:{}, {}����͵�:{}����������:{}".format( \
                period,priceHigh,cStock.dayStrList[indexHighPoint], \
                period,priceLow,cStock.dayStrList[indexLowPoint]))
        print("-"*72)
##----5����ֵ��������ģ��

##----���̵ķ��Ȳ��������
    print("-"*72)
    print("\n���ô��̵����ķ��Ȳ����������")
    print("-"*72)
##----ģ��

##----�������ڵ����ķ��Ⱦ�ֵ
    print("-"*72)
    print("\n�������ڵ����ľ�ֵ����")
    print("-"*72)
##----ģ��


    print("-"*72)
    for i in range(-3,0): ##ѭ��ָ����ʼ��ƥ��ָ����1
        weekDay=Ccomfunc.convertDateStr2Date(cStock.dayStrList[i]).isoweekday() 
        resultLine="{},����{}\t���̼�:{}\t�Ƿ�:{}\t���ܻ���:{}\t��������:{}".format(\
                cStock.dayStrList[i],weekDay,cStock.dayPriceClosedArray[i],cStock.dayRiseRateFList[i],\
                cStock.dayRadioLinkOfTradeVolumeFList[i],cStock.dayWaveRateFList[i])
        print resultLine

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
    stocIDkList=["002152"]
    for stockID in stocIDkList:
        curStock=Cstock.Stock(stockID)
        curStock.list2array()
        main(curStock)
    
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
