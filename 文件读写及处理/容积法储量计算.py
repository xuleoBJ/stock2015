# -*- coding: cp936 -*-
import os
import shutil

if __name__=="__main__":

    A=3.46                  ##������� km2
    h=26.2                   ##��Ч��� m
    pore=0.104            ##��϶�� 0.00
    So=0.55                   ##���ͱ��Ͷ�0.00
    density=0.7869    ##����ԭ���ܶ�
    Boi=1.7462         ##ԭ�����ϵ��
    GOR=241.4        ##���ͱ�m3/m3
    
    N=100*A*h*pore*So*density/Boi  ## ���ʴ���
    N_Gas=N*GOR/density

    print "N=",N," ��� \nN_gas=",N_Gas,"��m3"

    
