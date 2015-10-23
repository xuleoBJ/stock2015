# -*- coding: utf-8 -*-
import datetime
import ConfigParser

def getStockID():
    config = ConfigParser.ConfigParser()
    config.read('config.ini')
    return config.get('stock','stockID')

##近期走势
def trend():
    return


def mymain():
    stockIDList = getStockID().split(",")
    print stockIDList[1]


if __name__ == "__main__":
    mymain()
