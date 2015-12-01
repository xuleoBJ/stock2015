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



def main(curStock):
    print ("������Ŀ�ģ�1 ���� 2 T�۲� 3 ���Ʋ�λ 4 ֹ��")
    print ("����������1 �۸�λ 2 ʱ���")
    print ("��T�۸���㣬��t�����ɴ������������ķ�����һ��Ҫ�м۲�������롣��")
    print ("-"*72)
   
##  �����ʽ���������ԭ��

## �����һ��Ҫ ��������Ԥ�ڣ�������Ҫ����׼ 

    
##----�����ʽ���ѡ�ɱ�ļ�����ԭ�����ģ��
    ## ����ƥ������ȡ�����
    ##�������һ��ƥ���յ���ͼ۵��Ƿ�
    print("-"*72)
    print("\n�����ʽ���㣺")
    print("-"*72)
#    patternRecCalTPrice(curStock,dayRadioLinkPriceLowArray)
##----ģʽʶ�������ۼ���ģ��
  

##----�����ʽ�������ģ��
##----end �����ʽ�������ģ��
    
    
##----���Ż�����������

    print("-"*72)
##----�г�������������ģ��
    print("-"*72)
    print("\n�г����������㣺")
    print("-"*72)
##����
    if curStock.dayRiseRateArray[-1]>0:
        if 1.5<=curStock.dayRadioLinkOfTradeVolumeArray[-1]:
            print("�ž������ǡ�")
        if 1<curStock.dayRadioLinkOfTradeVolumeArray[-1]<1.5:
            print("΢�������ǡ�")
        if curStock.dayRadioLinkOfTradeVolumeArray[-1]<1:
            print("�������ǡ�")
##�µ�
    if curStock.dayRiseRateArray[-1]<0:
        if 1.5<=curStock.dayRadioLinkOfTradeVolumeArray[-1]:
            print("�޷����µ���")
        if 1<curStock.dayRadioLinkOfTradeVolumeArray[-1]<1.5:
            print("΢�����µ���")
        if curStock.dayRadioLinkOfTradeVolumeArray[-1]<1:
            print("�����µ���")
    marketMood=1
    if marketMood<=0.5:
        print("3��T����{:.2f}".format(priceLow3days*0.5+priceClose3days*0.5))

##----�г�������������ģ��

    
    print ("�ϸ��ִ��ֹ�𷽰���")

if __name__=="__main__":
    
    print("\n"+"#"*80)
    
    print ("�ϸ��ִ��ֹ�𷽰���")
    print ("�����Ʊ��Ҫ����5֧��")
    print ("�ϸ�Ĳ�λ����")
    
    startClock=time.clock() ##��¼����ʼ����ʱ��
    for stockID in configOS.stockIDList:
        curStock=Cstock.Stock(stockID)
        curStock.list2array()
        main(curStock)
    
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
