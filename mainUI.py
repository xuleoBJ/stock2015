# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created: Wed Dec 23 11:33:44 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui

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
        MainWindow.resize(763, 672)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 761, 641))
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tbgImportInfor = QtGui.QWidget()
        self.tbgImportInfor.setObjectName(_fromUtf8("tbgImportInfor"))
        self.groupBox_3 = QtGui.QGroupBox(self.tbgImportInfor)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 40, 701, 151))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.groupBox_4 = QtGui.QGroupBox(self.tbgImportInfor)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 220, 701, 151))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.groupBox_5 = QtGui.QGroupBox(self.tbgImportInfor)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 400, 701, 171))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.tabWidget.addTab(self.tbgImportInfor, _fromUtf8(""))
        self.tbgAnaTrend = QtGui.QWidget()
        self.tbgAnaTrend.setObjectName(_fromUtf8("tbgAnaTrend"))
        self.groupBox = QtGui.QGroupBox(self.tbgAnaTrend)
        self.groupBox.setGeometry(QtCore.QRect(340, 30, 381, 71))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.btnCalGDP = QtGui.QPushButton(self.groupBox)
        self.btnCalGDP.setGeometry(QtCore.QRect(270, 20, 75, 31))
        self.btnCalGDP.setObjectName(_fromUtf8("btnCalGDP"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 23, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(32, 46, 54, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(220, 22, 54, 12))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(220, 44, 54, 12))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.splitter_2 = QtGui.QSplitter(self.groupBox)
        self.splitter_2.setGeometry(QtCore.QRect(80, 20, 133, 40))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.lineEditMarketValueSH = QtGui.QLineEdit(self.splitter_2)
        self.lineEditMarketValueSH.setObjectName(_fromUtf8("lineEditMarketValueSH"))
        self.lineEditMarketValueSZ = QtGui.QLineEdit(self.splitter_2)
        self.lineEditMarketValueSZ.setObjectName(_fromUtf8("lineEditMarketValueSZ"))
        self.groupBox_2 = QtGui.QGroupBox(self.tbgAnaTrend)
        self.groupBox_2.setGeometry(QtCore.QRect(340, 150, 301, 391))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 201, 41))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEditDateRec = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditDateRec.setGeometry(QtCore.QRect(10, 60, 121, 21))
        self.lineEditDateRec.setObjectName(_fromUtf8("lineEditDateRec"))
        self.btnPatternRecAna = QtGui.QPushButton(self.groupBox_2)
        self.btnPatternRecAna.setGeometry(QtCore.QRect(140, 50, 75, 31))
        self.btnPatternRecAna.setObjectName(_fromUtf8("btnPatternRecAna"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 100, 131, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBoxStockID = QtGui.QComboBox(self.groupBox_2)
        self.comboBoxStockID.setGeometry(QtCore.QRect(10, 140, 111, 31))
        self.comboBoxStockID.setObjectName(_fromUtf8("comboBoxStockID"))
        self.pButtonSelect = QtGui.QPushButton(self.groupBox_2)
        self.pButtonSelect.setGeometry(QtCore.QRect(20, 190, 71, 31))
        self.pButtonSelect.setObjectName(_fromUtf8("pButtonSelect"))
        self.listWidgetMatchDate = QtGui.QListWidget(self.groupBox_2)
        self.listWidgetMatchDate.setGeometry(QtCore.QRect(140, 90, 131, 291))
        self.listWidgetMatchDate.setObjectName(_fromUtf8("listWidgetMatchDate"))
        self.lineEditInputStockIDTrend = QtGui.QLineEdit(self.tbgAnaTrend)
        self.lineEditInputStockIDTrend.setGeometry(QtCore.QRect(20, 80, 101, 31))
        self.lineEditInputStockIDTrend.setObjectName(_fromUtf8("lineEditInputStockIDTrend"))
        self.label_12 = QtGui.QLabel(self.tbgAnaTrend)
        self.label_12.setGeometry(QtCore.QRect(20, 40, 131, 41))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.lineEditTradeDate = QtGui.QLineEdit(self.tbgAnaTrend)
        self.lineEditTradeDate.setGeometry(QtCore.QRect(140, 80, 121, 31))
        self.lineEditTradeDate.setObjectName(_fromUtf8("lineEditTradeDate"))
        self.btnCycleTrend = QtGui.QPushButton(self.tbgAnaTrend)
        self.btnCycleTrend.setGeometry(QtCore.QRect(140, 130, 75, 23))
        self.btnCycleTrend.setObjectName(_fromUtf8("btnCycleTrend"))
        self.btnQuantitativeTrade = QtGui.QPushButton(self.tbgAnaTrend)
        self.btnQuantitativeTrade.setGeometry(QtCore.QRect(140, 161, 75, 23))
        self.btnQuantitativeTrade.setObjectName(_fromUtf8("btnQuantitativeTrade"))
        self.label_14 = QtGui.QLabel(self.tbgAnaTrend)
        self.label_14.setGeometry(QtCore.QRect(140, 40, 131, 41))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.btnTradeInfor = QtGui.QPushButton(self.tbgAnaTrend)
        self.btnTradeInfor.setGeometry(QtCore.QRect(31, 131, 75, 23))
        self.btnTradeInfor.setObjectName(_fromUtf8("btnTradeInfor"))
        self.btnMarketAna = QtGui.QPushButton(self.tbgAnaTrend)
        self.btnMarketAna.setGeometry(QtCore.QRect(30, 160, 75, 23))
        self.btnMarketAna.setObjectName(_fromUtf8("btnMarketAna"))
        self.tabWidget.addTab(self.tbgAnaTrend, _fromUtf8(""))
        self.tbgStockSelect = QtGui.QWidget()
        self.tbgStockSelect.setObjectName(_fromUtf8("tbgStockSelect"))
        self.btnMarketMoodAna_4 = QtGui.QPushButton(self.tbgStockSelect)
        self.btnMarketMoodAna_4.setGeometry(QtCore.QRect(70, 40, 101, 31))
        self.btnMarketMoodAna_4.setObjectName(_fromUtf8("btnMarketMoodAna_4"))
        self.btnMarketMoodAna_5 = QtGui.QPushButton(self.tbgStockSelect)
        self.btnMarketMoodAna_5.setGeometry(QtCore.QRect(200, 40, 101, 31))
        self.btnMarketMoodAna_5.setObjectName(_fromUtf8("btnMarketMoodAna_5"))
        self.btnMarketMoodAna_6 = QtGui.QPushButton(self.tbgStockSelect)
        self.btnMarketMoodAna_6.setGeometry(QtCore.QRect(330, 40, 101, 31))
        self.btnMarketMoodAna_6.setObjectName(_fromUtf8("btnMarketMoodAna_6"))
        self.btnMarketMoodAna_8 = QtGui.QPushButton(self.tbgStockSelect)
        self.btnMarketMoodAna_8.setGeometry(QtCore.QRect(460, 40, 101, 31))
        self.btnMarketMoodAna_8.setObjectName(_fromUtf8("btnMarketMoodAna_8"))
        self.btnMarketMoodAna_10 = QtGui.QPushButton(self.tbgStockSelect)
        self.btnMarketMoodAna_10.setGeometry(QtCore.QRect(70, 100, 101, 31))
        self.btnMarketMoodAna_10.setObjectName(_fromUtf8("btnMarketMoodAna_10"))
        self.lineEditDateTradeTactics_2 = QtGui.QLineEdit(self.tbgStockSelect)
        self.lineEditDateTradeTactics_2.setGeometry(QtCore.QRect(50, 200, 141, 21))
        self.lineEditDateTradeTactics_2.setText(_fromUtf8(""))
        self.lineEditDateTradeTactics_2.setObjectName(_fromUtf8("lineEditDateTradeTactics_2"))
        self.label_10 = QtGui.QLabel(self.tbgStockSelect)
        self.label_10.setGeometry(QtCore.QRect(50, 170, 201, 41))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.btnMarketMoodAna_11 = QtGui.QPushButton(self.tbgStockSelect)
        self.btnMarketMoodAna_11.setGeometry(QtCore.QRect(305, 195, 90, 30))
        self.btnMarketMoodAna_11.setObjectName(_fromUtf8("btnMarketMoodAna_11"))
        self.spinBox = QtGui.QSpinBox(self.tbgStockSelect)
        self.spinBox.setGeometry(QtCore.QRect(250, 200, 42, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label_11 = QtGui.QLabel(self.tbgStockSelect)
        self.label_11.setGeometry(QtCore.QRect(210, 190, 41, 41))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.groupBox_6 = QtGui.QGroupBox(self.tbgStockSelect)
        self.groupBox_6.setGeometry(QtCore.QRect(40, 240, 661, 111))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.groupBox_7 = QtGui.QGroupBox(self.tbgStockSelect)
        self.groupBox_7.setGeometry(QtCore.QRect(40, 390, 661, 111))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.btnAnaKpattern = QtGui.QPushButton(self.tbgStockSelect)
        self.btnAnaKpattern.setGeometry(QtCore.QRect(570, 530, 131, 31))
        self.btnAnaKpattern.setObjectName(_fromUtf8("btnAnaKpattern"))
        self.lineEditDateKHistory = QtGui.QLineEdit(self.tbgStockSelect)
        self.lineEditDateKHistory.setGeometry(QtCore.QRect(420, 530, 121, 31))
        self.lineEditDateKHistory.setObjectName(_fromUtf8("lineEditDateKHistory"))
        self.label_13 = QtGui.QLabel(self.tbgStockSelect)
        self.label_13.setGeometry(QtCore.QRect(270, 520, 201, 41))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_7 = QtGui.QLabel(self.tbgStockSelect)
        self.label_7.setGeometry(QtCore.QRect(40, 520, 131, 41))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEditStockID_2 = QtGui.QLineEdit(self.tbgStockSelect)
        self.lineEditStockID_2.setGeometry(QtCore.QRect(140, 530, 121, 31))
        self.lineEditStockID_2.setObjectName(_fromUtf8("lineEditStockID_2"))
        self.tabWidget.addTab(self.tbgStockSelect, _fromUtf8(""))
        self.tbgRiskManage = QtGui.QWidget()
        self.tbgRiskManage.setObjectName(_fromUtf8("tbgRiskManage"))
        self.btnMarketMoodAna_2 = QtGui.QPushButton(self.tbgRiskManage)
        self.btnMarketMoodAna_2.setGeometry(QtCore.QRect(60, 40, 101, 31))
        self.btnMarketMoodAna_2.setObjectName(_fromUtf8("btnMarketMoodAna_2"))
        self.btnMarketMoodAna_3 = QtGui.QPushButton(self.tbgRiskManage)
        self.btnMarketMoodAna_3.setGeometry(QtCore.QRect(190, 40, 101, 31))
        self.btnMarketMoodAna_3.setObjectName(_fromUtf8("btnMarketMoodAna_3"))
        self.btnMarketMoodAna_7 = QtGui.QPushButton(self.tbgRiskManage)
        self.btnMarketMoodAna_7.setGeometry(QtCore.QRect(320, 40, 101, 31))
        self.btnMarketMoodAna_7.setObjectName(_fromUtf8("btnMarketMoodAna_7"))
        self.tabWidget.addTab(self.tbgRiskManage, _fromUtf8(""))
        self.tbg_Data = QtGui.QWidget()
        self.tbg_Data.setObjectName(_fromUtf8("tbg_Data"))
        self.btnCopyData2Dir = QtGui.QPushButton(self.tbg_Data)
        self.btnCopyData2Dir.setGeometry(QtCore.QRect(60, 40, 101, 31))
        self.btnCopyData2Dir.setObjectName(_fromUtf8("btnCopyData2Dir"))
        self.lineEditDateTradeTactics = QtGui.QLineEdit(self.tbg_Data)
        self.lineEditDateTradeTactics.setGeometry(QtCore.QRect(100, 150, 131, 31))
        self.lineEditDateTradeTactics.setText(_fromUtf8(""))
        self.lineEditDateTradeTactics.setObjectName(_fromUtf8("lineEditDateTradeTactics"))
        self.label_8 = QtGui.QLabel(self.tbg_Data)
        self.label_8.setGeometry(QtCore.QRect(60, 160, 54, 12))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineEditPlanTradeTactics = QtGui.QLineEdit(self.tbg_Data)
        self.lineEditPlanTradeTactics.setGeometry(QtCore.QRect(100, 190, 131, 181))
        self.lineEditPlanTradeTactics.setText(_fromUtf8(""))
        self.lineEditPlanTradeTactics.setObjectName(_fromUtf8("lineEditPlanTradeTactics"))
        self.label_9 = QtGui.QLabel(self.tbg_Data)
        self.label_9.setGeometry(QtCore.QRect(40, 190, 54, 12))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.btnInertDataTradeTactics = QtGui.QPushButton(self.tbg_Data)
        self.btnInertDataTradeTactics.setGeometry(QtCore.QRect(50, 390, 101, 31))
        self.btnInertDataTradeTactics.setObjectName(_fromUtf8("btnInertDataTradeTactics"))
        self.tabWidget.addTab(self.tbg_Data, _fromUtf8(""))
        self.tbgMoneyManage = QtGui.QWidget()
        self.tbgMoneyManage.setObjectName(_fromUtf8("tbgMoneyManage"))
        self.tabWidget.addTab(self.tbgMoneyManage, _fromUtf8(""))
        self.tbgWebInfor = QtGui.QWidget()
        self.tbgWebInfor.setObjectName(_fromUtf8("tbgWebInfor"))
        self.btnMarketMoodAna_9 = QtGui.QPushButton(self.tbgWebInfor)
        self.btnMarketMoodAna_9.setGeometry(QtCore.QRect(30, 30, 101, 31))
        self.btnMarketMoodAna_9.setObjectName(_fromUtf8("btnMarketMoodAna_9"))
        self.tabWidget.addTab(self.tbgWebInfor, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 763, 23))
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
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "基于模式识别的stock交易系统", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "每日提示", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "本周提示", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "中长期提示", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbgImportInfor), _translate("MainWindow", "关键提示", None))
        self.groupBox.setTitle(_translate("MainWindow", "GDP计算", None))
        self.btnCalGDP.setText(_translate("MainWindow", "计算", None))
        self.label_2.setText(_translate("MainWindow", "上证市值", None))
        self.label_3.setText(_translate("MainWindow", "深证市值", None))
        self.label_4.setText(_translate("MainWindow", "万亿元", None))
        self.label_5.setText(_translate("MainWindow", "万亿元", None))
        self.lineEditMarketValueSH.setText(_translate("MainWindow", "29.99", None))
        self.lineEditMarketValueSZ.setText(_translate("MainWindow", "22.65", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "模式识别", None))
        self.label_6.setText(_translate("MainWindow", "请输入交易日（2008/08/08）", None))
        self.btnPatternRecAna.setText(_translate("MainWindow", "模式识别", None))
        self.label.setText(_translate("MainWindow", "请选择查看股票代码", None))
        self.pButtonSelect.setText(_translate("MainWindow", "选择", None))
        self.lineEditInputStockIDTrend.setText(_translate("MainWindow", "999999", None))
        self.label_12.setText(_translate("MainWindow", "请输入交易代码：", None))
        self.lineEditTradeDate.setText(_translate("MainWindow", "2008/08/08", None))
        self.btnCycleTrend.setText(_translate("MainWindow", "周期趋势", None))
        self.btnQuantitativeTrade.setText(_translate("MainWindow", "量化交易", None))
        self.label_14.setText(_translate("MainWindow", "分析日：", None))
        self.btnTradeInfor.setText(_translate("MainWindow", "交易提示", None))
        self.btnMarketAna.setText(_translate("MainWindow", "时空分析", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbgAnaTrend), _translate("MainWindow", "趋势分析", None))
        self.btnMarketMoodAna_4.setText(_translate("MainWindow", "行业前景", None))
        self.btnMarketMoodAna_5.setText(_translate("MainWindow", "财务状况", None))
        self.btnMarketMoodAna_6.setText(_translate("MainWindow", "管理团队", None))
        self.btnMarketMoodAna_8.setText(_translate("MainWindow", "股票个性", None))
        self.btnMarketMoodAna_10.setText(_translate("MainWindow", "股票弹性", None))
        self.label_10.setText(_translate("MainWindow", "请输入交易日（2008/08/08）", None))
        self.btnMarketMoodAna_11.setText(_translate("MainWindow", "分析选取", None))
        self.label_11.setText(_translate("MainWindow", "区间+", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "周期性选票", None))
        self.groupBox_7.setTitle(_translate("MainWindow", "基本面选票", None))
        self.btnAnaKpattern.setText(_translate("MainWindow", "K线分析", None))
        self.lineEditDateKHistory.setText(_translate("MainWindow", "2008/08/08", None))
        self.label_13.setText(_translate("MainWindow", "请输入交易日（2008/08/08）", None))
        self.label_7.setText(_translate("MainWindow", "请输入交易代码：", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbgStockSelect), _translate("MainWindow", "选票系统", None))
        self.btnMarketMoodAna_2.setText(_translate("MainWindow", "时间周期分析", None))
        self.btnMarketMoodAna_3.setText(_translate("MainWindow", "空间周期分析", None))
        self.btnMarketMoodAna_7.setText(_translate("MainWindow", "退出原则", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbgRiskManage), _translate("MainWindow", "风险控制", None))
        self.btnCopyData2Dir.setText(_translate("MainWindow", "复制数据", None))
        self.label_8.setText(_translate("MainWindow", "日期", None))
        self.label_9.setText(_translate("MainWindow", "交易策略", None))
        self.btnInertDataTradeTactics.setText(_translate("MainWindow", "数据入库", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbg_Data), _translate("MainWindow", "数据管理", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbgMoneyManage), _translate("MainWindow", "经验教训", None))
        self.btnMarketMoodAna_9.setText(_translate("MainWindow", "欧洲市场", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbgWebInfor), _translate("MainWindow", "信息获取", None))
        self.menu.setTitle(_translate("MainWindow", "系统", None))
        self.menu_2.setTitle(_translate("MainWindow", "帮助", None))

