# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created: Fri Nov 20 10:53:37 2015
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
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 781, 541))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
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
        self.listWidgetMatchDate.setGeometry(QtCore.QRect(40, 100, 256, 291))
        self.listWidgetMatchDate.setObjectName(_fromUtf8("listWidgetMatchDate"))
        self.pButtonSelect = QtGui.QPushButton(self.tab_6)
        self.pButtonSelect.setGeometry(QtCore.QRect(330, 110, 71, 31))
        self.pButtonSelect.setObjectName(_fromUtf8("pButtonSelect"))
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

