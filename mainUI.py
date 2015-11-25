# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created: Wed Nov 25 16:36:49 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(852, 673)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 831, 611))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.lineEditMarketValueSH = QtGui.QLineEdit(self.tab)
        self.lineEditMarketValueSH.setGeometry(QtCore.QRect(90, 60, 121, 31))
        self.lineEditMarketValueSH.setObjectName(_fromUtf8("lineEditMarketValueSH"))
        self.btnCalGDP = QtGui.QPushButton(self.tab)
        self.btnCalGDP.setGeometry(QtCore.QRect(280, 80, 75, 31))
        self.btnCalGDP.setObjectName(_fromUtf8("btnCalGDP"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 54, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEditMarketValueSZ = QtGui.QLineEdit(self.tab)
        self.lineEditMarketValueSZ.setGeometry(QtCore.QRect(90, 100, 121, 31))
        self.lineEditMarketValueSZ.setObjectName(_fromUtf8("lineEditMarketValueSZ"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(220, 70, 54, 12))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(220, 110, 54, 12))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.lineEditStockID = QtGui.QLineEdit(self.tab_6)
        self.lineEditStockID.setGeometry(QtCore.QRect(110, 40, 121, 31))
        self.lineEditStockID.setObjectName(_fromUtf8("lineEditStockID"))
        self.btnPatternRec = QtGui.QPushButton(self.tab_6)
        self.btnPatternRec.setGeometry(QtCore.QRect(240, 40, 75, 31))
        self.btnPatternRec.setObjectName(_fromUtf8("btnPatternRec"))
        self.label = QtGui.QLabel(self.tab_6)
        self.label.setGeometry(QtCore.QRect(40, 50, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.listWidgetMatchDate = QtGui.QListWidget(self.tab_6)
        self.listWidgetMatchDate.setGeometry(QtCore.QRect(40, 210, 256, 291))
        self.listWidgetMatchDate.setObjectName(_fromUtf8("listWidgetMatchDate"))
        self.pButtonSelect = QtGui.QPushButton(self.tab_6)
        self.pButtonSelect.setGeometry(QtCore.QRect(310, 220, 71, 31))
        self.pButtonSelect.setObjectName(_fromUtf8("pButtonSelect"))
        self.comboBoxStockID = QtGui.QComboBox(self.tab_6)
        self.comboBoxStockID.setGeometry(QtCore.QRect(40, 120, 131, 31))
        self.comboBoxStockID.setObjectName(_fromUtf8("comboBoxStockID"))
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 852, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.btnPatternRec, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEditStockID.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "基于模式识别的stock交易系统", None))
        self.lineEditMarketValueSH.setText(_translate("MainWindow", "29.99", None))
        self.btnCalGDP.setText(_translate("MainWindow", "计算", None))
        self.label_2.setText(_translate("MainWindow", "上证市值", None))
        self.label_3.setText(_translate("MainWindow", "深证市值", None))
        self.lineEditMarketValueSZ.setText(_translate("MainWindow", "22.65", None))
        self.label_4.setText(_translate("MainWindow", "万亿元", None))
        self.label_5.setText(_translate("MainWindow", "万亿元", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "每日提醒", None))
        self.btnPatternRec.setText(_translate("MainWindow", "识别", None))
        self.label.setText(_translate("MainWindow", "股票代码", None))
        self.pButtonSelect.setText(_translate("MainWindow", "选择", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "模式识别", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "风险控制", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "仓位管理", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "量化交易", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "信息获取", None))
        self.menu.setTitle(_translate("MainWindow", "系统", None))
        self.menu_2.setTitle(_translate("MainWindow", "帮助", None))

