# -*- coding: cp936 -*-
import os
import shutil

if __name__=="__main__":

    A=3.46                  ##含油面积 km2
    h=26.2                   ##有效厚度 m
    pore=0.104            ##孔隙度 0.00
    So=0.55                   ##含油饱和度0.00
    density=0.7869    ##地面原油密度
    Boi=1.7462         ##原油体积系数
    GOR=241.4        ##汽油比m3/m3
    
    N=100*A*h*pore*So*density/Boi  ## 地质储量
    N_Gas=N*GOR/density

    print "N=",N," 万吨 \nN_gas=",N_Gas,"万m3"

    
