import os
print "hello,world"
## engulfing pattern 确定趋势中的大阴包大阳，算法是第二天收盘价小于第一天的开盘价并且两根长柱子
if curStock.dayRiseRateFList[i-1]>=2 and curStock.dayRiseRateFList[i]<=-2 and curStock.priceCloseingFList[i]<curStock.dayPriceOpenFList[i-1] and  curStock.priceCloseingFList[i-1]<curStock.dayPriceOpenFList[i]:

## price rate	
if 0<curStock.dayRiseRateFList[i-2]<=1 and -0.5<=curStock.dayRiseRateFList[i-1]<=0.5 and 2<=curStock.dayRiseRateFList[i]:

## 连跌3天，但是每天的跌幅变小
if curStock.dayRiseRateFList[i-2]<= curStock.dayRiseRateFList[i-1]<=curStock.dayRiseRateFList[i]<0 and curStock.priceCloseingFList[i-2]>curStock.priceCloseingFList[i-1]>curStock.priceCloseingFList[i]:

