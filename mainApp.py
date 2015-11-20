# -*- coding: utf-8 -*-
from PyQt4 import QtGui # Import the PyQt4 module we'll need
import sys # We need sys so that we can pass argv to QApplication
from PyQt4.QtGui import *

import mainUI # This file holds our MainWindow and all design related things
              # it also keeps events etc that we defined in Qt Designer

from Cstock import Stock
from candleStickPlot import drawCandleStick

class mainApp(QtGui.QMainWindow, mainUI.Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined
        dateList="2003/05/28	2003/12/08	2005/02/18	2011/05/12	2012/11/27	2013/05/14	2014/01/03".split()                    
        for iDate in dateList:
            item = QListWidgetItem(iDate)
            self.listWidgetMatchDate.addItem(item)

        self.pButtonSelect.clicked.connect(self.selectExe)  # When the button is pressed

    def selectExe(self):
        stockID='999999'
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
#    QMessageBox.about(self, u"标题",u"中文")
