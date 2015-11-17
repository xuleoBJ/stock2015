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
    
    curStock=Cstock.Stock('600787')
    
    print ("��T�۸���㣬��t�����ɴ������������ķ�����")
    arrayDayPriceLowest=np.array(curStock.dayPriceLowestFList)

    ## ����-1.5���ϣ��������粻����T�������ʶȵ����������T�� 
    ## �����T�ļ۸���15����K�ߵ�֧�Ż���������λ��
    ## �����Ǽ��� ���Ҷ� �������ߡ� 
    
    ##T�ļ۸��� ����15���ӵ�֧�ż�+����Ӧ����������͵���Ⱦ�ֵ+���ɵĴ����ǵ���)/4��Ϊ��׼��T������
    ##������15����K�ߵ�֧��λ����T��

    ##��T�ļ۸��������2���� �������

    ## �������Ԥ�����鲻�ã����Բ��Ӳ������ɲ��� 
    ## ��TӦ�ø��ݿ��̼ۣ���������ɵ����ƹ�ϵ���������׵�����ע�Ᵽ�ֲ�λ�����Ǵ��̱��������У������ǵ�����
    ## �����к����е��жϣ���Ҫ��ϴ��̺͸�����������
    ## ���T���� ���߲�λ�����Ļ�������β��2��45������������ɲ�׬Ǯ��������Ǯ��
    ## ���Ʊ����ű��ǣ����˾��Ƿ��ˣ����ֿ�����Ҳ������ô��ġ�һ��Ҳ���ᷢ�����ء�����ƽ̯�˲�λ���ա������˶��١�

    print(u"���5����ͼ�{}".format(arrayDayPriceLowest[-5:]))
    print(arrayDayPriceLowest[-5:].mean())
    
    print ("�ϸ��ִ��ֹ�𷽰���")
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


