# -*- coding: utf-8 -*-
from PyQt4 import QtGui # Import the PyQt4 module we'll need
import sys # We need sys so that we can pass argv to QApplication
from PyQt4.QtGui import *

import mainUI # This file holds our MainWindow and all design related things
              # it also keeps events etc that we defined in Qt Designer

from Cstock import Stock
from candleStickPlot import drawCandleStick

import configOS
import stockPatternRecognition
import copyFile2Dir
import start

def updateListWidgetItem(listWidget,listStr):
    listWidget.clear()
    for iDate in listStr:
        item = QListWidgetItem(iDate)
        listWidget.addItem(item)

class mainApp(QtGui.QMainWindow, mainUI.Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined
         
        self.comboBoxStockID.clear()
        self.comboBoxStockID.addItems(configOS.stockIDMarketList)

        self.comboBoxStockID.currentIndexChanged.connect(self.setupListWidget)
  
        dateList=configOS.config.get('patternRecDate', 'SH').split(',')
        for iDate in dateList:
            item = QListWidgetItem(iDate)
            self.listWidgetMatchDate.addItem(item)

        self.pButtonSelect.clicked.connect(self.selectExe)  # When the button is pressed
        self.btnCalGDP.clicked.connect(self.calGDP)
        self.btnTradeInfor.clicked.connect(self.tradeWarn)
        self.btnPatternRecAna.clicked.connect(self.calPatternRec)

        ##交易策略入库
        self.btnInertDataTradeTactics.clicked.connect(self.inertDataTradeTactics)

        ##数据管理 目录管理
        self.btnCopyData2Dir.clicked.connect(self.copyData2dir)
    
    def inertDataTradeTactics(self):
        QMessageBox.about(self, u"提示",u"交易策略已入库")

    def copyData2dir(self):
        copyFile2Dir.copyData2Dir()
        QMessageBox.about(self, u"提示",u"数据已经复制到文件夹。")

    def calPatternRec(self):
        sDate=str(self.lineEditDateRec.text())
        print sDate
        stockPatternRecognition.mainAppCall(sDate)

    def tradeWarn(self):
        for stockID in ["999999"]:
            curStock=Stock(stockID)
            curStock.list2array()
            start.main(curStock)
    
    def setupListWidget(self,iItem):
        stockIDselect=self.comboBoxStockID.itemText(iItem)
        dateList=[]
        if stockIDselect=="999999":
            dateList=configOS.config.get('patternRecDate', 'SH').split(',')
        if stockIDselect=="399001":
            dateList=configOS.config.get('patternRecDate', 'SZ').split(',')
        print dateList
        updateListWidgetItem(self.listWidgetMatchDate,dateList)

    def calGDP(self):
        fGDPsh=float(self.lineEditMarketValueSH.text())
        fGDPsz=float(self.lineEditMarketValueSZ.text())
        fGDP2014=63.6
        QMessageBox.about(self, u"计算结果",u"两市市值总和占2014GDP比例:\t{:.2f}".format((fGDPsh+fGDPsz)/fGDP2014))
    
    def selectExe(self):
        stockID=str(self.comboBoxStockID.currentText())
        print stockID
        curStock=Stock(stockID)
        dateFind=self.listWidgetMatchDate.currentItem().text()
        drawCandleStick(curStock,dateFind)

def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = mainApp()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()              
